import requests
import pathlib 
import pandas as pd 

id = 100
n = 10

url = f"https://api.jikan.moe/v4/anime/{id}/full"

print(url)

response = requests.get(url).json()

anime = []

for i in range(1, n):

    res_dict = {}

    res_dict['id'] = response['data']['mal_id']
    res_dict['url'] = response['data']['url']
    res_dict['trailer'] = response['data']['trailer']['url']
    res_dict['title'] = response['data']['title']
    res_dict['number_of_episodes'] = response['data']['episodes']
    res_dict['status'] = response['data']['status']
    res_dict['is_airing'] = response['data']['airing']
    res_dict['duration_per_episode'] = response['data']['duration']
    res_dict['rating'] = response['data']['rating']
    res_dict['score'] = response['data']['score']
    res_dict['rank'] = response['data']['rank']
    res_dict['popularity'] = response['data']['popularity']
    res_dict['description'] = response['data']['synopsis']
    res_dict[''] = response['data']['year']
    res_dict['genres'] = response['data']['genres']
    res_dict['themes'] = response['data']['themes']
    res_dict['streaming_sites'] = response['data']['streaming']

    anime.append(res_dict)

anime_df = pd.DataFrame(anime)

anime_df.to_csv('mini_data.csv') 

#res_dict['id'] = response[]