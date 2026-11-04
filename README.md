# EvalAI — AI Response Quality Evaluation

EvalAI is a Streamlit-based dashboard that evaluates AI-generated responses using automated quality checks. It helps assess response quality through scoring, pass/fail results, and detailed check summaries.

## Features
- Evaluate AI responses using quality checks
- Calculate quality scores
- Display PASS/FAIL status
- View detailed evaluation results
- Generate JSON and CSV reports
- Run automated tests with Pytest

## Tech Stack
Python · Streamlit · FastAPI · Pytest · JSON · GitHub

## Run Locally

```bash
git clone https://github.com/samvithak7-coder/EvalAI.git
cd EvalAI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app/streamlit_app.py
```

## Project Structure

```text
EvalAI/
├── app/
├── tests/
├── reports/
├── test_dataset.json
├── requirements.txt
└── README.md
```

## Project Goal
To demonstrate practical AI Quality Engineering through automated response evaluation, validation, scoring, and reporting.

**GitHub:** https://github.com/samvithak7-coder/EvalAI
