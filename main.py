"""
Main script — Automated Personality Questionnaire Scoring & Report Generation.

Usage:
    python main.py <input_csv_path> [output_directory]

This script:
  1. Reads questionnaire responses from a CSV file (exported from Google Forms)
  2. Scores each respondent on 4 MBTI-like dimensions
  3. Generates individual PDF reports for each respondent
  4. Generates an Excel summary of all respondents

The CSV file should have:
  - Column 1: "Timestamp" (from Google Forms)
  - Column 2: "Name" (respondent's name)
  - Columns 3-26: The 24 questionnaire items (Likert 1-7 responses)
"""

import sys
import os
import pandas as pd

from questionnaire import QUESTIONS
from scoring import calculate_all_scores, get_personality_type
from interpretations import get_all_interpretations
from report_generator import generate_reports_batch
from excel_generator import generate_excel_summary


def parse_csv(csv_path):
    """
    Parse a Google Forms CSV export into respondent data.

    Expected CSV format:
      Timestamp, Name, Q1_response, Q2_response, ..., Q24_response

    The question columns can be:
      - The full question text (as Google Forms exports it), OR
      - Generic column names (they'll be matched by position)

    Returns:
        list of dicts with keys: name, date, responses (dict of question_id → score)
    """
    df = pd.read_csv(csv_path)

    if len(df.columns) < 26:
        print(f"WARNING: Expected at least 26 columns, found {len(df.columns)}.")
        print("  Expected: Timestamp, Name, then 24 question responses.")
        print(f"  Your columns: {list(df.columns)}")

    respondents = []

    for _, row in df.iterrows():
        # First column = Timestamp/Date, second = Name
        date_val = str(row.iloc[0]) if pd.notna(row.iloc[0]) else ""
        name = str(row.iloc[1]) if pd.notna(row.iloc[1]) else "Unknown"

        # Columns 3 onwards = question responses (matched by position)
        responses = {}
        for i, q in enumerate(QUESTIONS):
            col_idx = i + 2  # offset by Timestamp and Name columns
            if col_idx < len(row):
                try:
                    score = int(float(row.iloc[col_idx]))
                    if 1 <= score <= 7:
                        responses[q["id"]] = score
                    else:
                        print(f"  WARNING: {name}, Q{q['id']}: score {score} out of range (1-7), skipping.")
                except (ValueError, TypeError):
                    print(f"  WARNING: {name}, Q{q['id']}: invalid value '{row.iloc[col_idx]}', skipping.")

        respondents.append({
            "name": name,
            "date": date_val,
            "responses": responses,
        })

    return respondents


def process_respondents(respondents):
    """
    Score all respondents and prepare data for report generation.

    Args:
        respondents: list from parse_csv()

    Returns:
        list of dicts with keys: name, date, scores, personality_type, interpretations
    """
    processed = []

    for resp in respondents:
        scores = calculate_all_scores(resp["responses"])
        personality_type = get_personality_type(scores)
        interpretations = get_all_interpretations(scores)

        processed.append({
            "name": resp["name"],
            "date": resp["date"],
            "scores": scores,
            "personality_type": personality_type,
            "interpretations": interpretations,
        })

    return processed


def main():
    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("=" * 60)
        print("  Automated Personality Assessment Report Generator")
        print("=" * 60)
        print()
        print("Usage:")
        print("  python main.py <input_csv_path> [output_directory]")
        print()
        print("Arguments:")
        print("  input_csv_path    Path to the CSV file exported from Google Forms")
        print("  output_directory  (Optional) Where to save reports. Default: ./output")
        print()
        print("Example:")
        print("  python main.py responses.csv ./reports")
        print()
        print("The CSV should have columns: Timestamp, Name, then 24 Likert (1-7) responses.")
        sys.exit(1)

    csv_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"

    # Validate input
    if not os.path.exists(csv_path):
        print(f"ERROR: File not found: {csv_path}")
        sys.exit(1)

    print("=" * 60)
    print("  Automated Personality Assessment Report Generator")
    print("=" * 60)
    print()

    # Step 1: Read CSV
    print(f"[1/4] Reading responses from: {csv_path}")
    respondents = parse_csv(csv_path)
    print(f"      Found {len(respondents)} respondent(s).")
    print()

    # Step 2: Score
    print("[2/4] Scoring all respondents...")
    processed = process_respondents(respondents)
    for p in processed:
        print(f"      {p['name']} → {p['personality_type']}")
    print()

    # Step 3: Generate PDF reports
    print(f"[3/4] Generating individual PDF reports...")
    pdf_dir = os.path.join(output_dir, "pdf_reports")
    pdf_files = generate_reports_batch(processed, pdf_dir)
    for f in pdf_files:
        print(f"      Created: {f}")
    print()

    # Step 4: Generate Excel summary
    print("[4/4] Generating Excel summary...")
    excel_path = os.path.join(output_dir, "summary_results.xlsx")
    generate_excel_summary(processed, excel_path)
    print(f"      Created: {excel_path}")
    print()

    print("=" * 60)
    print(f"  DONE! All reports saved to: {output_dir}/")
    print(f"  - {len(pdf_files)} PDF report(s) in {pdf_dir}/")
    print(f"  - 1 Excel summary at {excel_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
