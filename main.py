import requests

from pprint import pprint

files_url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(files_url)

hero_comparison_dict = {}
for hero in response.json():
    if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
        hero_comparison_dict[hero['name']] = hero['powerstats']['intelligence']
for hero_1 in hero_comparison_dict.items():
    if  sorted(hero_comparison_dict.values())[-1] == hero_1[1]:
        print(hero_1[0], '- самый умный.')







