
# PY-MICROSERVICE-POC

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=upa-io_py-microservice-poc&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=upa-io_py-microservice-poc) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=upa-io_py-microservice-poc&metric=coverage)](https://sonarcloud.io/summary/new_code?id=upa-io_py-microservice-poc) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=upa-io_py-microservice-poc&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=upa-io_py-microservice-poc)

Proyecto PoC de REST API con FastAPI en Python.
# Requirements

- Python 3.11
- FastAPI 0.111.0

# API Endpoints Documentation

This document provides an overview of the API endpoints available in the application. Each endpoint serves a specific function, as detailed below.

## Endpoints

### 1. Generate Current Datetime

- **Endpoint**: `/generate_current_datetime`
- **Method**: `GET`
- **Description**: Returns the current datetime.
- **Response**:
  - `current_datetime`: The current datetime in ISO format.

### 2. Days Between Dates

- **Endpoint**: `/days_between_dates`
- **Method**: `POST`
- **Description**: Calculates the number of days between two dates.
- **Request Body**:
  - `date1`: The start date in ISO format.
  - `date2`: The end date in ISO format.
- **Response**:
  - `days_between`: The number of days between `date1` and `date2`.

### 3. String to Datetime

- **Endpoint**: `/string_to_datetime`
- **Method**: `POST`
- **Description**: Converts a string representation of a date into a datetime object based on the provided format.
- **Request Body**:
  - `date_string`: The date string to convert.
  - `date_format`: The format of the date string (default is "%Y-%m-%d").
- **Response**:
  - `result_date`: The converted datetime in ISO format.
