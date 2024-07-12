from fastapi import FastAPI, Body, Query
from datetime import datetime
from pydantic import BaseModel
from utils import Utils

app = FastAPI()

class DateInput(BaseModel):
    date: datetime = datetime.now()

class DateRangeInput(BaseModel):
    date1: datetime
    date2: datetime

class StringDateInput(BaseModel):
    date_string: str
    date_format: str = "%Y-%m-%d"

@app.get("/generate_current_datetime")
def generate_current_datetime():
    return {"current_datetime": Utils.generate_current_datetime()}

@app.post("/days_between_dates")
def days_between_dates(input: DateRangeInput):
    days = Utils.days_between_dates(input.date1, input.date2)
    return {"days_between": days}

@app.post("/string_to_datetime")
def string_to_datetime(input: StringDateInput):
    result_date = Utils.string_to_datetime(input.date_string, input.date_format)
    return {"result_date": result_date}

@app.get("/first_day_of_month")
def get_first_day_of_month(date: datetime = Query(..., description="The date to find the first day of its month")):
    result_date = Utils.get_first_day_of_month(date)
    return {"first_day_of_month": result_date.isoformat()}

@app.get("/last_day_of_month")
def get_last_day_of_month(date: datetime = Query(..., description="The date to find the last day of its month")):
    result_date = Utils.get_last_day_of_month(date)
    return {"last_day_of_month": result_date.isoformat()}
