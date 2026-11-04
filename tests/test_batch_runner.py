
from app.batch_runner import run_batch_evaluation


def test_batch_runner_returns_all_results():
    responses = {
        "TC001": "Artificial intelligence is technology that helps computers learn patterns and solve problems.",
        "TC002": "The answer is 4.",
        "TC003": "Python loops repeat a block of code. For example, a for loop can iterate over a list.",
        "TC004": "AI is the broader field. Machine learning is a subset of AI that learns patterns from data.",
        "TC005": "Paris is the capital of France.",
    }

    results = run_batch_evaluation(responses)

    assert len(results) == 5


def test_batch_runner_handles_missing_response():
    responses = {
        "TC001": "Artificial intelligence helps computers solve problems."
    }

    results = run_batch_evaluation(responses)

    assert len(results) == 5
    assert results[1]["response"] == ""
    assert results[1]["evaluation"]["status"] == "FAIL"
