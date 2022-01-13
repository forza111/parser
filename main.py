import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks
from pydantic import HttpUrl
import uvicorn

from scraper import get_content


app = FastAPI()

def remove_file(path: str) -> None:
    os.unlink(path)

@app.get("/")
def main(url: HttpUrl, width: int, image_url: bool, background_tasks: BackgroundTasks):
    path = get_content(url, width, image_url)
    background_tasks.add_task(remove_file, path)
    return FileResponse(path)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)