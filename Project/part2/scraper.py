import requests
from bs4 import BeautifulSoup
import sqlite3


if __name__ == "__main__":

    dbName = "OlympicsData.db"
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    query="SELECT DONE_OR_NOT_DONE,WikipediaURL FROM SummerOlympics WHERE DONE_OR_NOT_DONE = 0"
    cursor.execute(query)


    rows = cursor.fetchall()
    headers = {
  'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8',
  'Cache-Control': 'max-age=60',
  'Referer': 'https://example.com/previous-page',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    for row in rows:
        dnd=1
        url=row[1]
        # print(url)
        response=requests.get(url, headers=headers)
        soup=BeautifulSoup(response.text,'html.parser')

        name=soup.find('span',class_='mw-page-title-main').text
        # print(name)
        wiki_url=url
        year=name[0:4]
        year=int(year)
        # print(year)
        # print(wiki_url)
        table=soup.find('table',class_="wikitable")
        rows=table.find_all('tr')
        row=rows[1]
        column=row.find_all('td')
        # print(row)
        host_city=column[1].text.strip()
        # print(host_city)

        table=soup.find('table',class_='infobox')
        # print(table)
        table=table.find_all('tr')
        atheletes=table[4].text
        atheletes=atheletes[8:14].strip()
        atheletes=int(atheletes.replace(",",""))
        #   print(atheletes)
        #   atheletes=int(atheletes)
        ranks=soup.find('table',class_='plainrowheaders')

        ranks=ranks.find_all('tr')
        rank_1_nation=ranks[1].a.text
        rank_2_nation=ranks[2].a.text
        rank_3_nation=ranks[3].a.text

        tables=soup.find_all('table',class_='wikitable')

        # print(tables[2]\)
        # print(len(tables))


        for table in tables:

            table_header=table.th
            if table_header is not None:
                if "Participating" in table_header.text:
                #    print(table_header.text)
                    break
            
        # print(table)
        # print(part_table)
        table=table.find_all('tr')
        table=table[1].td
        table=table.find('div')
        table=table.find_all('li')
        nations=""
        # print(len(table))
        for item in table:
            nations=nations +" " + item.a.text

        sports=soup.find_all('table',class_='wikitable')
        # print(len(sports))

        for sport in sports:
            sport_header=sport.th
            if sport_header is not None:
                if "Sports" in sport_header.text:
                    break
        sport_rows=sport.find_all('tr')
        sport_row=sport_rows[1].div
        sport_list=sport_row.find_all('li')
        olympic_sports=""
        for link in sport_list:
            link=link.a
            if link is not None:
                olympic_sports=olympic_sports + "," + link.text




        # print(nations)
        # query = "CREATE TABLE IF NOT EXISTS SummerOlympics(Name, WikipediaURL, Year, HostCity,Athletes, Rank_1_nation, Rank_2_nation, Rank_3_nation, Particpating_nations, Sports,DONE_OR_NOT_DONE)"
        # cursor.execute(query)
        d=1
        # print(type(d))

        query = "UPDATE SummerOlympics SET Name = '%s', WikipediaURL = '%s', Year = %d, HostCity = '%s', Athletes = %d, Rank_1_nation = '%s', Rank_2_nation = '%s', Rank_3_nation = '%s', Particpating_nations = '%s', Sports = '%s', DONE_OR_NOT_DONE = %d WHERE WikipediaURL = '%s'" % (name, wiki_url, year, host_city, atheletes, rank_1_nation, rank_2_nation, rank_3_nation, nations, olympic_sports, d, wiki_url)
        cursor.execute(query)


con.commit()       

# query = "SELECT * FROM SummerOlympics"
# result=cursor.execute(query)


# for row in result:
#      print(row)
    



    
   
    
# Close the connection
con.close()
