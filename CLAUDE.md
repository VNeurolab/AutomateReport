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
Google Forms → Export CSV → Python script → PDF reports + Excel summary → Push to GitHub
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
| `sample_output/` | Demo PDFs + Excel pushed to repo so user can download from GitHub |

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
- [ ] **H. Overall Insights text** — either user-provided per type combo, or Claude pre-generates all combinations during development

They can provide these in any format: Excel, Word, PDF, PPT, or typed in chat.

## Deployment & Output Expectations

- **Expected batch size: ~127 respondents** per run
- **Output delivery: push generated PDFs to GitHub repo** for user to download (do NOT rely on showing PDFs in chat — user cannot see them visually)
- **PDF generation capacity:** 127 reports is well within limits, runs in under a minute
- **Report assets supported:** polarity bars, pie charts, bar charts, radar/spider charts, logos/images, tables, multi-page layouts, custom fonts (.ttf)
- **"Overall Insights" or AI-written sections:** pre-generate all possible texts during development and bake into the system — no AI runs at report generation time. Two approaches:
  - Option A: User provides wording for each type combination
  - Option B: Claude pre-writes all possible insight texts, user reviews/approves
- **Design iteration is the main effort** — once the template is finalized, generating N copies is trivial

## User Context

- The user is a complete beginner with no coding experience
- They do not know how to use GitHub, Python, or terminal commands
- All technical work should be done by Claude — the user just provides content and reviews output
- The user CANNOT see PDF previews in chat — always push PDFs to GitHub repo for download
- The current MBTI-like questionnaire is a demo — expect it to be fully replaced
- Output formats: PDF reports (individual) + Excel summary (batch)
- Input source: Google Forms → exported as CSV
- Processing: batch (~127 respondents at once)
