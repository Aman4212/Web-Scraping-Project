# Web-scraping-project

Overview
---------------

This project encompasses a web scraping system designed to collect and analyze data from the web using Python. The system focuses on two main tasks: collecting structured JSON data from the OpenWeatherMap API and extracting information about the Summer Olympics from Wikipedia. Additionally, it explores performance improvements through parallel processing.

Requirements
---------------
-Python 3.x
-Libraries: requests or urllib3, json, beautifulsoup4 (bs4), sqlite3, random
-External tools: SQLite database
-Installation
-To install the required Python libraries, run:

pip3 install requests beautifulsoup4 sqlite3
Replace requests with urllib3 if preferred.

Project Structure
--------------------
-weather_data_collector.py: Collects weather data from the OpenWeatherMap API and stores it in a SQLite database named Weather.db.
-olympics_data_scraper.py: Scrapes information about the Summer Olympics from Wikipedia and stores it in a SQLite database named OlympicsData.db.
-multiprocess_handler.py: Implements multiprocessing to speed up the scraping process for the Olympics data.
-scraper.py: Auxiliary script called by multiprocess_handler.py for parallel data processing.
-checker.py: Checks if all data rows in the OlympicsData.db are populated and reports on specific queries.

Usage
-----------
Collecting Weather Data
Obtain an API key from OpenWeatherMap.
Run weather_data_collector.py, specifying the cities you wish to query.
Scraping Olympics Data
Run olympics_data_scraper.py to scrape and store data about the Summer Olympics.
Multiprocessing to Speed Up Scraping
Run multiprocess_handler.py to initiate the multiprocessing scraping for the Olympics data.

Contribution
-------------
This project was completed as part of the Computing Laboratory I (CS69011) assignment under the Autumn Semester 2023, showcasing skills in web scraping, data processing, and the implementation of multiprocessing in Python.
