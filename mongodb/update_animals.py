import io
import json

from lxml.builder import unicode
from pymongo import MongoClient
import constants
from bson.json_util import dumps



if __name__ == '__main__':

    client = MongoClient('mongodb://localhost:27017/')
    # firstUpdateRes = client['shironet']['songs'].update_many({}, {'$set': {'has_animal': False}}, upsert=False)
    for animal in constants.ANIMAL_NAMES:
        animalFilter = {
            '$text': {
                '$search': animal
            }
        }
        result = client['shironet']['songs'].update_many(
            filter=animalFilter, update={'$set': {'animal': animal, 'has_animal': True}}, upsert=False
        )
        result_list = list(result)
        baseDir = "/home/benaya/Documents/Refael/"
        with io.open(baseDir+animal, 'w+', encoding='utf8') as outfile:
            outfile.write(unicode(dumps(result_list, ensure_ascii=False)))
        print("done!")



