import gradio as gr
import requests

def ask_ai(question):
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"message": question}
    )

    data = response.json()
    return data.get("reply", "No response")

demo = gr.Interface(
    fn=ask_ai,
    inputs="text",
    outputs="text",
    title="AI Tutor",
    description="Ask a question and the AI tutor will explain it."
)

demo.launch()