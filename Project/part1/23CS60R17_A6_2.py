import requests
import sqlite3
import json
from bs4 import BeautifulSoup
import random




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

headers = {
  'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8',
  'Cache-Control': 'max-age=60',
  'Referer': 'https://example.com/previous-page',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

url='https://en.wikipedia.org/wiki/Summer_Olympic_Games'
response=requests.get(url, headers=headers)
# print(response.text)

#Creating the database


soup=BeautifulSoup(response.text,'html.parser')
# print(soup)



table=soup.find('table',class_='sortable wikitable')
# print(table)
rows=table.find_all('tr')

import random

while True:
     
    random_divisible_by_four1=random.randint(1972, 2020)
    random_divisible_by_four2=random.randint(1972, 2020)
    if random_divisible_by_four1 % 4==0 and random_divisible_by_four2 % 4==0 and random_divisible_by_four1 !=random_divisible_by_four2 :
         break


multiple_url=[f"https://en.wikipedia.org/wiki/{random_divisible_by_four1}_Summer_Olympics",f"https://en.wikipedia.org/wiki/{random_divisible_by_four2}_Summer_Olympics"]

# print(multiple_url)
headers = {
  'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8',
  'Cache-Control': 'max-age=60',
  'Referer': 'https://example.com/previous-page',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }


dbName = "OlympicsData.db"
cursor = createDatabaseConnect(dbName)
print(multiple_url)
for i in range (len(multiple_url)):

  url_1=multiple_url[i]
  # print(url_1)
  response=requests.get(url_1,headers=headers)
  soup=BeautifulSoup(response.text,"html.parser")
  # print(soup)
  name=soup.find('span',class_='mw-page-title-main')
  name=name.text
  # print(name)
  # print(name)
  wiki_url=url_1
  year=name[0:4]
  year=int(year)
  # print(year)
  table=soup.find('table',class_="wikitable")
  # print(table)
  rows=table.find_all('tr')
  # print(rows)
  row=rows[1]
  column=row.find_all('td')
  # print(row)
  host_city=column[1].text.strip()
  # print(host_city)

  table=soup.find('table',class_='infobox')
  # print(table)
  table=table.find_all('tr')
  atheletes=table[4].text
  atheletes=atheletes[8:]
  # print(atheletes)
  ranks=soup.find('table',class_='plainrowheaders')

  ranks=ranks.find_all('tr')
  rank_1_nation=ranks[1].a.text
  rank_2_nation=ranks[2].a.text
  rank_3_nation=ranks[3].a.text

  #Creatin the database


  query = "CREATE TABLE IF NOT EXISTS SummerOlympics(Name, WikipediaURL, Year, HostCity, Athletes, Rank_1_nation, Rank_2_nation, Rank_3_nation)"
  cursor.execute(query)

  query = "INSERT INTO SummerOlympics VALUES ('%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s')" % (name, wiki_url, year, host_city, atheletes, rank_1_nation, rank_2_nation, rank_3_nation)
  cursor.execute(query)

  # print(type(name))
  # print(wiki_url)
  # print(year)
  # print(host_city)
  # print(atheletes)
  # print(rank_1_nation)
  # print(rank_1_nation)
  # print(rank_2_nation)

# query = "SELECT * FROM SummerOlympics"
# result = cursor.execute(query)
# for row in result:
# 	print(row)
     
# ○ What are the years you chose?
print("Years Chosen: ")
query = "SELECT year FROM SummerOlympics"
result_1 = cursor.execute(query)
for row in result_1:
	print(row)


row_list=[]
query="SELECT rank_1_nation, rank_2_nation, rank_3_nation FROM SummerOlympics"
result_1 = cursor.execute(query)
for row in result_1:
    row_list.append(row)
    

cursor.close()

tuple1 =row_list[0] 
tuple2 =row_list[1]

set1 = set(tuple1)
set2 = set(tuple2)

print("Common Nation(s) :")
common_nations = set1.intersection(set2)
common_nations_tuple = tuple(common_nations)
print(common_nations_tuple)
          
 
   








     


