from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>Hello World!</h1>"