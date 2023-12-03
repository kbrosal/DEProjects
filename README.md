# Yellow Pages Scraper
## Overview
This Yellow Pages Scraper is an efficient ETL (Extract, Transform, Load) tool. It extracts restaurant data from Yellow Pages in Los Angeles, processes and cleans the data for analysis, and then stores it in an organized database format.

## Project Purpose
The aim is to assist a digital service company that supports restaurants. We gather detailed restaurant information, clean and analyze it to identify potential business opportunities for our clients in the restaurant industry.

## Client Perspective
Our client, an aspiring entrepreneur in the restaurant sector, seeks insights into the market. Our high-tech solution offers them a comprehensive understanding of successful restaurant owners, helping them gain a competitive edge.

##Technical Aspects
Data Collection: Uses web scraping tools like Beautiful Soup and Selenium.
Data Storage: Utilizes a SQL database.
Data Analysis: Employs Python libraries (Pandas, NumPy, Matplotlib) for data processing and analysis.
Pattern Identification: Applies machine learning with Scikit-Learn.

## Deliverables
A detailed report with analytical insights on top-performing restaurant owners.
Clean, organized Python code for ongoing or future use.

## Project Impact
Our solution equips the client with data-driven insights, offering a comprehensive view of the market and aiding in strategic business decisions.

## Requirements
1. Python 3.7 or higher.
2. Python libraries: requests, beautifulsoup4, pandas, psycopg2, regex, time, json, and psycopg2.
3. An AWS database.
4. An SQL client like DBeaver for database connectivity.

## Usage Instructions
- Clone the repository.
- Install required libraries: pip install -r requirements.txt.
- Configure the AWS database in config.py.
- Run yellow_pages_scraper.py to gather and store data.
- Execute data_analysis.py for data visualization and recommendations.

## Acknowledgments
Thanks to our restaurant business clients for their invaluable input.
