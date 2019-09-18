import json
from os import listdir
from os.path import isfile, join

def get_json_files(jsons_folder):
    json_files =[]
    for f in listdir(jsons_folder):
        f = join(jsons_folder, f)
        if isfile(f) and f.endswith('.json') :
            json_files.append(f)

    return json_files

def combine_json_files(json_files,logging):
    combined_data = []
    for json_file in json_files:
        try:
            with open(json_file,'r') as f:
                data = json.load(f)
                combined_data.extend(data)
        except Exception as e:
            logging.error(f"[-] Failed reading file {json_file}: {e}")

    return combined_data 


def combine_jsons(jsons_folder,logging):

    json_files = get_json_files(jsons_folder)

    combined_data = combine_json_files(json_files,logging)
    
    return combined_data