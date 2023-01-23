import requests
from random import randint
import json


def shazam():
	selection = randint(1, 19)
	try:
		url = "https://shazam.p.rapidapi.com/charts/track"

		querystring = {"locale":"en-US", "pageSize":"20", "startFrom":"0"}

		headers = {
			"X-RapidAPI-Key": "84249c3b15msh08fa2206d39249fp1ef24bjsnea4c4da242fa",
			"X-RapidAPI-Host": "shazam.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)


		song_title = json.loads(response.text)['tracks'][selection]['title']
		subtitle = json.loads(response.text)['tracks'][selection]['subtitle']
		href = json.loads(response.text)['tracks'][selection]['share']["href"]

	except requests.exceptions.ConnectionError:
		with open("music_data.json", "r", encoding="utf-8") as fr:
			mus = json.load(fr)
			song_title = mus['tracks'][selection]['title']
			subtitle = mus['tracks'][selection]['subtitle']
			href = mus['tracks'][selection]['share']["href"]

	print(f'Shazam рекомендує послухати: "{song_title}", яку виконує {subtitle}\n'
		  f'Це можна зробити за посиланням: {href}')


def music():
	while True:
		shazam()
		print()
		if input("Підібрати інший варіан? Натисни 1\n"
				 "Зайнятися чимось іншим, натисни Enther: ") == "1":
			print()
		else:
			break



