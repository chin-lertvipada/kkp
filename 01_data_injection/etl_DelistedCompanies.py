#etl.py
#import Library
import glob
import json
import os
from typing import List

import psycopg2
import requests


# api-endpoint
SOURCE = "https://financialmodelingprep.com/api/v3/delisted-companies"
PARAMS = ""
APIKEY = "?apikey=ea820aad3cd75bc1482eef5798b4d793"
URL = SOURCE + PARAMS + APIKEY

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
datas = r.json()


table_insert_DelistedCompanies     = "INSERT INTO DelistedCompanies VALUES %s ON CONFLICT DO NOTHING;"


def process(cur, conn, data):

    for data in datas:
        # insert
        val = data["symbol"], data["companyName"], data["exchange"], data["ipoDate"], data["delistedDate"]
        sql_insert = table_insert_DelistedCompanies % str(val)
        cur.execute(sql_insert)
            
    conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    process(cur, conn, datas)

    conn.close()


if __name__ == "__main__":
    main()
