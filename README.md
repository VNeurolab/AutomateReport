# Automated Personality Assessment Report Generator

Automatically scores MBTI-like personality questionnaire responses and generates professional PDF reports and Excel summaries.

## What It Does

1. Reads questionnaire responses from a CSV file (exported from Google Forms)
2. Scores each respondent on 4 personality dimensions using percentage polarities
3. Generates an individual PDF report for each respondent
4. Generates an Excel summary spreadsheet with all respondents

## The 4 Personality Dimensions

| Dimension | Left Pole | Right Pole |
|-----------|-----------|------------|
| E-I | Extraversion | Introversion |
| S-N | Sensing | Intuition |
| T-F | Thinking | Feeling |
| J-P | Judging | Perceiving |

Each dimension produces a percentage polarity (e.g., **30% Introversion — 70% Extraversion**) and a descriptive interpretation based on the score.

## Setup

### 1. Install Python

If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/) (version 3.8 or newer).

### 2. Install Dependencies

Open a terminal/command prompt in this folder and run:

```
pip install -r requirements.txt
```

## How to Use

### Step 1: Set Up Your Google Form

Create a Google Form with these settings:

- **First question**: "Name" (Short answer, required)
- **Questions 2-25**: The 24 personality questions listed below, each as a **Linear Scale from 1 to 7**
  - 1 = Strongly Disagree
  - 7 = Strongly Agree

The 24 questions (in order):

1. I feel energized after spending time with a large group of people.
2. I prefer to spend my free time alone or with one close friend.
3. I enjoy being the center of attention in social situations.
4. I need quiet time to recharge after social interactions.
5. I find it easy to start conversations with strangers.
6. I tend to think carefully before speaking in group discussions.
7. I focus on concrete facts and details rather than abstract ideas.
8. I enjoy thinking about theoretical concepts and possibilities.
9. I trust information that comes from direct, hands-on experience.
10. I am drawn to finding patterns and connections between different ideas.
11. I prefer step-by-step instructions when learning something new.
12. I often think about what could be rather than what currently is.
13. I make decisions based on logic and objective analysis.
14. I consider how my decisions will affect other people's feelings.
15. I value fairness and consistency over personal circumstances.
16. I prioritize harmony and maintaining good relationships.
17. I prefer to give honest feedback even if it might upset someone.
18. I am sensitive to the emotional atmosphere in a room.
19. I like to have a clear plan before starting a project.
20. I prefer to keep my options open and adapt as I go.
21. I feel satisfied when I complete tasks ahead of schedule.
22. I enjoy spontaneity and dislike rigid schedules.
23. I prefer to make decisions quickly and move on.
24. I like to explore all possibilities before committing to a choice.

### Step 2: Export Responses as CSV

1. Open your Google Form responses in Google Sheets
2. Go to **File > Download > Comma Separated Values (.csv)**
3. Save the file somewhere on your computer

The CSV should have columns: `Timestamp, Name, Q1, Q2, ..., Q24`

### Step 3: Run the Tool

```
python main.py path/to/your/responses.csv
```

Or specify a custom output directory:

```
python main.py path/to/your/responses.csv my_reports
```

### Step 4: Find Your Reports

After running, you'll find:

- `output/pdf_reports/` — One PDF report per respondent
- `output/summary_results.xlsx` — Excel spreadsheet with all scores

## Testing with Sample Data

A sample CSV with 5 fictional respondents is included:

```
python main.py sample_data/sample_responses.csv
```

## Project Files

| File | Description |
|------|-------------|
| `main.py` | Main script — run this to generate reports |
| `questionnaire.py` | Defines the 24 questions and 4 dimensions |
| `scoring.py` | Calculates percentage polarity scores |
| `interpretations.py` | Descriptive wording for each score range |
| `report_generator.py` | Generates individual PDF reports |
| `excel_generator.py` | Generates the Excel summary spreadsheet |
| `requirements.txt` | Python package dependencies |
| `sample_data/` | Sample CSV for testing |
