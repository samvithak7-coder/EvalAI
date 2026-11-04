
import json
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent

REPORT_PATH = PROJECT_ROOT / "reports" / "evaluation_report.json"


st.set_page_config(
    page_title="EvalAI Dashboard",
    page_icon="🧪",
    layout="wide"
)


st.title("🧪 EvalAI")
st.subheader("AI Quality Engineering Dashboard")

st.write(
    "Monitor AI response quality, test results, and evaluation scores."
)


def load_report():
    """Load the latest evaluation report."""

    if not REPORT_PATH.exists():
        return None

    with open(REPORT_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


report = load_report()


if report is None:

    st.warning(
        "No evaluation report found yet. "
        "Generate a report using the batch runner first."
    )

    st.code(
        "reports/evaluation_report.json",
        language="text"
    )

    st.stop()


total_tests = report["total_tests"]
passed_tests = report["passed"]
failed_tests = report["failed"]


if total_tests > 0:
    pass_rate = (passed_tests / total_tests) * 100
else:
    pass_rate = 0


# Dashboard metrics

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Tests",
    total_tests
)

col2.metric(
    "Passed",
    passed_tests
)

col3.metric(
    "Failed",
    failed_tests
)

col4.metric(
    "Pass Rate",
    f"{pass_rate:.1f}%"
)


st.divider()


# Detailed test results

st.subheader("Test Results")


results = report.get("results", [])


table_data = []


for result in results:

    evaluation = result.get("evaluation", {})

    table_data.append(
        {
            "Test ID": result.get("test_id", "N/A"),
            "Prompt": result.get("prompt", ""),
            "Score": evaluation.get("score", 0),
            "Status": evaluation.get("status", "FAIL"),
            "Latency (seconds)": result.get("latency", 0)
        }
    )


if table_data:

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )


    st.subheader("Pass / Fail Distribution")


    chart_data = {
        "Status": ["Passed", "Failed"],
        "Count": [passed_tests, failed_tests]
    }


    st.bar_chart(
        chart_data,
        x="Status",
        y="Count"
    )


    st.subheader("Evaluation Scores")


    score_data = {
        "Test ID": [
            row["Test ID"]
            for row in table_data
        ],
        "Score": [
            row["Score"]
            for row in table_data
        ]
    }


    st.bar_chart(
        score_data,
        x="Test ID",
        y="Score"
    )


else:

    st.info("The evaluation report contains no test results.")
