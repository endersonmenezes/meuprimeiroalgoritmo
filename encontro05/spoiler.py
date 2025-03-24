from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(title="Hello World API", version="1.0.0")

@app.get("/")
def read_root():
    """Return a hello world message"""
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    """Return API version and health status"""
    return {
        "version": app.version,
        "health": "ok"
    }

@app.get("/sum")
def sum_numbers(a: int, b: int):
    """
    Sum two numbers provided as GET parameters
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON with the result of a + b
    """
    result = a + b
    return {"result": result}

# To run this application:
# pip install fastapi uvicorn
# uvicorn spoiler:app --reload
# Access API docs at http://127.0.0.1:8000/docs