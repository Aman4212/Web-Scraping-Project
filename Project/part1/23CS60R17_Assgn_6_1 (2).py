import requests
import sqlite3
import json
from bs4 import BeautifulSoup

def get_latitude():
    lat=input("enter latitude: ")
    return str(lat)

def get_longitude():
    lon=input("enter longitude: ")
    return str(lon)


def getData(url):
    response = requests.get(url)
    #convert to text string and return 
    return response.text

def convertJson(data):
    return json.loads(data)

def createDatabaseConnect(dbName):
	con = sqlite3.connect(dbName)
	cur = con.cursor()
	return cur

def get_data(cursor):

    api_key = "0e9d9b58d2f6f0ac5b3db974a9fbdf99"
    complete_url = "http://api.openweathermap.org/data/2.5/weather?lat="+get_latitude()+"&lon="+get_longitude()+"&appid="+api_key
    # print(complete_url)

    response=requests.get(complete_url).text
        # print(response)

    res = json.loads(response)
    # print(type(res))


    city_name=res['name']
    city_temp=res['main']['temp']
    city_weather=res['weather'][0]['description']
    city_humidity=res['main']['humidity']
    city_windSpeed=res['wind']['speed']

        #creating database

        
        # query_check="SELECT count(name) FROM sqlite_master WHERE type='table' AND name='city_weather'"
        # cursor.execute(query)

        # if cursor.fetchone()[0]==1:
        #     query="DROP TABLE city_weather"
        #     cursor.execute(query)


        # City
        # ○ Temperature
        # ○ Description
        # ○ Humidity
        # ○ WindSpeed

    query = "CREATE TABLE IF NOT EXISTS city_weather(City, Temperature, Description, Humidity, WindSpeed)"
    cursor.execute(query)

    query = "INSERT INTO city_weather VALUES ('%s', '%s', '%s','%s','%s')"%(city_name, city_temp, city_weather, city_humidity, city_windSpeed)
    cursor.execute(query)

    query = "SELECT * from city_weather"
    result = cursor.execute(query)
    for row in result:
        print(row)
    

if __name__=="__main__":
    
    dbName = "Weather.db"
    cursor = createDatabaseConnect(dbName)
    for i in range(3):
        get_data(cursor)
    cursor.close()
