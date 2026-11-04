
import json
from pathlib import Path

from app.evaluator import evaluate_response


# Locate the dataset in the main EvalAI folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "test_dataset.json"


def load_test_dataset():
    """Load test cases from the JSON dataset."""

    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def run_batch_evaluation(responses):
    """
    Evaluate multiple responses without calling Gemini.

    responses: dictionary mapping test_id to a generated response.
    """

    test_cases = load_test_dataset()
    results = []

    for test_case in test_cases:
        test_id = test_case["test_id"]
        response = responses.get(test_id, "")

        evaluation = evaluate_response(response)

        results.append(
            {
                "test_id": test_id,
                "prompt": test_case["prompt"],
                "response": response,
                "evaluation": evaluation,
            }
        )

    return results
