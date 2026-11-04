
import json
import csv
from pathlib import Path


def generate_json_report(results, output_file="reports/evaluation_report.json"):
    """
    Generate a JSON report from batch evaluation results.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = {
        "total_tests": len(results),
        "passed": sum(
            1 for result in results
            if result.get("evaluation", {}).get("status") == "PASS"
        ),
        "failed": sum(
            1 for result in results
            if result.get("evaluation", {}).get("status") != "PASS"
        ),
        "results": results
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return report


def generate_csv_report(results, output_file="reports/evaluation_report.csv"):
    """
    Generate a CSV report for easy analysis.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "test_id",
        "prompt",
        "score",
        "status",
        "latency"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for result in results:
            evaluation = result.get("evaluation", {})

            writer.writerow({
                "test_id": result.get("test_id", "N/A"),
                "prompt": result.get("prompt", ""),
                "score": evaluation.get("score", 0),
                "status": evaluation.get("status", "FAIL"),
                "latency": result.get("latency", 0)
            })
