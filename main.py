import os
from typing import  Optional

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks
from pydantic import HttpUrl

from scraper import get_content


app = FastAPI()

def remove_file(path: str) -> None:
    os.unlink(path)

@app.get("/")
def main(
        background_tasks: BackgroundTasks,
        url: HttpUrl,
        width: Optional[int] = Query(60, ge=10, le=100),
        image_url: Optional[bool] = Query(False),
         ):
    """
    ## Performing page parsing at the given URL.

    Query Parameters
    ----------
    * url: HttpUrl
      #### example: https://www.timberland.com/shop/mens-boots
    * width: Optional[int (10-100)] Width line (DEFAULT 60).
    * image_url: Optional[bool] Display image url (DEFAULT False).

    Returns
    -------
    .txtFile with extracted data.
    """

    path = get_content(url, width, image_url)
    background_tasks.add_task(remove_file, path)
    return FileResponse(path)