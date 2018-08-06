from bs4 import BeautifulSoup
import requests, re

def fetch_lyrics(song_artist, song_title):
    google_base_url = "https://www.google.com/search"

    new_artist_name = song_artist.replace(" ", "+")
    new_title = song_title.replace(" ", "+")

    p = {"q" : [new_artist_name, new_title, "metrolyrics"]}
    page = requests.get(google_base_url, params=p)
    page.encode = 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    href = soup.find("h3", class_="r").a.get('href')
    url = re.search("q=(.*?)&", href).group(1)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    return "\n\n".join(i.text for i in soup.findAll("p", class_='verse'))