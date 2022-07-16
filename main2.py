import io
import json
import os
import config

from bs4 import BeautifulSoup
from lxml.builder import unicode

import constants
from pages.artist_page import ArtistsPages
from song import Song


def parse_artists(url):
    page = session.get(url, timeout=60)

    # Decode the page content from bytes to string
    html = page.content.decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")
    print(soup.h2)
    print(soup.head)
    artists = soup.findAll(class_="index_link")
    for i, artist in enumerate(artists):
        artist_url = 'https://shironet.mako.co.il/artist?type=works&' + artist.get("href")[8:]
        artist_name = artist.string.strip()
        print("artist url is: ", artist_url)
        print("artist name is: ", artist_name)
        parse_artists_songs(artist_url, i, artist.string)


def parse_artists_songs(url, songs_index, artist):
    page = session.get(url, timeout=60)

    # Decode the page content from bytes to string
    html = page.content.decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")

    # table width="100%" border="0" cellspacing="3" cellpadding="0" dir="rtl" style="padding-right: 5px"
    songs_table = soup.find("table", {'width': '100%', 'cellspacing': '3', 'cellpadding': '0'})
    if songs_table:
        local_songs = songs_table.findAll(class_="artist_player_songlist")
        for song in local_songs:
            print(str(songs_index) + ': https://shironet.mako.co.il' + song.get("href"))
            print(artist)
            songs_index += 1
            parse_song('https://shironet.mako.co.il' + song.get("href"), songs_index, artist)


def parse_song(url, local_song_index, artist):
    res = session.get(url, timeout=60, )

    # Decode the page content from bytes to string
    html = res.content.decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")

    if res.status_code == 200 and soup.h1 and soup.find(class_="artist_lyrics_text"):
        title = soup.h1.string + "_" + str(local_song_index)
        title = title.replace("/", "").replace("\\", "").replace("\"", "").replace("*", "") \
            .replace(":", "").replace("?", "").replace("<", "").replace(">", "").replace("|", "")
        singer = soup.find(class_="artist_singer_title").string if soup.find(
            class_="artist_singer_title") else artist.string
        singer = singer.replace("/", "").replace("\\", "").replace("\"", "").replace("*", "") \
            .replace(":", "").replace("?", "").replace("<", "").replace(">", "").replace("|", "")
        year = soup.find(class_="artist_color_gray").string if soup.find(class_="artist_color_gray") else 0
        lyrics = soup.find(class_="artist_lyrics_text").text
        song = Song(url, title, year, singer, lyrics)
        songs.append(song)
        data['songs'].append({
            'url': url,
            'title': title,
            'year': year,
            'singer': singer,
        })


def get_artist_pages():
    artist_pages = set()
    for letter, size in constants.ARTISTS_BY_LETTER_SIZES.items():
        artist_letter_page = ArtistsPages(letter, size)
        artist_pages.add(artist_letter_page)
    return artist_pages


def write_lyrics_and_metadata(lyrics_dir):
    for song in songs:
        file_name = song.singer + "_" + song.title + ".txt"
        filepath = os.path.join(lyrics_dir, file_name)
        with io.open(filepath, 'w+', encoding='utf8') as file:
            file.write(song.lyrics)


if __name__ == '__main__':
    session = config.config_http_client()
    all_artist_pages = get_artist_pages()
    songs = []
    data = {'songs': []}
    for artist_pages_set in all_artist_pages:
        for index, artists_url in enumerate(artist_pages_set.urls):
            print(index)
            print(artists_url)
            parse_artists(artists_url)

    lyrics_dir = "/home/benaya/PycharmProjects/shironet/examples"

    print("done with downloading data, now copying to files:")
    write_lyrics_and_metadata(lyrics_dir)
    lyrics_data = "/home/benaya/PycharmProjects/shironet/examples/json_data.json"
    with io.open(lyrics_data, 'w+', encoding='utf8') as outfile:
        outfile.write(unicode(json.dumps(data, ensure_ascii=False)))
    print("done!")
