# %%
import pandas as pd
import numpy as np
from importlib import reload
import s3_info
import info
import keyring as kr
import re
# %%
reload(s3_info)
reload(info)
# %%
setting = s3_info.setting;setting
s3_setting = s3_info.s3_setting;s3_setting

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
df = pd.DataFrame(s3_setting)
# %%
for i in range(len(df)) :
   print(i)

# %%
i = 2
workers = df.iloc[i,:];workers
# %%

temp_query = """SELECT
	DATE(DATE_ADD(reg_date, INTERVAL {time_difference} hour)) division_date
	, account_idx
	, account_type
	, os_type
	, country
	, league_no
	, lev
	, reg_dt_utc
	, DATE_ADD(reg_date, INTERVAL {time_difference} hour) reg_dt
	, DATE_ADD(now(), INTERVAL {time_difference} hour) mig_dt
	, log_when
	, log_sub
	, login_type
	, nft_info
	, YEAR(DATE_ADD(reg_date, INTERVAL {time_difference} hour)) year
	, MONTH(DATE_ADD(reg_date, INTERVAL {time_difference} hour)) month
	, DAY(DATE_ADD(reg_date, INTERVAL {time_difference} hour)) day
FROM log_login
WHERE reg_date > '{start_dt}' AND reg_date <= '{end_dt}';
"""
temp_query
# %%
time_difference = 9
start_dt = '2023-01-01'
end_dt = '2023-01-02'
args = re.findall(r'\{([^}]+)\}',temp_query)
args = list(set(args));args
format_arg = ','.join([f"{var}={var}" for var in args])
format_call = f'temp_query.format({format_arg})';format_call
# %%
eval(format_call)
# %%

# %%

# %%
