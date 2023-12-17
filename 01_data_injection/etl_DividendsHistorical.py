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


table_insert_DividendsHistorical1 = "INSERT INTO DividendsHistorical %s "
table_insert_DividendsHistorical2 = "VALUES %s ON CONFLICT DO NOTHING;"


def process(cur, conn, symbol, hists):

    for hist in hists:
        # add symbol to the data
        data = {"symbol": symbol}
        data.update(hist)

        # extract col_name and value
        col = [d for d in data if str(data[d])!='']
        val = [data[v] for v in data if str(data[v])!='']

        # build insert sql
        sql1 =  table_insert_DividendsHistorical1 % (tuple(col),)
        sql2 =  table_insert_DividendsHistorical2 % (tuple(val),)

        cur.execute(sql1.replace("'", "") + sql2)
            
    conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    process(cur, conn, datas["symbol"], datas["historical"])

    conn.close()


if __name__ == "__main__":
    main()
