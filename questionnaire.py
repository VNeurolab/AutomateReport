"""
Questionnaire definition for MBTI-like personality assessment.

4 Dimensions (6 questions each = 24 total):
  1. Extraversion (E) vs Introversion (I)
  2. Sensing (S) vs Intuition (N)
  3. Thinking (T) vs Feeling (F)
  4. Judging (J) vs Perceiving (P)

Each question uses a 7-point Likert scale:
  1 = Strongly Disagree
  2 = Disagree
  3 = Slightly Disagree
  4 = Neutral
  5 = Slightly Agree
  6 = Agree
  7 = Strongly Agree

Scoring direction:
  "right" = high score (7) maps toward the RIGHT pole (e.g., Introversion)
  "left"  = high score (7) maps toward the LEFT pole (e.g., Extraversion)
  This ensures balanced measurement with some reverse-scored items.
"""

# Define the 4 dimensions with their pole labels
DIMENSIONS = [
    {
        "id": "EI",
        "left_pole": "Extraversion",
        "right_pole": "Introversion",
        "left_code": "E",
        "right_code": "I",
    },
    {
        "id": "SN",
        "left_pole": "Sensing",
        "right_pole": "Intuition",
        "left_code": "S",
        "right_code": "N",
    },
    {
        "id": "TF",
        "left_pole": "Thinking",
        "right_pole": "Feeling",
        "left_code": "T",
        "right_code": "F",
    },
    {
        "id": "JP",
        "left_pole": "Judging",
        "right_pole": "Perceiving",
        "left_code": "J",
        "right_code": "P",
    },
]

# All 24 questionnaire items
# "direction": "right" means agreeing (high score) = more toward RIGHT pole
# "direction": "left" means agreeing (high score) = more toward LEFT pole
QUESTIONS = [
    # --- Extraversion (E) vs Introversion (I) ---
    {
        "id": 1,
        "text": "I feel energized after spending time with a large group of people.",
        "dimension": "EI",
        "direction": "left",  # Agreeing = more Extraversion
    },
    {
        "id": 2,
        "text": "I prefer to spend my free time alone or with one close friend.",
        "dimension": "EI",
        "direction": "right",  # Agreeing = more Introversion
    },
    {
        "id": 3,
        "text": "I enjoy being the center of attention in social situations.",
        "dimension": "EI",
        "direction": "left",
    },
    {
        "id": 4,
        "text": "I need quiet time to recharge after social interactions.",
        "dimension": "EI",
        "direction": "right",
    },
    {
        "id": 5,
        "text": "I find it easy to start conversations with strangers.",
        "dimension": "EI",
        "direction": "left",
    },
    {
        "id": 6,
        "text": "I tend to think carefully before speaking in group discussions.",
        "dimension": "EI",
        "direction": "right",
    },
    # --- Sensing (S) vs Intuition (N) ---
    {
        "id": 7,
        "text": "I focus on concrete facts and details rather than abstract ideas.",
        "dimension": "SN",
        "direction": "left",  # Agreeing = more Sensing
    },
    {
        "id": 8,
        "text": "I enjoy thinking about theoretical concepts and possibilities.",
        "dimension": "SN",
        "direction": "right",  # Agreeing = more Intuition
    },
    {
        "id": 9,
        "text": "I trust information that comes from direct, hands-on experience.",
        "dimension": "SN",
        "direction": "left",
    },
    {
        "id": 10,
        "text": "I am drawn to finding patterns and connections between different ideas.",
        "dimension": "SN",
        "direction": "right",
    },
    {
        "id": 11,
        "text": "I prefer step-by-step instructions when learning something new.",
        "dimension": "SN",
        "direction": "left",
    },
    {
        "id": 12,
        "text": "I often think about what could be rather than what currently is.",
        "dimension": "SN",
        "direction": "right",
    },
    # --- Thinking (T) vs Feeling (F) ---
    {
        "id": 13,
        "text": "I make decisions based on logic and objective analysis.",
        "dimension": "TF",
        "direction": "left",  # Agreeing = more Thinking
    },
    {
        "id": 14,
        "text": "I consider how my decisions will affect other people's feelings.",
        "dimension": "TF",
        "direction": "right",  # Agreeing = more Feeling
    },
    {
        "id": 15,
        "text": "I value fairness and consistency over personal circumstances.",
        "dimension": "TF",
        "direction": "left",
    },
    {
        "id": 16,
        "text": "I prioritize harmony and maintaining good relationships.",
        "dimension": "TF",
        "direction": "right",
    },
    {
        "id": 17,
        "text": "I prefer to give honest feedback even if it might upset someone.",
        "dimension": "TF",
        "direction": "left",
    },
    {
        "id": 18,
        "text": "I am sensitive to the emotional atmosphere in a room.",
        "dimension": "TF",
        "direction": "right",
    },
    # --- Judging (J) vs Perceiving (P) ---
    {
        "id": 19,
        "text": "I like to have a clear plan before starting a project.",
        "dimension": "JP",
        "direction": "left",  # Agreeing = more Judging
    },
    {
        "id": 20,
        "text": "I prefer to keep my options open and adapt as I go.",
        "dimension": "JP",
        "direction": "right",  # Agreeing = more Perceiving
    },
    {
        "id": 21,
        "text": "I feel satisfied when I complete tasks ahead of schedule.",
        "dimension": "JP",
        "direction": "left",
    },
    {
        "id": 22,
        "text": "I enjoy spontaneity and dislike rigid schedules.",
        "dimension": "JP",
        "direction": "right",
    },
    {
        "id": 23,
        "text": "I prefer to make decisions quickly and move on.",
        "dimension": "JP",
        "direction": "left",
    },
    {
        "id": 24,
        "text": "I like to explore all possibilities before committing to a choice.",
        "dimension": "JP",
        "direction": "right",
    },
]


def get_dimension_by_id(dimension_id):
    """Get dimension config by its ID (e.g., 'EI')."""
    for dim in DIMENSIONS:
        if dim["id"] == dimension_id:
            return dim
    return None


def get_questions_for_dimension(dimension_id):
    """Get all questions belonging to a specific dimension."""
    return [q for q in QUESTIONS if q["dimension"] == dimension_id]


def get_google_forms_columns():
    """
    Return the expected column headers for a Google Forms CSV export.
    The first column is 'Timestamp', second is 'Name',
    then one column per question using the question text.
    """
    columns = ["Timestamp", "Name"]
    for q in QUESTIONS:
        columns.append(q["text"])
    return columns
