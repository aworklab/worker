game_code = 'G_SPD' # game code is
time_difference = 9

list_wotan_delabs = [
   'dau_day','nru_ru_day','job_status'
]

setting = {
   'nru_ru' :{
      'web' : {
         'is_country_valid' : False,
         'is_os_valid' : True,
         'dog' : 'love'
      }, 
      'app' : {
         'is_country_valid' : True,
         'is_os_valid' : True
      }
   },
   'dau_day' :{
      'web' : {
         'is_country_valid' : False,
         'is_os_valid' : True
      }, 
      'app' : {
         'is_country_valid' : True,
         'is_os_valid' : True,
         'cat' : 'loved'
      }
   }
}

# %%

s3_setting = {"game_code":{"0":"G_SPD","1":"G_SPD","2":"G_SPD","3":"G_SPD","4":"G_SPD","5":"G_SPD","6":"G_SPD","7":"G_SPD","8":"G_SPD","9":"G_SPD","10":"G_SPD","11":"G_SPD","12":"G_SPD","13":"G_SPD","14":"G_SPD","15":"G_SPD","16":"G_SPD","17":"G_SPD","18":"G_SPD","19":"G_SPD","20":"G_SPD","21":"G_SPD","22":"G_SPD","23":"G_SPD"},"game_name":{"0":"rumble-racing","1":"rumble-racing","2":"rumble-racing","3":"rumble-racing","4":"rumble-racing","5":"rumble-racing","6":"rumble-racing","7":"rumble-racing","8":"rumble-racing","9":"rumble-racing","10":"rumble-racing","11":"rumble-racing","12":"rumble-racing","13":"rumble-racing","14":"rumble-racing","15":"rumble-racing","16":"rumble-racing","17":"rumble-racing","18":"rumble-racing","19":"rumble-racing","20":"rumble-racing","21":"rumble-racing","22":"rumble-racing","23":"rumble-racing"},"db_name":{"0":"ldb","1":"ldb","2":"ldb","3":"ldb","4":"ldb","5":"ldb","6":"ldb","7":"ldb","8":"ldb","9":"ldb","10":"ldb","11":"ldb","12":"ldb","13":"ldb","14":"ldb","15":"ldb","16":"ldb","17":"ldb","18":"ldb","19":"ldb","20":"ldb","21":"ldb","22":"ldb","23":"ldb"},"is_total":{"0":True,"1":False,"2":True,"3":True,"4":True,"5":True,"6":True,"7":True,"8":True,"9":True,"10":True,"11":True,"12":True,"13":True,"14":True,"15":True,"16":True,"17":True,"18":True,"19":True,"20":True,"21":True,"22":False,"23":True},"table_name":{"0":"log_login_detail","1":"log_cash_purchase","2":"log_league_change","3":"log_star","4":"log_battle_ready","5":"log_battle_room_begin","6":"log_battle_room_end","7":"log_battle_user_begin","8":"log_battle_user_end","9":"log_tournament_join","10":"log_levelup","11":"log_victory_point","12":"log_victory_point_reward","13":"log_asset_change","14":"log_tournament_join","15":"log_levelup","16":"log_victory_point","17":"log_victory_point_reward","18":"log_asset_unlock","19":"log_collection","20":"log_achievement","21":"log_sticker_attach","22":"log_sticker","23":"log_alnumn_complete_total"},"s3_path":{"0":"s3://wotan-data/rumble-racing/log_login_detail/","1":"s3://wotan-data/rumble-racing/log_cash_purchase/","2":"s3://wotan-data/rumble-racing/log_league_change/","3":"s3://wotan-data/rumble-racing/log_star/","4":"s3://wotan-data/rumble-racing/log_battle_ready/","5":"s3://wotan-data/rumble-racing/log_battle_room_begin/","6":"s3://wotan-data/rumble-racing/log_battle_room_end/","7":"s3://wotan-data/rumble-racing/log_battle_user_begin/","8":"s3://wotan-data/rumble-racing/log_battle_user_end/","9":"s3://wotan-data/rumble-racing/log_tournament_join/","10":"s3://wotan-data/rumble-racing/log_levelup/","11":"s3://wotan-data/rumble-racing/log_victory_point/","12":"s3://wotan-data/rumble-racing/log_victory_point_reward/","13":"s3://wotan-data/rumble-racing/log_asset_change/","14":"s3://wotan-data/rumble-racing/log_tournament_join/","15":"s3://wotan-data/rumble-racing/log_levelup/","16":"s3://wotan-data/rumble-racing/log_victory_point/","17":"s3://wotan-data/rumble-racing/log_victory_point_reward/","18":"s3://wotan-data/rumble-racing/log_asset_unlock/","19":"s3://wotan-data/rumble-racing/log_collection/","20":"s3://wotan-data/rumble-racing/log_achievement/","21":"s3://wotan-data/rumble-racing/log_sticker_attach/","22":"s3://wotan-data/rumble-racing/log_sticker/","23":"s3://wotan-data/rumble-racing/log_alnumn_complete_total/"},"s_folder":{"0":"rumble-racing/log_login_detail/","1":"rumble-racing/log_cash_purchase/","2":"rumble-racing/log_league_change/","3":"rumble-racing/log_star/","4":"rumble-racing/log_battle_ready/","5":"rumble-racing/log_battle_room_begin/","6":"rumble-racing/log_battle_room_end/","7":"rumble-racing/log_battle_user_begin/","8":"rumble-racing/log_battle_user_end/","9":"rumble-racing/log_tournament_join/","10":"rumble-racing/log_levelup/","11":"rumble-racing/log_victory_point/","12":"rumble-racing/log_victory_point_reward/","13":"rumble-racing/log_asset_change/","14":"rumble-racing/log_tournament_join/","15":"rumble-racing/log_levelup/","16":"rumble-racing/log_victory_point/","17":"rumble-racing/log_victory_point_reward/","18":"rumble-racing/log_asset_unlock/","19":"rumble-racing/log_collection/","20":"rumble-racing/log_achievement/","21":"rumble-racing/log_sticker_attach/","22":"rumble-racing/log_sticker/","23":"rumble-racing/log_alnumn_complete_total/"},"redshift_name":{"0":"spd_log_login_detail","1":None,"2":"spd_log_league_change","3":"spd_log_star","4":"spd_log_battle_ready","5":"spd_log_battle_room_begin","6":"spd_log_battle_room_end","7":"spd_log_battle_user_begin","8":"spd_log_battle_user_end","9":"spd_log_tournament_join","10":"spd_log_levelup","11":"spd_log_victory_point","12":"spd_log_victory_point_reward","13":"spd_log_asset_change","14":"spd_log_asset_unlock","15":"spd_log_collection","16":"spd_log_victory_point","17":"spd_log_victory_point_reward","18":"spd_log_asset_unlock","19":"spd_log_collection","20":"spd_log_achievement","21":"spd_log_sticker_attach","22":None,"23":"spd_log_alnumn_complete"}}
# %%
s3_setting
# %%

# %%
