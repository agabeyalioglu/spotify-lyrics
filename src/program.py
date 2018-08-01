#!/bin/python

from bs4 import BeautifulSoup
import urllib3, dbus, re

def fetch_metadata():
    try:
        bus = dbus.SessionBus()
        spotify_bus = bus.get_object("org.mpris.MediaPlayer2.spotify",
                                            "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus,
                                            "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", 
                                            "Metadata")

        artist = metadata['xesam:artist'][0]
        title = metadata['xesam:title']
    
        return artist, re.split("[,\-!(?:]+", title)[0]

        # print(artist, song, sep=' --- ')
        
        # for k, v in metadata.items():
        #     print(k, v)
    except Exception as e:
        print(e)

def fetch_lyrics(song_artist, song_title):
    print(song_artist, song_title)

def main():
    fetch_lyrics(*fetch_metadata())

main()