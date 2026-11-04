def evaluate_response(answer: str) -> dict:

    checks = {
        "not_empty": bool(answer.strip()),
        "minimum_length": len(answer.strip()) >= 20,
        "no_error_message": "traceback" not in answer.lower()
    }

    passed = sum(checks.values())
    total = len(checks)

    score = round((passed / total) * 100, 2)

    return {
        "checks": checks,
        "score": score,
        "status": "PASS" if passed == total else "FAIL"
    }