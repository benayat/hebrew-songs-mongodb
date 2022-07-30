import constants

if __name__ == '__main__':
    all_animals = ""
    for index, animal in enumerate(constants.ANIMAL_NAMES):
        all_animals = all_animals+animal
        if index < len(constants.ANIMAL_NAMES)-1:
            all_animals = all_animals+"-"
    print(all_animals)