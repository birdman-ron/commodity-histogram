from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

import config
import service.histogram
from logger import get_logger

_logger = get_logger()
_logger.info("Starting: " + config.SERVICE_NAME)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {"service": config.SERVICE_NAME}


def check_if_column_exist_or_404(column_name: str):
    if column_name not in service.histogram.available_column_names_for_route():
        raise HTTPException(status_code=404, detail="Column Not found")


@app.get("/{column_name}/histogram", response_class=HTMLResponse)
def histogram(request: Request, column_name: str):
    check_if_column_exist_or_404(column_name)
    aggregate_count_result = service.histogram.field_count_aggregate(column_name)

    values = {"request": request, "column_name": column_name, "aggregate_count_result": aggregate_count_result}
    return templates.TemplateResponse("aggregate_count.html", values)
