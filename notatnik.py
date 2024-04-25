import folium
import requests
from bs4 import BeautifulSoup

from models.data_source import users
def full_map(users:str)->None:
    lista_wspolrzednych = []
    map = folium.Map(location=[52, 21], zoom_start=8)
    for user in users:
        url: str = f'https://pl.wikipedia.org/wiki/{user['location']}'
        response = requests.get(url)
        # print(response.text)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = response_html.select('.latitude')[1].text.replace(",",".")
        longitude = response_html.select('.longitude')[1].text.replace(",",".")
        lista_wspolrzednych.append([latitude, longitude])
        print(latitude)
        print(longitude)
    for wspolrzedne in lista_wspolrzednych:
        folium.Marker(location=wspolrzedne).add_to(map)

    map.save(f'./common_map.html')

full_map(users)
