import requests
import pathlib 

id = 100

url = f"https://api.jikan.moe/v4/anime/{id}/full"

print(url)

response = requests.get(url).json()

anime = []

res_dict = {}

print(response['data']['mal_id'])
print(response['data']['url'])
print(response['data']['trailer']['url'])
print(response['data']['title'])
print(response['data']['episodes'])
print(response['data']['status'])
print(response['data']['airing'])
print(response['data']['duration'])
print(response['data']['rating'])
print(response['data']['score'])
print(response['data']['rank'])
print(response['data']['popularity'])
print(response['data']['synopsis'])
print(response['data']['year'])
print(response['data']['genres'])
print(response['data']['themes'])
print(response['data']['streaming'])

#res_dict['id'] = response[]