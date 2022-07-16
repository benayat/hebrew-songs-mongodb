import os
import numpy
import pymongo

if __name__ == '__main__':
    # with open('../examples/json_data.json') as file:
    #     file_data = json.load(file)

    # all_files = os.listdir("../examples")
    # all_songs = []
    #
    # for path in all_files:
    #     if path.__contains__("json_data.json"):
    #         continue
    #     song_details = path.split("_")
    #     singer = song_details[0]
    #     song_title = song_details[1]
    #     song_lyrics = open("../examples/"+path, 'r').read()
    #     song_object = {
    #         "title": song_title,
    #         "artist": singer.replace("\r", "").replace("\n", "").replace("\t", ""),
    #         "lyrics": song_lyrics
    #     }
    #     all_songs.append(song_object)
    #
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["shironet"]
    print(client.list_database_names())
    songs_collection = mydb["songs"]
    # songs_devided_to_sublists = numpy.array_split(all_songs, 30)
    # for song_list in songs_devided_to_sublists:
    #     song_list_as_python_list = song_list.tolist()
    #     result = songs_collection.insert_many(song_list_as_python_list)
    print("done")
    res1 = songs_collection.find({"$text": {"$search": "\"כלב\""}})
