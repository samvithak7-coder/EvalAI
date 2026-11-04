
from app.report_generator import generate_json_report


sample_results = [
    {
        "test_id": "TC001",
        "prompt": "Explain artificial intelligence",
        "answer": "AI enables computers to perform tasks that typically require human intelligence.",
        "latency": 1.2,
        "evaluation": {
            "score": 100,
            "status": "PASS"
        }
    },
    {
        "test_id": "TC002",
        "prompt": "What is 2 + 2?",
        "answer": "The answer is 4.",
        "latency": 0.8,
        "evaluation": {
            "score": 100,
            "status": "PASS"
        }
    },
    {
        "test_id": "TC003",
        "prompt": "Explain Python loops",
        "answer": "Hi",
        "latency": 0.5,
        "evaluation": {
            "score": 33.33,
            "status": "FAIL"
        }
    }
]


generate_json_report(sample_results)

print("Sample evaluation report created!")
