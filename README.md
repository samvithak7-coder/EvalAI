# EvalAI — AI Response Quality Evaluation

EvalAI is a Streamlit dashboard that evaluates AI-generated responses with configurable, automated quality checks. Paste a response, or generate one from a prompt with the Gemini API, and get a quality score, a PASS/FAIL verdict and a per-check breakdown. Results can be exported as JSON and CSV reports.

**Live demo:** https://evalai-f94vrqs6ajgiu6ibp4cdzd.streamlit.app/

## Why This Project

AI output can fail silently: empty answers, error messages returned as answers, or replies too short to be useful. EvalAI treats AI output like any other software output, and checks it automatically before it's trusted.

## Features

- Rule-based quality checks on AI responses
- Quality score with a PASS/FAIL status
- Per-check results, so you can see exactly why a response failed
- Gemini API integration to generate a response for a prompt and evaluate it
- Batch evaluation over a test dataset (`test_dataset.json`)
- JSON and CSV report generation
- Automated tests with Pytest

## Quality Checks

| Check | What it verifies |
|-------|------------------|
| Non-empty | The response contains actual content |
| Minimum length | The response meets a minimum length |
| Error-message detection | The "answer" is not an error or failure message |

Checks are configurable, so new rules can be added without changing the dashboard.

## Tech Stack

Python · Streamlit · Gemini API · Pytest · JSON/CSV · Git/GitHub

## How It Works

1. Enter a response, or give a prompt and generate one through the Gemini service module.
2. The evaluator runs every enabled check and computes a quality score.
3. The dashboard shows the score, the PASS/FAIL status and the result of each check.
4. The report generator exports the results as JSON and CSV.
5. The batch runner repeats this over a whole test dataset.

## Run Locally

```bash
git clone https://github.com/samvithak7-coder/EvalAI.git
cd EvalAI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app/streamlit_app.py
```

To use the Gemini integration, set your API key as an environment variable (never commit it):

```bash
export GEMINI_API_KEY="your-key-here"
```

## Run Tests

```bash
pytest tests/
```

## Project Structure

```text
EvalAI/
├── app/                 # Streamlit app, evaluator, Gemini service, report generator
├── tests/               # Pytest test cases
├── reports/             # Generated JSON/CSV reports
├── test_dataset.json    # Sample dataset for batch evaluation
├── requirements.txt
└── README.md
```

## Limitations

The current checks are simple rule-based heuristics. They catch obvious failures but cannot judge factual accuracy or relevance.

## Future Improvements

- LLM-as-judge scoring for relevance and correctness
- A labeled test set with measured agreement against human ratings
- More checks: format validation, toxicity and hallucination signals

## Author

**Samvitha K**
[GitHub](https://github.com/samvithak7-coder) · [LinkedIn](https://www.linkedin.com/in/kesapragada-samvitha-977714376/)
