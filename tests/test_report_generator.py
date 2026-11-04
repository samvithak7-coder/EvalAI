
import json

from app.report_generator import (
    generate_json_report,
    generate_csv_report
)


def sample_results():
    return [
        {
            "test_id": "TC001",
            "prompt": "Explain AI",
            "answer": "AI helps computers learn from data.",
            "latency": 1.2,
            "evaluation": {
                "score": 100,
                "status": "PASS"
            }
        },
        {
            "test_id": "TC002",
            "prompt": "Explain Python",
            "answer": "",
            "latency": 0.5,
            "evaluation": {
                "score": 0,
                "status": "FAIL"
            }
        }
    ]


def test_json_report(tmp_path):
    results = sample_results()

    output_file = tmp_path / "report.json"

    report = generate_json_report(
        results,
        str(output_file)
    )

    assert report["total_tests"] == 2
    assert report["passed"] == 1
    assert report["failed"] == 1

    assert output_file.exists()

    with open(output_file, encoding="utf-8") as file:
        saved_report = json.load(file)

    assert saved_report["total_tests"] == 2


def test_csv_report(tmp_path):
    results = sample_results()

    output_file = tmp_path / "report.csv"

    generate_csv_report(
        results,
        str(output_file)
    )

    assert output_file.exists()

    content = output_file.read_text(encoding="utf-8")

    assert "TC001" in content
    assert "TC002" in content
    assert "PASS" in content
    assert "FAIL" in content
