import os
import json

path = f"{os.getcwd()}/Music"


for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        filename = os.path.join(root, name)
        if name.endswith(".flac"):
            flac_location = filename
            json_location = f"{filename[0:-5]}.json"
            img_location = f"{filename[61:-5]}.jpg"
            with open(json_location) as file:
                json_data = json.load(file)
                data = json_data["format"]["tags"]
                data = list(data.values())
                # print(data)

                title = json_data["format"]["tags"]["TITLE"]
                album = json_data["format"]["tags"]["ALBUM"]
                artist = json_data["format"]["tags"]["ARTIST"]
                try:
                    release_date = json_data["format"]["tags"]["DATE"]
                except:
                    release_date = 0
                database = SoundCoreModel.objects.create(
                    author=artist,
                    album=album,
                    title=title,
                    album_art=img_location,
                    music_file=flac_location[61:],
                    release_date=release_date,
                )
                database.save()
