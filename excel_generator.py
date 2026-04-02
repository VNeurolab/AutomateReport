"""
Excel summary generator.

Creates a summary spreadsheet with all respondents' scores,
personality types, and interpretation labels in one file.
"""

import os
import pandas as pd
from questionnaire import DIMENSIONS


def generate_excel_summary(respondents_data, output_path):
    """
    Generate an Excel summary of all respondents.

    Args:
        respondents_data: list of dicts, each with keys:
            - "name": respondent name
            - "scores": dict from calculate_all_scores()
            - "personality_type": 4-letter code
            - "interpretations": dict from get_all_interpretations()
            - "date": optional date string
        output_path: file path for the Excel output

    Returns:
        str: the output file path
    """
    rows = []

    for data in respondents_data:
        row = {
            "Name": data["name"],
            "Date": data.get("date", ""),
            "Personality Type": data["personality_type"],
        }

        for dim in DIMENSIONS:
            dim_id = dim["id"]
            dim_scores = data["scores"][dim_id]
            interp = data["interpretations"][dim_id]

            left = dim_scores["left_pole"]
            right = dim_scores["right_pole"]

            row[f"{left} %"] = dim_scores["left_percent"]
            row[f"{right} %"] = dim_scores["right_percent"]
            row[f"{left}-{right} Interpretation"] = interp["label"]

        rows.append(row)

    df = pd.DataFrame(rows)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    df.to_excel(output_path, index=False, sheet_name="Results")

    return output_path
