from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel
import os

app = FastAPI()


@app.get("/")
def read_root():
    return 'another one'


@app.get("/predict/{title}")
def read_item(title: str):
    model_file = f'{os.getcwd()}/persisted_models/2020-05-18T12:00:35Z_Layoffs-Pipeline'
    does_file_exist = os.path.isfile(model_file)
    assert does_file_exist
    model = load(model_file)
    pred = model.predict(['title'])[0]
    prob = model.predict_proba(['title'])[0].tolist()
    return {'title': title, 'pred': pred, 'prob': prob}
