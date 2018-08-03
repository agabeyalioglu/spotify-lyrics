from bs4 import BeautifulSoup
import requests

def fetch_lyrics(song_artist, song_title):
    quote_page = 'http://www.metrolyrics.com/take-me-to-church-lyrics-hozier.html'
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.text, 'html.parser')
    lyrics = soup.findAll("p", attrs={'class':'verse'})

    print(lyrics)
