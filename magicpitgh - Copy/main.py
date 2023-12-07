# main.py
from fastapi import FastAPI
from app.main import app as main_app

app = FastAPI()

app.mount("/app", main_app)
