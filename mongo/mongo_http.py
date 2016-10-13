#/usr/bin/env python
from pymongo import MongoClient
import time
import json
num = 0
stat = {}
now =  time.strftime('%Y%m%d')
table_name = 'alert_codes' + now
http_stat_table= 'http_stat' + now
conn = MongoClient("127.0.0.1",27017)
database = conn.hlssysalert
key = ['http_stat']
initial = {'count': 0}
func = '''
    function(obj,prev){
        prev.count = prev.count + obj.count
    }
'''
num = database[table_name].group(key,None,initial,func)
database[http_stat_table].save({"_id":now,"info":num})
    
