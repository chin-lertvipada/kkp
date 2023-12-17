# importing the requests library
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

print(type(datas))


# extracting latitude, longitude and formatted address
# of the first matching location
for data in datas:
    print(data['symbol'])
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
# 	%(latitude, longitude,formatted_address))
