"""
Interpretation wording based on polarity scores.

Each dimension has 5 score ranges, each with a descriptive paragraph
that explains the respondent's tendency on that dimension.

Score ranges (based on the RIGHT pole percentage):
  0-20%    → Strong LEFT pole
  >20-40%  → Moderate LEFT pole
  >40-60%  → Balanced / Slight preference
  >60-80%  → Moderate RIGHT pole
  >80-100% → Strong RIGHT pole
"""

INTERPRETATIONS = {
    "EI": {
        "ranges": [
            {
                "min": 0,
                "max": 20,
                "label": "Strong Extraversion",
                "description": (
                    "You are strongly extraverted. You thrive in social environments "
                    "and feel energized by interacting with others. You are likely outgoing, "
                    "talkative, and enthusiastic in group settings. You prefer to think out loud "
                    "and enjoy being at the center of activity. You may find prolonged solitude "
                    "draining and seek out social stimulation naturally."
                ),
            },
            {
                "min": 21,
                "max": 40,
                "label": "Moderate Extraversion",
                "description": (
                    "You lean toward extraversion. You generally enjoy social interactions "
                    "and feel comfortable in group settings, though you also appreciate some "
                    "quiet time. You tend to be sociable and approachable, and you often prefer "
                    "to process ideas by discussing them with others. You strike a good balance "
                    "but tend to seek out people and activity when given the choice."
                ),
            },
            {
                "min": 41,
                "max": 60,
                "label": "Balanced Extraversion-Introversion",
                "description": (
                    "You show a balanced mix of extraversion and introversion. You can adapt "
                    "comfortably to both social and solitary situations. Sometimes you enjoy "
                    "being around people and drawing energy from the group, while other times "
                    "you prefer quiet reflection. This flexibility allows you to navigate "
                    "different social contexts with ease."
                ),
            },
            {
                "min": 61,
                "max": 80,
                "label": "Moderate Introversion",
                "description": (
                    "You lean toward introversion. You prefer meaningful one-on-one "
                    "conversations over large group interactions. While you can function "
                    "well in social settings, you need regular alone time to recharge. "
                    "You tend to think before you speak and prefer to observe before "
                    "participating. You value depth over breadth in your relationships."
                ),
            },
            {
                "min": 81,
                "max": 100,
                "label": "Strong Introversion",
                "description": (
                    "You are strongly introverted. You draw your energy from solitude and "
                    "internal reflection. You prefer quiet, low-stimulation environments and "
                    "deep conversations with a few close people rather than large social "
                    "gatherings. You are likely thoughtful, reflective, and independent. "
                    "Extended social interaction can feel exhausting, and you need significant "
                    "alone time to feel your best."
                ),
            },
        ],
    },
    "SN": {
        "ranges": [
            {
                "min": 0,
                "max": 20,
                "label": "Strong Sensing",
                "description": (
                    "You are strongly oriented toward sensing. You focus on concrete, "
                    "tangible information and trust what you can see, hear, and touch. "
                    "You are practical, detail-oriented, and grounded in the present moment. "
                    "You prefer proven methods and step-by-step approaches. You excel at "
                    "working with facts and real-world data rather than abstract theories."
                ),
            },
            {
                "min": 21,
                "max": 40,
                "label": "Moderate Sensing",
                "description": (
                    "You lean toward sensing. You generally prefer dealing with concrete "
                    "information and practical matters, though you can appreciate the "
                    "occasional abstract idea. You tend to be realistic and observant, "
                    "noticing details that others might miss. You value experience and "
                    "prefer to learn by doing rather than theorizing."
                ),
            },
            {
                "min": 41,
                "max": 60,
                "label": "Balanced Sensing-Intuition",
                "description": (
                    "You show a balanced mix of sensing and intuition. You can work "
                    "comfortably with both concrete details and abstract concepts. "
                    "You appreciate practical, hands-on experience but also enjoy "
                    "exploring possibilities and big-picture thinking. This balance "
                    "allows you to be both grounded and creative depending on the situation."
                ),
            },
            {
                "min": 61,
                "max": 80,
                "label": "Moderate Intuition",
                "description": (
                    "You lean toward intuition. You enjoy exploring ideas, patterns, and "
                    "possibilities beyond the immediate facts. You tend to look at the big "
                    "picture and think about future potential rather than focusing solely on "
                    "present realities. You are imaginative and enjoy connecting seemingly "
                    "unrelated concepts, though you can still attend to details when needed."
                ),
            },
            {
                "min": 81,
                "max": 100,
                "label": "Strong Intuition",
                "description": (
                    "You are strongly oriented toward intuition. You are drawn to abstract "
                    "ideas, theories, and future possibilities. You see patterns and "
                    "connections that others might overlook and enjoy exploring innovative "
                    "concepts. You may find routine, detail-heavy tasks tedious and prefer "
                    "to focus on the big picture and what could be rather than what is."
                ),
            },
        ],
    },
    "TF": {
        "ranges": [
            {
                "min": 0,
                "max": 20,
                "label": "Strong Thinking",
                "description": (
                    "You are strongly oriented toward thinking. You make decisions based on "
                    "logic, objectivity, and rational analysis. You value truth and fairness "
                    "applied consistently, even when it may be uncomfortable. You are "
                    "analytical and strategic, and you tend to evaluate situations "
                    "impersonally. You may sometimes be perceived as blunt, but your "
                    "strength lies in clear, principled reasoning."
                ),
            },
            {
                "min": 21,
                "max": 40,
                "label": "Moderate Thinking",
                "description": (
                    "You lean toward thinking in your decision-making. You generally prefer "
                    "logical analysis and objective criteria, though you also consider people's "
                    "feelings when important. You tend to be fair-minded and consistent, "
                    "and you value competence and accuracy. You can be empathetic but "
                    "ultimately rely on reason when making tough choices."
                ),
            },
            {
                "min": 41,
                "max": 60,
                "label": "Balanced Thinking-Feeling",
                "description": (
                    "You show a balanced approach between thinking and feeling. You can "
                    "apply logical analysis when needed and also tune into the emotional "
                    "needs of others. You consider both objective criteria and personal "
                    "values when making decisions. This balance makes you adaptable in "
                    "both analytical and interpersonal contexts."
                ),
            },
            {
                "min": 61,
                "max": 80,
                "label": "Moderate Feeling",
                "description": (
                    "You lean toward feeling in your decision-making. You give significant "
                    "weight to personal values, empathy, and how decisions affect people. "
                    "You are warm, compassionate, and attentive to others' emotional needs. "
                    "While you can think logically, you ultimately prioritize harmony "
                    "and human connection when making important choices."
                ),
            },
            {
                "min": 81,
                "max": 100,
                "label": "Strong Feeling",
                "description": (
                    "You are strongly oriented toward feeling. Your decisions are deeply "
                    "guided by personal values, empathy, and concern for others' well-being. "
                    "You are highly attuned to the emotional atmosphere around you and "
                    "prioritize maintaining harmony and positive relationships. You may "
                    "find purely impersonal, logical decisions difficult, as you naturally "
                    "consider the human impact of every choice."
                ),
            },
        ],
    },
    "JP": {
        "ranges": [
            {
                "min": 0,
                "max": 20,
                "label": "Strong Judging",
                "description": (
                    "You are strongly oriented toward judging. You prefer structure, "
                    "organization, and clear plans. You like to make decisions promptly "
                    "and feel satisfied when tasks are completed and things are settled. "
                    "You are disciplined, orderly, and prefer predictability. "
                    "You may feel uncomfortable with ambiguity and last-minute changes."
                ),
            },
            {
                "min": 21,
                "max": 40,
                "label": "Moderate Judging",
                "description": (
                    "You lean toward judging. You generally prefer having a plan and "
                    "working in an organized manner, though you can be flexible when "
                    "needed. You like to set goals and meet deadlines, and you feel "
                    "more comfortable when things are decided rather than left open-ended. "
                    "You appreciate structure but can adapt when circumstances change."
                ),
            },
            {
                "min": 41,
                "max": 60,
                "label": "Balanced Judging-Perceiving",
                "description": (
                    "You show a balanced mix of judging and perceiving tendencies. You "
                    "can work within structured plans but also enjoy flexibility and "
                    "spontaneity. Sometimes you prefer to have things decided and organized, "
                    "while other times you enjoy keeping your options open. This adaptability "
                    "helps you navigate both planned and unpredictable situations."
                ),
            },
            {
                "min": 61,
                "max": 80,
                "label": "Moderate Perceiving",
                "description": (
                    "You lean toward perceiving. You prefer to keep your options open "
                    "and enjoy a flexible, adaptable approach to life. You tend to be "
                    "curious and open-minded, exploring possibilities before committing. "
                    "While you can follow plans when necessary, you prefer spontaneity "
                    "and may find rigid schedules constraining."
                ),
            },
            {
                "min": 81,
                "max": 100,
                "label": "Strong Perceiving",
                "description": (
                    "You are strongly oriented toward perceiving. You thrive on "
                    "spontaneity, flexibility, and keeping your options open. You are "
                    "curious, adaptable, and enjoy exploring new possibilities. You may "
                    "resist rigid schedules and deadlines, preferring to go with the flow. "
                    "You are energized by new experiences and may start many projects, "
                    "enjoying the process of exploration more than reaching a final conclusion."
                ),
            },
        ],
    },
}


def get_interpretation(dimension_id, right_percent):
    """
    Get the interpretation text for a dimension based on the right-pole percentage.

    Args:
        dimension_id: e.g., "EI", "SN", "TF", "JP"
        right_percent: float 0-100 (percentage toward the right pole)

    Returns:
        dict with "label" and "description"
    """
    dim_interp = INTERPRETATIONS.get(dimension_id)
    if not dim_interp:
        return {"label": "Unknown", "description": "No interpretation available."}

    # Use threshold-based matching to avoid gaps with decimal scores
    thresholds = [20, 40, 60, 80, 100]
    for i, threshold in enumerate(thresholds):
        if right_percent <= threshold:
            r = dim_interp["ranges"][i]
            return {"label": r["label"], "description": r["description"]}

    # Fallback (should not happen)
    r = dim_interp["ranges"][-1]
    return {"label": r["label"], "description": r["description"]}


def get_all_interpretations(scores):
    """
    Get interpretations for all dimensions.

    Args:
        scores: dict returned by scoring.calculate_all_scores()

    Returns:
        dict mapping dimension_id to interpretation dict
    """
    result = {}
    for dim_id, dim_scores in scores.items():
        interp = get_interpretation(dim_id, dim_scores["right_percent"])
        result[dim_id] = interp
    return result
