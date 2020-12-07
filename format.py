import pandas as pd

# Replace with relative paths for respective .csv files from Synthetic data repository
synthTestDataMaster = pd.read_csv(r"Synthetic-data-master/test_data_master.csv")

synthTestDataMaster.to_json('./data/master.json', orient='index' ,date_format="epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
    
