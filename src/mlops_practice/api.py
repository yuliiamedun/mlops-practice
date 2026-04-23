from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mlops_practice.calculator import add, divide, multiply

app = FastAPI(
    title="mlops-practice API",
    description="A practice API for learning MLOps",
    version="0.1.0",
)


class CalculatorRequest(BaseModel):
    a: float
    b: float


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Welcome to mlops-practice API!"}


@app.post("/add")
def add_numbers(request: CalculatorRequest):
    """Add two numbers."""
    result = add(request.a, request.b)
    return {"result": result}


@app.post("/divide")
def divide_numbers(request: CalculatorRequest):
    """Divide two numbers."""
    try:
        result = divide(request.a, request.b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """Multiply two numbers."""
    result = multiply(a, b)
    return {"result": result}
