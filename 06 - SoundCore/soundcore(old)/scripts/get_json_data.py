import os
import json


def get_tag(path):
    with open(path) as file:
        json_data = json.load(file)

        print(json_data["format"]["tags"]["title"])


get_tag(f"{os.getcwd()}/test.json")
