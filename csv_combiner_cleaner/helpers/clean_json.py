import json

def remove_duplicates(data):
    cleaned_data =[]
    seen = set()
    for d in data:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            cleaned_data.append(d)   
            
    return cleaned_data

def clean_json(json_file,logging):
    cleaned_data = []
    try:
        with open(json_file,"r") as f:
            data = json.load(f)
            no_duplicates = remove_duplicates(data)
            cleaned_data = no_duplicates
    except Exception as e:
        logging.error(f"[-] Error while cleaning data: {e}")

    return cleaned_data