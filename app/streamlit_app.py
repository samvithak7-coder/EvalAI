import json
import streamlit as st
from app.evaluator import evaluate_response

st.set_page_config(
    page_title="EvalAI | AI Quality Evaluation",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 EvalAI")
st.caption("AI Response Quality Evaluation Dashboard")

st.markdown(
    """
    Evaluate AI-generated responses using configurable quality checks.
    Review scores, inspect individual checks, and export evaluation results.
    """
)

st.divider()

prompt = st.text_area(
    "Test prompt",
    placeholder="Enter the prompt given to the AI model...",
    height=100,
)

response = st.text_area(
    "AI response",
    placeholder="Paste the AI-generated response here...",
    height=220,
)

if st.button("Run Evaluation", type="primary", use_container_width=True):
    if not response.strip():
        st.warning("Please enter an AI response before evaluating.")
    else:
        evaluation = evaluate_response(response)

        report = {
            "prompt": prompt,
            "response": response,
            "evaluation": evaluation,
        }

        st.session_state["evalai_report"] = report

report = st.session_state.get("evalai_report")

if report:
    evaluation = report["evaluation"]

    st.divider()
    st.subheader("Evaluation Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Quality Score", f'{evaluation["score"]:.2f}%')
    col2.metric("Status", evaluation["status"])
    col3.metric(
        "Checks Passed",
        f'{sum(evaluation["checks"].values())}/{len(evaluation["checks"])}',
    )

    if evaluation["status"] == "PASS":
        st.success("All evaluation checks passed.")
    else:
        st.error("One or more evaluation checks failed.")

    st.subheader("Detailed Checks")

    for check_name, passed in evaluation["checks"].items():
        if passed:
            st.success(f"✓ {check_name.replace('_', ' ').title()}")
        else:
            st.error(f"✗ {check_name.replace('_', ' ').title()}")

    st.download_button(
        "Download Evaluation Report (JSON)",
        data=json.dumps(report, indent=2),
        file_name="evalai_report.json",
        mime="application/json",
        use_container_width=True,
    )

st.divider()
st.caption("EvalAI • AI Quality Engineering Project")
