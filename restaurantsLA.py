import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
import json

#creating an empty list for the data to be appended in here.
list_restaurantsLA = []


#function that extract the parsed html element by setting the soup object. 
def extract(url):
    #Used headers in the request to avoid being blocked by the website.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/101.0.4951.54 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'https://google.com',
        'DNT': '1',
        'Accept-Language': 'en-GB,en;q=0.5'
    }

    url = ("https://www.yellowpages.com/los-angeles-ca/restaurants?page=1")
    page = requests.get(url, headers=headers).content

    soup = BeautifulSoup(page, "html.parser")

    return soup.find_all('div', class_='result')


#Main function to extract and transform the data.
def transform(organic_results):

    for i, item in enumerate(organic_results):
        
        restaurant_name = item.find('a', class_ =  "business-name").text

        phone_number = item.find('div', class_ = "phones phone primary").text
        
        try:
            street_address = item.find('div', class_='street-address').text
        except:
            street_address = ''                                           

        locality = item.find('div', class_ = "locality").text
        
        try:
            website = item.find("a", class_ = "track-visit-website")["href"]
        except:
            website = ''

        menu = item.find('a', class_ = 'menu', href=True)
        if menu is not None:
            menu_link = "www.yellowpages.com" + menu['href']
        else:
            menu_link = None
        
        categories = item.find('div', {"class": "categories"}).find_all("a")[1].text

        try:
            sub_categories = item.find('div', {"class": "categories"}).find_all("a")[2].text
        except:
            sub_categories = ''
        
        internalRating = item.find('div', class_ = 'ratings').find('div')
        if internalRating is not None:
            rating = str(internalRating)
        
            value = re.findall(r'(?<=result-rating )(\S*\w*\s*\w*)?\"', rating)
            
            string_to_num = {
                "one": 1,
                "one half": 1.5,
                "two": 2,
                "two half": 2.5,
                "three": 3,
                "three half": 3.5,
                "four": 4,
                "four half": 4.5,
                "five": 5
            }

            value = string_to_num.get(value[0])
                
            internalRating = value
        else:
            internalRating = None
        
        number_of_reviews = item.find('span', class_ = "count")
        if number_of_reviews is not None:
            count = number_of_reviews.text
            number_of_reviews = count.replace("(", "").replace(")", "")
        else:
            number_of_reviews = None

        for e in item.select('.info-section:has(h2)'):
            if rating:= e.select_one('.ratings').get('data-tripadvisor'):
                TA_ratings = (json.loads(rating).get('rating'))
            else:
                TA_ratings = None

        for e in item.select('.info-section:has(h2)'):
            if rating:= e.select_one('.ratings').get('data-tripadvisor'):
                TA_rating_count = (json.loads(rating).get('count'))
            else:
                TA_rating_count = None
        
        try:
            years_in_business = item.find('div', class_ = "years-in-business").find_all("div")[0].text
        except:
            years_in_business = ''

        try:
            top_comment = item.find('p', class_='body').text
        except:
            top_comment = "No comment added"


        #creating a dictionary to store the datas transformed and append it to the empty list created above.
        restaurantsLA = {
            'restaurant_name': restaurant_name,
            'phone_number': phone_number,
            'street_address': street_address,
            'locality': locality,
            'website': website,
            'menu_link': menu_link,
            'categories': categories,
            'sub_categories': sub_categories,
            'internal_rating': internalRating,
            'number_of_reviews': number_of_reviews,
            'TA_ratings': TA_ratings,
            'TA_rating_count': TA_rating_count, 
            'years_in_business': years_in_business,
            'top_comment': top_comment
        }
        list_restaurantsLA.append(restaurantsLA)
    return

#funtion that load the data to a dataframe using Pandas and save it as a .csv file.
def load():
    df = pd.DataFrame(list_restaurantsLA)
    df.to_csv('restaurantsLA.csv', index=False)

#Dealing with pagination in the website.
for x in range(1,101):
    print(f'Getting the data in page {x}')
    organic_results = extract(f'https://www.yellowpages.com/los-angeles-ca/restaurants?page={x}')
    transform(organic_results)
    time.sleep(5)

load()
print('Saved to CSV')