from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.histogram import field_count_aggregate
from fastapi import Depends

import config
from logger import get_logger


__logger = get_logger()
__logger.info("Starting: " + config.SERVICE_NAME)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    response = {"service": config.SERVICE_NAME}
    return response


@app.get("/test")
def test():
    response = {"ok": "something happened!"}
    return response
