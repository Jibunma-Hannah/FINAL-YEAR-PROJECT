import subprocess
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TinyLlama API via Ollama")

class Question(BaseModel):
    message: str

@app.post("/ask")
def ask_ai(question: Question):
    """
    Send the question to TinyLlama via Ollama CLI and return the response.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "TinyLlama", question.message],
            capture_output=True,
            text=True,
            check=True  # Raises CalledProcessError if Ollama fails
        )
        reply = result.stdout.strip()
        if not reply:
            reply = "TinyLlama returned an empty response."
        return {"reply": reply}
    except subprocess.CalledProcessError as e:
        return {"error": f"Ollama failed: {e}"}