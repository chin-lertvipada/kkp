#etl.py
#import Library
import glob
import json
import os
import sys
from typing import List

import psycopg2
import requests


# api-endpoint
SOURCE = "https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/"
PARAM = sys.argv[1]
APIKEY = "?apikey=ea820aad3cd75bc1482eef5798b4d793"
URL = SOURCE + PARAM + APIKEY

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
datas = r.json()

print(datas["symbol"])
hists = datas["historical"]

# extracting latitude, longitude and formatted address
# of the first matching location
for hist in hists:
    print(hist["date"])
    print(hist["label"])
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
# 	%(latitude, longitude,formatted_address))