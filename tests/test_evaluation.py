from app.evaluator import evaluate_response


def test_valid_response():

    result = evaluate_response(
        "Python is a programming language."
    )

    assert result["status"] == "PASS"
    assert result["score"] == 100


def test_empty_response():

    result = evaluate_response("")

    assert result["status"] == "FAIL"


def test_short_response():

    result = evaluate_response("Hi")

    assert result["status"] == "FAIL"


def test_error_response():

    result = evaluate_response(
        "Traceback: Something went wrong"
    )

    assert result["status"] == "FAIL"