#!/bin/python

import sys
import dbus

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
        song = metadata['xesam:title']

        # print(artist, song, sep=' --- ')
        
        # for k, v in metadata.items():
        #     print(k, v)
    except Exception as e:
        print(e)

def fetch_Lyrics():
    pass

def main():
    pass