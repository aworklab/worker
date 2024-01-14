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