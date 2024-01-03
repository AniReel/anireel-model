from fastapi import FastAPI
from recommend import vector_search
from pydantic import BaseModel
import requests 
import pandas as pd

df = pd.read_csv('mini_data.csv')


class validation(BaseModel):
    title: str 


app = FastAPI()


@app.post('/recommend')
def get_recommendations(items: validation):
    anime = df[df['title'] == items.title]

    if len(anime) == 0:
        return None 
    
    desc = anime['description']

    completion = vector_search(desc)

    return completion