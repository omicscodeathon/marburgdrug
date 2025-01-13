import requests # type: ignore
import os
import pandas as pd
import io

SAVE_RAW_DATA_PATH = os.path.join('data', 'raw')

# assay data
MARBURG_ACTIVITY_DATA_FILE = {'download_url': 'https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&actvty=all&response_type=save&aid=540276', 'title': 'MARBURG_ASSAY_DATA_RAW', 'save_path': os.path.join(SAVE_RAW_DATA_PATH, 'MARBURG_ASSAY_DATA_RAW.csv')} #743050


'''
download data files from pubchem
'''

def main():
    print('downloading dataset...')
    response = requests.get(MARBURG_ACTIVITY_DATA_FILE['download_url'])
    content = response.content
    df = pd.read_csv(io.BytesIO(content))
    print(df.describe())

    df.to_csv(MARBURG_ACTIVITY_DATA_FILE['save_path'])
    

        
    
if __name__ == '__main__':
    main()