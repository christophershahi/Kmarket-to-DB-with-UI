from tools import DownloadJSON
import requests
import time
import sqlite3
import logging
import winsound
import mysql.connector


start_time = time.time()

# This will log our each requests and record the time and error whenever the script fails so it would be easy to debug later:
logging.basicConfig(filename='opendata.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(message)s', datefmt=f"%d-%b-%y %H:%M:%S")


# Making an sql connection
 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '', 
    database = 'openData'
)

curr = mydb.cursor()
db_name = "CREATE DATABASE openData"
# curr.execute(db_name)

table_name = "CREATE TABLE kmarketOpendata (Date VARCHAR(50), Commodity VARCHAR(50), Unit VARCHAR(50), Minimum VARCHAR(50), Maximum VARCHAR(50), Average VARCHAR(50))"
#curr.execute(table_name)

print(f"---------\nScraping.\n---------------------------------------")

total_records = 197161 # This increases the page limit in api-url:

opendata_kmarket = f"https://opendatanepal.com/api/3/action/datastore_search?resource_id=06a18d43-c7ef-42d7-96a7-284671f731bd&limit={total_records}"

json = DownloadJSON(opendata_kmarket).read_JSON()


# We have the needed datas in this key value pair in dictionary data type:
jsons_datas = json['result']['records']


# Looping and extracting the data using list comprehension:
try:    
    dates = [jsons_datas[i]['Date'].replace("T00:00:00", "") for i in range(total_records)]
    commodities = [jsons_datas[i]['Commodity'] for i in range(total_records)]
    units = [jsons_datas[i]['Unit'] for i in range(total_records)]
    maximum = [jsons_datas[i]['Maximum'] for i in range(total_records)]
    minimum = [jsons_datas[i]['Minimum'] for i in range(total_records)]
    average = [jsons_datas[i]['Average'] for i in range(total_records)]
except IndexError:
    print("Index error!")



# Storing all the scraped data in tuple by using zip method:
all_lists = list(zip(dates, commodities, units, minimum, maximum, average))

s = "insert into kmarketOpendata VALUES(%s, %s, %s, %s, %s, %s)"

curr.executemany(s, all_lists)
mydb.commit()
mydb.close()
print(f"Database is saved! | {total_records} records scraped.\n--------------------------------------------")
time.sleep(2)


# Calulation for the total time of execution:
total_time = total_time = round(time.time()-start_time, 2)
time_in_secs = round(total_time, 2)
time_in_mins = round(total_time/60, 2)

print(f"Took |> {time_in_secs} seconds. | {time_in_mins} minutes.\n---------------------------------------")


# Play the sound after the completion of Scraping process:
winsound.PlaySound('notification.mp3', winsound.SND_FILENAME)