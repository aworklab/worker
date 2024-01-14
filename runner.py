# %%
import pandas as pd
import numpy as np
from importlib import reload
import s3_info
import keyring as kr
# %%
reload(s3_info)
# %%
setting = s3_info.setting;setting
s3_setting = s3_info.s3_setting;s3_setting
# %%
pd.DataFrame(s3_setting)
# %%

# %%
temp = pd.read_clipboard(sep ='\t')
temp = temp.iloc[:,0:7]
temp = temp.to_json(orient = 'columns')  
temp = temp.replace('\\','')
temp = temp.replace('true','True')
temp = temp.replace('false','False')
temp = temp.replace('null','None')
temp
# %% 
kr.set_password('awork','gs4','aaaaa')

# %%
a = kr.get_password('admin','gs4')

# %%
kr.get_password('awork')
# %%
