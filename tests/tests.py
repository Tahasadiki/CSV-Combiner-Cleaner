from csv_combiner_cleaner.helpers.clean_json import clean_json
from csv_combiner_cleaner.helpers.combine_jsons import combine_jsons
import unittest
import os

import logging
logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')

class TestCsvCombinerCleaner(unittest.TestCase):

    def assess_data_cleaning(self):
        test_file = os.path.join(os.path.realpath(__file__),"tests_files","to_clean.json")
        cleaned_data = clean_json(test_file,logging)
        self.assertTrue(cleaned_data)

    def assess_data_combining(self):
        test_folder = os.path.join(os.path.realpath(__file__),"tests_files")
        combined_data = combine_jsons(test_folder,logging)
        self.assertTrue(combined_data)

if __name__ == '__main__':
    unittest.main()