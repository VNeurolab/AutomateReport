# AutomateReport — Project Memory

## What This Project Is

An automated personality questionnaire scoring and report generation pipeline.
It reads questionnaire responses (CSV from Google Forms), scores them, and generates
individual PDF reports + an Excel summary spreadsheet.

## Current State

The system is fully functional with a **demo/placeholder** questionnaire (MBTI-like).
The user has NOT provided their actual content yet. Everything below marked with
"[PLACEHOLDER]" needs to be replaced with real content when the user provides it.

## Architecture

```
Google Forms → Export CSV → Python script → PDF reports + Excel summary
```

### Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point. Reads CSV, orchestrates scoring and report generation |
| `questionnaire.py` | [PLACEHOLDER] Defines questions, dimensions, and scoring directions |
| `scoring.py` | Calculates percentage polarity scores per dimension (0-100%) |
| `interpretations.py` | [PLACEHOLDER] Descriptive wording for 5 score ranges per dimension |
| `report_generator.py` | Generates individual PDF reports using reportlab |
| `excel_generator.py` | Generates Excel summary spreadsheet using pandas + openpyxl |
| `requirements.txt` | Python dependencies: pandas, openpyxl, reportlab |
| `sample_data/sample_responses.csv` | Sample CSV for testing |

### How It Works

1. CSV format: `Timestamp, Name, Q1_response, Q2_response, ..., QN_response`
2. Each question maps to a dimension (polarity pair) with a scoring direction
3. 7-point Likert scale (1=Strongly Disagree, 7=Strongly Agree)
4. Scores are normalized to 0-100% per dimension (e.g., 30% Introvert — 70% Extrovert)
5. Descriptive wording is retrieved based on 5 score ranges (0-20, 21-40, 41-60, 61-80, 81-100)
6. PDF report shows: name, date, personality type code, visual polarity bars, percentages, descriptions
7. Excel summary shows: all respondents with scores and interpretation labels

### Running It

```bash
pip install -r requirements.txt
python main.py <input_csv> [output_directory]
```

Output goes to `output/pdf_reports/` (individual PDFs) and `output/summary_results.xlsx`.

## What the User Needs to Provide (Checklist)

When the user is ready to customize, they need to provide:

- [ ] **A. Dimensions/polarities** — what pairs are being measured (e.g., "Analytical vs Creative")
- [ ] **B. Questionnaire items** — the actual question statements, which dimension each belongs to, and scoring direction
- [ ] **C. Likert scale confirmation** — currently 7-point, confirm or change
- [ ] **D. Scoring rules** — any special formula (current: simple average → percentage)
- [ ] **E. Descriptive wording** — paragraphs for each score range per dimension (5 ranges x N dimensions)
- [ ] **F. Report design** — colors, logo, layout preferences, or a PPT/PDF template to match
- [ ] **G. Response data** — actual CSV exported from Google Forms

They can provide these in any format: Excel, Word, PDF, PPT, or typed in chat.

## User Context

- The user is a complete beginner with no coding experience
- They do not know how to use GitHub, Python, or terminal commands
- All technical work should be done by Claude — the user just provides content and reviews output
- The user can see PDF previews directly in the Claude Code chat
- The current MBTI-like questionnaire is a demo — expect it to be fully replaced
- Output formats: PDF reports (individual) + Excel summary (batch)
- Input source: Google Forms → exported as CSV
- Processing: batch (many respondents at once)
