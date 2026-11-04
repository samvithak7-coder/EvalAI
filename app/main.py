from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.gemini_service import generate_response
from app.evaluator import evaluate_response


app = FastAPI(
    title="EvalAI",
    description="AI Quality Assurance Framework",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    prompt: str


@app.get("/")
def home():

    return {
        "message": "Welcome to EvalAI",
        "status": "running"
    }



@app.post("/evaluate")
def evaluate(request: QueryRequest):

    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Prompt cannot be empty"
        )

    try:
        result = generate_response(request.prompt)

        evaluation = evaluate_response(
            result["answer"]
        )

        return {
            "prompt": request.prompt,
            "answer": result["answer"],
            "latency": result["latency"],
            "evaluation": evaluation
        }

    except Exception as error:
        print("Gemini Error:", repr(error))

        raise HTTPException(
            status_code=502,
            detail=str(error)
        )
