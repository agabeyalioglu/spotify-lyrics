#!/bin/python
import fetch_metadata as fm
import fetch_lyrics as fl
if __name__ == '__main__':
    metadata = fm.fetch_metadata()
    title = '\n'.join(metadata[::-1])
    lyrics = fl.fetch_lyrics(*metadata)
    print(title + "\n\n" + lyrics)