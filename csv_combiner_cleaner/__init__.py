"""
Usage:
    csv-combiner-cleaner combine <jsons_folder> [--target_file=<target_file>]
    csv-combiner-cleaner clean <json_file>

Options:

"""

from docopt import docopt

import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')

#import helpers
from csv_combiner_cleaner.helpers.combine_jsons import combine_jsons
from csv_combiner_cleaner.helpers.clean_json import clean_json
from csv_combiner_cleaner.helpers import helpers as hlp 


def main():
    '''entrypoint'''
    args = docopt(__doc__,version="csv-combiner-cleaner 0.1")

    if args["combine"]:
        jsons_folder = args["<jsons_folder>"]
        combined_data = combine_jsons(jsons_folder,logging)
        if args["--target_file"]:
            target_file = args["--target_file"]
            hlp.save_data_to_json(combined_data,target_file,logging)
            logging.info("[+] Done combining and saving data!")
        else:
            print(combined_data)
            
    elif args["clean"]:
        json_file = args["<json_file>"]
        clean_json(json_file)
        pass


if __name__=="__main__":
    main()