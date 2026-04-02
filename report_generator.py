"""
PDF report generator for personality assessment results.

Generates a professional-looking PDF report for each respondent with:
  - Header with respondent name and date
  - 4-letter personality type
  - Visual polarity bars for each dimension
  - Percentage scores
  - Interpretive descriptions
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER

from questionnaire import DIMENSIONS
from interpretations import get_all_interpretations
from scoring import get_personality_type


# Color palette
COLOR_PRIMARY = HexColor("#2C3E50")
COLOR_ACCENT = HexColor("#3498DB")
COLOR_LEFT_BAR = HexColor("#3498DB")
COLOR_RIGHT_BAR = HexColor("#E74C3C")
COLOR_BAR_BG = HexColor("#ECF0F1")
COLOR_TEXT = HexColor("#2C3E50")
COLOR_LIGHT_TEXT = HexColor("#7F8C8D")
COLOR_WHITE = HexColor("#FFFFFF")


def generate_pdf_report(name, scores, output_path, date_taken=""):
    """
    Generate a PDF personality report for one respondent.

    Args:
        name: respondent's name
        scores: dict from scoring.calculate_all_scores()
        output_path: file path for the PDF output
        date_taken: optional date string
    """
    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)

    personality_type = get_personality_type(scores)
    interpretations = get_all_interpretations(scores)

    # --- Header ---
    y = height - 30 * mm

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(width / 2, y, "Personality Assessment Report")

    # Separator line
    y -= 8 * mm
    c.setStrokeColor(COLOR_ACCENT)
    c.setLineWidth(2)
    c.line(30 * mm, y, width - 30 * mm, y)

    # Name and date
    y -= 10 * mm
    c.setFont("Helvetica", 12)
    c.setFillColor(COLOR_TEXT)
    c.drawString(30 * mm, y, f"Name: {name}")
    if date_taken:
        c.drawRightString(width - 30 * mm, y, f"Date: {date_taken}")

    # Personality type box
    y -= 18 * mm
    box_width = 60 * mm
    box_height = 16 * mm
    box_x = (width - box_width) / 2
    c.setFillColor(COLOR_PRIMARY)
    c.roundRect(box_x, y - 2 * mm, box_width, box_height, 3 * mm, fill=1, stroke=0)
    c.setFillColor(COLOR_WHITE)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, y + 2 * mm, personality_type)

    y -= 6 * mm
    c.setFillColor(COLOR_LIGHT_TEXT)
    c.setFont("Helvetica", 9)
    c.drawCentredString(width / 2, y, "Your Personality Type")

    # --- Dimension Results ---
    y -= 16 * mm

    for dim in DIMENSIONS:
        dim_id = dim["id"]
        dim_scores = scores[dim_id]
        interp = interpretations[dim_id]

        # Dimension title
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(COLOR_PRIMARY)
        title = f"{dim_scores['left_pole']} vs {dim_scores['right_pole']}"
        c.drawString(30 * mm, y, title)

        # Score label
        y -= 7 * mm
        c.setFont("Helvetica", 10)
        c.setFillColor(COLOR_TEXT)
        score_text = (
            f"{dim_scores['left_percent']:.0f}% {dim_scores['left_pole']}  —  "
            f"{dim_scores['right_percent']:.0f}% {dim_scores['right_pole']}"
        )
        c.drawString(30 * mm, y, score_text)

        # Polarity bar
        y -= 8 * mm
        bar_x = 30 * mm
        bar_width = width - 60 * mm
        bar_height = 8 * mm

        # Background
        c.setFillColor(COLOR_BAR_BG)
        c.roundRect(bar_x, y, bar_width, bar_height, 2 * mm, fill=1, stroke=0)

        # Left portion (blue)
        left_width = bar_width * (dim_scores["left_percent"] / 100)
        if left_width > 0:
            c.setFillColor(COLOR_LEFT_BAR)
            c.roundRect(bar_x, y, max(left_width, 4 * mm), bar_height, 2 * mm, fill=1, stroke=0)

        # Right portion (red)
        right_width = bar_width * (dim_scores["right_percent"] / 100)
        if right_width > 0:
            c.setFillColor(COLOR_RIGHT_BAR)
            right_x = bar_x + bar_width - max(right_width, 4 * mm)
            c.roundRect(right_x, y, max(right_width, 4 * mm), bar_height, 2 * mm, fill=1, stroke=0)

        # Pole labels on bar
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(COLOR_WHITE)
        c.drawString(bar_x + 2 * mm, y + 2.5 * mm, dim_scores["left_code"])
        c.drawRightString(bar_x + bar_width - 2 * mm, y + 2.5 * mm, dim_scores["right_code"])

        # Interpretation label
        y -= 7 * mm
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(COLOR_ACCENT)
        c.drawString(30 * mm, y, interp["label"])

        # Interpretation description (wrapped text)
        y -= 4 * mm
        style = getSampleStyleSheet()["Normal"]
        style.fontName = "Helvetica"
        style.fontSize = 8.5
        style.leading = 11
        style.textColor = COLOR_TEXT

        para = Paragraph(interp["description"], style)
        para_width = bar_width
        w, h = para.wrap(para_width, 200 * mm)
        y -= h
        para.drawOn(c, 30 * mm, y)

        # Spacing between dimensions
        y -= 10 * mm

        # Check if we need a new page
        if y < 40 * mm:
            c.showPage()
            y = height - 30 * mm

    # --- Footer ---
    c.setFont("Helvetica", 8)
    c.setFillColor(COLOR_LIGHT_TEXT)
    c.drawCentredString(
        width / 2,
        15 * mm,
        "This report is generated automatically based on self-reported questionnaire responses.",
    )

    c.save()


def generate_reports_batch(respondents_data, output_dir):
    """
    Generate PDF reports for a batch of respondents.

    Args:
        respondents_data: list of dicts, each with keys:
            - "name": respondent name
            - "scores": dict from calculate_all_scores()
            - "date": optional date string
        output_dir: directory to save PDF files

    Returns:
        list of generated file paths
    """
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []

    for data in respondents_data:
        name = data["name"]
        # Create a safe filename
        safe_name = "".join(c if c.isalnum() or c in " -_" else "" for c in name).strip()
        safe_name = safe_name.replace(" ", "_")
        filename = f"Report_{safe_name}.pdf"
        filepath = os.path.join(output_dir, filename)

        generate_pdf_report(
            name=name,
            scores=data["scores"],
            output_path=filepath,
            date_taken=data.get("date", ""),
        )
        generated_files.append(filepath)

    return generated_files
