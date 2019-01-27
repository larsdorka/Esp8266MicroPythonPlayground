import json


def run():
    config_file_path = "config/wlan.json"
    file_data = {}
    try:
        with open(config_file_path) as file:
            file_data = json.load(file)
    except Exception as ex:
        print("error on reading config file: " + str(ex))
    print(file_data)
