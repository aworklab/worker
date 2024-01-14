# %%
import pandas as pd
import numpy as np
import keyring as kr

# %%
# 설치 
#pip install --upgrade oauth2client 
#pip install gspread
#pip install PyOpenSSL

'https://effortkim.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%EA%B8%80-%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C%EC%8B%9C%ED%8A%B8-%ED%8E%B8%EC%A7%91-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0/'

#%%
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# %%
# Authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
#%%
creds = ServiceAccountCredentials.from_json_keyfile_name('json', scope)
client = gspread.authorize(creds)

# Open the spreadsheet and select the worksheet by name
spreadsheet = client.open('시트이름')
worksheet = spreadsheet.worksheet('bs_db')

# Update a cell's value
row_num = 5
col_num = 5
cell = worksheet.cell(row_num, col_num)
cell.value = 'New Value'
worksheet.update_cell(row_num, col_num, 'TestValue')
# %%
