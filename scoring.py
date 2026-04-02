"""
Scoring engine for the personality questionnaire.

For each dimension, calculates a percentage polarity:
  - 0% = fully LEFT pole (e.g., 100% Extraversion)
  - 100% = fully RIGHT pole (e.g., 100% Introversion)
  - 50% = balanced between both poles

The percentage is displayed as:
  "X% LeftPole — Y% RightPole" where X + Y = 100

Scoring logic:
  - For "right" direction items: raw score is used (1-7)
  - For "left" direction items: score is reversed (8 - raw_score)
  - Average of all normalized scores for a dimension → convert to 0-100%
"""

from questionnaire import QUESTIONS, DIMENSIONS, get_dimension_by_id


def reverse_score(score):
    """Reverse a 7-point Likert score: 1↔7, 2↔6, 3↔5, 4↔4."""
    return 8 - score


def calculate_dimension_score(responses, dimension_id):
    """
    Calculate the percentage score for one dimension.

    Args:
        responses: dict mapping question ID (int) to Likert score (1-7)
        dimension_id: e.g., "EI", "SN", "TF", "JP"

    Returns:
        float: percentage toward the RIGHT pole (0-100)
    """
    dimension_questions = [q for q in QUESTIONS if q["dimension"] == dimension_id]
    normalized_scores = []

    for q in dimension_questions:
        raw_score = responses.get(q["id"])
        if raw_score is None:
            continue

        # Normalize so that higher = more toward RIGHT pole
        if q["direction"] == "right":
            normalized = raw_score
        else:
            normalized = reverse_score(raw_score)

        normalized_scores.append(normalized)

    if not normalized_scores:
        return 50.0  # default to balanced if no data

    # Convert average (1-7 scale) to percentage (0-100)
    avg = sum(normalized_scores) / len(normalized_scores)
    percentage_right = ((avg - 1) / 6) * 100

    return round(percentage_right, 1)


def calculate_all_scores(responses):
    """
    Calculate scores for all 4 dimensions.

    Args:
        responses: dict mapping question ID (int) to Likert score (1-7)

    Returns:
        dict with structure:
        {
            "EI": {
                "left_pole": "Extraversion",
                "right_pole": "Introversion",
                "left_code": "E",
                "right_code": "I",
                "left_percent": 70.0,
                "right_percent": 30.0,
                "dominant_code": "E",
                "dominant_pole": "Extraversion",
            },
            ...
        }
    """
    results = {}

    for dim in DIMENSIONS:
        right_percent = calculate_dimension_score(responses, dim["id"])
        left_percent = round(100 - right_percent, 1)

        if left_percent >= right_percent:
            dominant_code = dim["left_code"]
            dominant_pole = dim["left_pole"]
        else:
            dominant_code = dim["right_code"]
            dominant_pole = dim["right_pole"]

        results[dim["id"]] = {
            "left_pole": dim["left_pole"],
            "right_pole": dim["right_pole"],
            "left_code": dim["left_code"],
            "right_code": dim["right_code"],
            "left_percent": left_percent,
            "right_percent": right_percent,
            "dominant_code": dominant_code,
            "dominant_pole": dominant_pole,
        }

    return results


def get_personality_type(scores):
    """
    Get the 4-letter personality type code (e.g., 'ENFP').

    Args:
        scores: dict returned by calculate_all_scores()

    Returns:
        str: 4-letter type code
    """
    return (
        scores["EI"]["dominant_code"]
        + scores["SN"]["dominant_code"]
        + scores["TF"]["dominant_code"]
        + scores["JP"]["dominant_code"]
    )
