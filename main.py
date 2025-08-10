from fastapi import FastAPI
app = FastAPI()
@app.get("/Question")

def Ask_Question():
    return {"Question": "What is the capital of Sudan?",
            "Answer":"Khartoum"
            }