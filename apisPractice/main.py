import requests
#import json


if __name__ == '__main__':
	#url = 'http://dogs.magnet.cl/api/v1/auth/'
	url = 'https://pokeapi.co/api/v2/pokemon-form/'    

	response = requests.get(url)

	if response.status_code == 200:

		payload = response.json()
		results = payload.get('results', [])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)