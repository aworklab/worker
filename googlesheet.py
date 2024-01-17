# %%
import pandas as pd
import numpy as np
import keyring as kr
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
# %%
# 설치 
#pip install --upgrade oauth2client 
#pip install gspread
#pip install PyOpenSSL

'https://greeksharifa.github.io/references/2023/04/10/gspread-usage/'

# %%
# Authenticate with Google Sheets API
json_is = 'gs4.json'
url_is = 'https://docs.google.com/spreadsheets/d/1bG6oa_dU9Qzkj2kaGI_NCYZGzGAhO_pbn5w3hAKMQH8/edit#gid=923913297'
key_is = '1bG6oa_dU9Qzkj2kaGI_NCYZGzGAhO_pbn5w3hAKMQH8'
sheet_name = '433.AWS_Work'
#%%
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://spreadsheets.google.com/feed'
]
credentials = Credentials.from_service_account_file(
    'gs4.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

gc.open(sheet_name)

#%% 
#gc = gspread.service_account('gs4.json')
gc = gspread.service_account('gs4.json')

sh = gc.open('433.AWS_Work')
sh = gc.open_by_key(key_is)
sh = gc.open_by_url(url_is)
#%%
sheet = sh.worksheets()
sheet = sh.worksheet('s3_url')
# %%
df = pd.DataFrame(sheet.get_all_values())
# %%
pd.DataFrame(sheet.get_all_records())
# %%
