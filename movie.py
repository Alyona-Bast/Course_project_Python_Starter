import requests
from random import randint
import json


def top_movie():
	selection = randint(1, 45)

	try:
		url = "https://moviesminidatabase.p.rapidapi.com/movie/order/byPopularity/"

		headers = {
			"X-RapidAPI-Key": "84249c3b15msh08fa2206d39249fp1ef24bjsnea4c4da242fa",
			"X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers)

		movie_title = json.loads(response.text)['results'][selection]['title']

	except requests.exceptions.ConnectionError:
		with open("movie_data.json", "r", encoding="utf-8") as fr:
			movie_title = json.load(fr)['results'][selection]['title']

	print(f'Рекомендую подивитися: "{movie_title}", про нього гарні відгуки')


def movie():
	while True:
		top_movie()
		print()
		if input("Підібрати інший варіан? Натисни 1\n"
				 "Зайнятися чимось іншим, натисни Enter: ") == "1":
			print()
		else:
			break
