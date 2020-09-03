#FROM frolvlad/alpine-python-machinelearning:latest
#FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip
RUN pip install --upgrade joblib
RUN pip install --upgrade scikit-learn

COPY persisted_models/* ./persisted_models/

COPY ./app /app