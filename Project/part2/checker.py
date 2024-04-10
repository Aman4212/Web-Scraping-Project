import requests
from bs4 import BeautifulSoup
import sqlite3
from collections import Counter

dbName = "OlympicsData.db"
con = sqlite3.connect(dbName)
cursor = con.cursor()



query="SELECT * FROM SummerOlympics WHERE DONE_OR_NOT_DONE=1"
cursor.execute(query)
rows = cursor.fetchall()
# print(len(rows))
if len(rows)==8:
    print("All rows are populated")

    # Choosing Years
    print("Years Chosen :")
    query = "SELECT Year FROM SummerOlympics"
    result=cursor.execute(query)
    for i in result:
        print(i)

    # Calculating avrage number of atheletes

    print("Average number of Atheletes :")

    query="SELECT AVG(Athletes) FROM SummerOlympics"
    result=cursor.execute(query)

    for row in result:
        print(row)

    #Calculation 2nd query

    query="SELECT rank_1_nation FROM SummerOlympics"
    cursor.execute(query)
    rows_1=cursor.fetchall()
    # print(rows_1)

    query="SELECT rank_2_nation FROM SummerOlympics"
    cursor.execute(query)
    rows_2=cursor.fetchall()
    # print(rows_2)

    query="SELECT rank_3_nation FROM SummerOlympics"
    cursor.execute(query)
    rows_3=cursor.fetchall()
    # print(rows_3)

    merged_list = [t[0] for t in rows_1] + [t[0] for t in rows_2] + [t[0] for t in rows_3]

    # print(merged_list)

    string_counts = Counter(merged_list)

    # Find the most common string and its count
    most_common_string = max(string_counts, key=string_counts.get)
    max_occurrences = string_counts[most_common_string]

    print("Most common string:", most_common_string)
    