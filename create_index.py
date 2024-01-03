import pinecone
import cohere 
import os 
from dotenv import dotenv_values
import pandas as pd 
from tqdm.auto import tqdm
import time

env_name = ".env"
config = dotenv_values(env_name)


co = cohere.Client(config['cohere_api'])

response = co.embed(
  texts=["what is your name"],
  model='embed-english-v3.0',
  input_type='search_query'
).embeddings



df = pd.read_csv('mini_data.csv')

index_name = 'anireel'

pinecone.init(
    api_key=config['pinecone_api'],
    environment= config['pinecone_env']
)

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=len(response[0]))

index = pinecone.Index(index_name)

data = list(df['description']) 

count = 0  # we'll use the count to create unique IDs
batch_size = 1  
for i in tqdm(range(0, len(data), batch_size)):
    # set end position of batch
    i_end = min(i+batch_size, len(data))
    # get batch of lines and IDs
    lines_batch = data[i: i+batch_size]
    print('lines batch: ', lines_batch)
    ids_batch = [str(n) for n in range(i, i_end)]
    # create embeddings
    res = co.embed(texts=lines_batch,model="embed-english-v3.0", input_type='search_query')
    time.sleep(30)
    embeds = res.embeddings
    print('embeddings: ', embeds)
    # prep metadata and upsert batch
    meta = [{'text': line} for line in lines_batch]
    print('metdata: ', meta)
    #to_upsert = zip(ids_batch, embeds, meta)
    #print('add to index: ', list(to_upsert))
    # upsert to Pinecone

    index.upsert(vectors=list(zip(ids_batch, embeds, meta)))