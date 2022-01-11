from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from parser import get_content

app = FastAPI()

@app.get("/")
def main(url: str, width: int):
    path = get_content(url, width)
    return FileResponse(path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
