import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(url=URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, 'html.parser')
header_name = soup.find_all(name='h3', class_='title')
with open('top_100_movies', 'w') as f:
    for movie in reversed(header_name):
        f.write(movie.getText())
        f.write('\n')
