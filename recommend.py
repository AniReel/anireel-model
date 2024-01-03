import cohere
import os
import pinecone
import pandas as pd 
import numpy as np
from dotenv import dotenv_values

env_name = ".env"
config = dotenv_values(env_name)

co = cohere.Client(os.environ['cohere_api'])

index = pinecone.Index(config['pinecone_index'])

def embed_text(text):
    embeddings = co.embed(
        texts=[text],
        model='embed-english-v3.0',
        input_type='search_query'
    )

    return embeddings



def vector_search(desc):

    results = []

    embeddings = co.embed(
        texts=[desc],
        model='embed-english-v3.0',
        input_type='search_query'
    )

    res = index.query([embeddings.embeddings[0]], top_k=2, include_metadata=True)

    for match in res['matches']:
        if match['score'] < 0.8:
            continue 

        results.append(match['metadata']['text'])

    return results