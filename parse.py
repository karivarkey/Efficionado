import json

def get_items(fileObject):
    rawData = json.load(fileObject)
    items = {}
    for key , value  in rawData.items():
        items[key] = value
    return items
        

def string_to_json(string):
    jsonString = {}
    stringLines = string.split("\n")
    for i in stringLines:
        if ":" in i:
            key , value = i.split(":",1)
            jsonString[key.strip()] = value.strip()
    return jsonString

