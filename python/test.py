#!/usr/bin/python
import os
import pycurl
import StringIO

from time import sleep
from influxdb import InfluxDBClient

mss_data = StringIO.StringIO()
marker_offset = 'market_mss'
info_list = []

def get_mss_monitor(offset):
    URL = "http://api.mq.aodianyun.com/v1/messages/dms_notify/0/" + str(offset)
    curl.setopt(pycurl.URL,URL)
    curl.setopt(pycurl.WRITEFUNCTION,mss_data.write)
    curl.perform()


curl = pycurl.Curl()
curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
curl.setopt(pycurl.CONNECTTIMEOUT, 60)
curl.setopt(pycurl.TIMEOUT, 600)
curl.setopt(pycurl.NOPROGRESS, 1)
curl.setopt(pycurl.ENCODING, 'gzip')


if  os.path.exists(marker_offset):
    with open(marker_offset,'r') as f:
        offset = f.read()
    if len(offset) == 0:
        offset = 0
else:
    with open(marker_offset,'w') as f:
        f.write(0)
    offset = 0


get_mss_monitor(432676848)


res = eval(mss_data.getvalue())

with open(marker_offset,'w') as f:
    f.write(str(res['nextOffset']))

client = InfluxDBClient('114.55.9.109', 8086, 'root', 'aodian123456', 'test')
#for list_info  in res['list'][0]:
list_info = res['list'][0]
list_info["tags"] = eval(list_info['body'])
list_info["measurement"]="dms_notify"
list_info["fields"] = {"value": 0.66}
info_list.append(list_info)
client.write_points(info_list)
