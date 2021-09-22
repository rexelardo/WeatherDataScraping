""" This code is meant to deploy on a server and indeed scrape the entire BestPlaces website"""

#Importing packages
import pandas as pd


# Getting all cities
data = pd.read_csv('cities_to_scrape.csv')
data.columns =  data.iloc[0]
data = data.drop(0,0)
data
cities_needed = []
for i in data['City, State']:
    cities_needed.append(i)

city_scrape = []
state_scrape = []
for i in cities_needed:
    i = i.replace(',','')
    city_scrape.append(i[:-2])
    state_scrape.append(i[-2:])

# OK now we import selenium and run the next steps

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
# import base64
# import streamlit as st
# def st_csv_download_button(df):
#     csv = df.to_csv(index=False) #if no filename is given, a string is returned
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a>'
#     st.markdown(href, unsafe_allow_html=True)  


home_data = {'city': city_scrape[13400:], 'state':state_scrape[13400:],'county':[], 'number of homes':[], 'median home age':[],\
           'median home cost':[], 'home appr. last 12 months':[], 'home appr. last 5 years':[],\
           'home appr. last 10 years':[], 'Property Tax Rate':[], 'Property Taxes Paid':[], 'Homes Owned':[],\
           'Housing Vacant':[], 'Homes Rented':[]}



#Let's see if we can download this info
# dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in home_data.items() })
# st_csv_download_button(dict_df)


# Now we run the Selenium instance
for i, j in zip(home_data['city'],home_data['state']):
    url = f'https://www.bestplaces.net/housing/city/{j}/{i}'
    # trying the method to deploy on Heroku
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("enable-features=NetworkServiceInProcess")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    
    # This part will be to see where the Excel is stored
    dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in home_data.items() })
    dict_df.to_csv('housingData.csv')
    try:  
        driver.get(url)  
        tables = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table")))
    except TimeoutException:
        print(f'No data for {i},{j}')
        home_data['number of homes'].append('no data')
        home_data['median home age'].append('no data')
        home_data['median home cost'].append('no data')
        home_data['home appr. last 12 months'].append('no data')
        home_data['home appr. last 5 years'].append('no data')
        home_data['home appr. last 10 years'].append('no data')
        home_data['Property Tax Rate'].append('no data')
        home_data['Property Taxes Paid'].append('no data')
        home_data['Homes Owned'].append('no data')
        home_data['Housing Vacant'].append('no data')
        home_data['Homes Rented'].append('no data')
        home_data['county'].append('no data')
        driver.quit()
        continue
    try:
        newTable = pd.read_html(tables[0].get_attribute('outerHTML'))
        #Putting this at the top, so that it triggers immediately a KeyError if there are problems
        homes_rented = newTable[0][1][11]
        print(f'Getting the data of home Homes Rented {i},{j}: it is equal to {homes_rented}')
        home_data['Homes Rented'].append(homes_rented) 
        #getting median home age
        median_home_age = newTable[0][1][2]
        print(f'Getting the data of median home age {i},{j}: it is equal to {median_home_age}')
        home_data['median home age'].append(median_home_age)
        #getting number of homes
        number_of_homes = newTable[0][1][1]
        print(f'Getting the data of number of homes {i},{j}: it is equal to {number_of_homes}')
        home_data['number of homes'].append(number_of_homes)
        #getting median home cost
        median_home_cost = newTable[0][1][3]
        print(f'Getting the data of median home cost {i},{j}: it is equal to {median_home_cost}')
        home_data['median home cost'].append(median_home_cost)
        # getting home appr. last 12 months
        median_home_appr_12mo = newTable[0][1][4]
        print(f'Getting the data of home appr. last 12 months {i},{j}: it is equal to {median_home_appr_12mo}')
        home_data['home appr. last 12 months'].append(median_home_appr_12mo)
        # getting home home appr. last 5 years
        median_home_appr_5y = newTable[0][1][5]
        print(f'Getting the data of home appr. last 5 years {i},{j}: it is equal to {median_home_appr_5y}')
        home_data['home appr. last 5 years'].append(median_home_appr_5y)
        # getting home home home appr. last 10 years
        median_home_appr_10y = newTable[0][1][6]
        print(f'Getting the data of home appr. last 5 years {i},{j}: it is equal to {median_home_appr_10y}')
        home_data['home appr. last 10 years'].append(median_home_appr_10y)
        # getting home Property Tax Rate
        property_tax = newTable[0][1][7]
        print(f'Getting the data of home Property Tax Rate {i},{j}: it is equal to {property_tax}')
        home_data['Property Tax Rate'].append(property_tax)
        # getting home Property Taxes Paid
        property_tax_paid = newTable[0][1][8]
        print(f'Getting the data of home Property Taxes Paid {i},{j}: it is equal to {property_tax_paid}')
        home_data['Property Taxes Paid'].append(property_tax_paid)
        # getting home Homes Owned
        homes_owned = newTable[0][1][9]
        print(f'Getting the data of home Homes Owned {i},{j}: it is equal to {homes_owned}')
        home_data['Homes Owned'].append(homes_owned)
        # getting home Housing Vacant
        housing_vacant = newTable[0][1][10]
        print(f'Getting the data of home Housing Vacant {i},{j}: it is equal to {housing_vacant}')
        home_data['Housing Vacant'].append(housing_vacant)
        # getting home Homes Rented  
        County = driver.find_elements_by_xpath('//div[@class="col-md-7 mt-2 mb-4"]')[0].text
        getCounty = County.split('/')[3].strip()
        home_data['county'].append(getCounty)
        driver.quit()
    except KeyError :
        print(f'server issue with {i},{j} right now')
        home_data['median home age'].append('server issue, perhaps collect later')
        home_data['number of homes'].append('server issue, perhaps collect later')
        home_data['median home cost'].append('server issue, perhaps collect later')
        home_data['home appr. last 12 months'].append('server issue, perhaps collect later')
        home_data['home appr. last 5 years'].append('server issue, perhaps collect later')
        home_data['home appr. last 10 years'].append('server issue, perhaps collect later')
        home_data['Property Tax Rate'].append('server issue, perhaps collect later')
        home_data['Property Taxes Paid'].append('server issue, perhaps collect later')
        home_data['Homes Owned'].append('server issue, perhaps collect later')
        home_data['Housing Vacant'].append('server issue, perhaps collect later')
        home_data['Homes Rented'].append('server issue, perhaps collect later')
        home_data['county'].append('server issue, perhaps collect later')
        driver.quit()



