import io
import json
import os


def write_json():
    lyrics_data = "/home/benaya/PycharmProjects/shironet/examples/json_data.json"
    with io.open(lyrics_data, 'w+', encoding='utf8') as outfile:
        outfile.write(unicode(json.dumps(data, ensure_ascii=False)))
    print("done!")

def format_json(data):
    re
def search():

    lyrics_dir = "/home/benaya/PycharmProjects/shironet/examples"
    lyrics_data = "/home/benaya/PycharmProjects/shironet/examples/json_data.json"
    file = open(lyrics_data)
    data = json.load(file)
    with io.open(lyrics_data, 'w+', encoding='utf8') as outfile:
        outfile.write(unicode(json.dumps(data, ensure_ascii=False)))
    print("done!")