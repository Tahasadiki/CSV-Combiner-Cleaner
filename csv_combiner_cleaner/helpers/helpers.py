import json

def save_data_to_json(data,target_file,logging):
    try:
        with open(target_file,'w') as f:
            json.dump(data,f)
    except Exception as e:
        logging.error(f"[-] Error while writing data to file: {e}")