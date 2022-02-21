import sys
from typing import List, Dict
from client import Client




# add samsum datasets
client = Client(dataset_name_db="test_samsum", dataset_name_sdk="samsum", calculate_features = True, data_typology = 'textdataset')
client.add_dataset_from_sdk()