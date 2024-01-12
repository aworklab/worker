# %%
import pandas as pd
import numpy as np

from importlib import reload
import info
# %%
reload(info)
# %%
setting = info.setting;setting
s3_setting = info.s3_setting;setting
# %%
def get_table_info(info_file = setting) :

   res = []
   for main_key, sub_dict in info_file.items() :
      for sub_key, value in sub_dict.items() :
         row = pd.json_normalize(value)
         row['table'] = main_key
         row['type'] = sub_key
         res.append(row)

   df = pd.concat(res, ignore_index = True)
   df.set_index(['table','type'], inplace = True)
   df = df.reset_index()

   return df
# %%
get_table_info(s3_setting)

# %%

# %%
temp = pd.read_clipboard(sep ='\t')
temp = temp.to_json(orient = 'columns')  
temp = temp.replace('\\','')
temp = temp.replace('true','True')
temp = temp.replace('false','False')
temp = temp.replace('null','')
temp
# %%
temp
# %%
s3_setting
# %%
setting
# %%
get_table_info(s3_setting)
# %%

# %%

# %%
