import requests
from bs4 import BeautifulSoup


def get_data_for_song(song_object):
    # to search
    query = "לקנות לך יהלום אייל גולן"

    base_url = "https://www.google.com/search?"
    updated_url = base_url + "+" + song_object["singer"] + "+" + song_object["title"]
    res = requests.get(updated_url)
    html = res.content.decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")
    data = soup.findAll("div", {"aria-label": "מידע כללי"})
    print(data)


if __name__ == '__main__':
    song_object = {
        "singer": "אייל גולן",
        "title": "לקנות לך יהלום"
    }
    get_data_for_song(song_object)
