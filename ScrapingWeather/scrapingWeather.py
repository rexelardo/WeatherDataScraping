
import pandas as pd

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




#Starting Selenium instance
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


weather_data = {'city': city_scrape, 'state':state_scrape, 'county':[],'Rainfall':[],'Snowfall':[],'Precipitation':[],\
           'Sunny':[],'Avg. July High':[],'Avg. Jan. Low':[], 'Comfort Index (higher=better)':[],'UV Index':[],\
           'Elevation':[]}



for i, j in zip(weather_data['city'],weather_data['state']):
    url = f'https://www.bestplaces.net/climate/city/{j}/{i}'
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("enable-features=NetworkServiceInProcess")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    
    # This part will be to see where the Excel is stored
    dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in weather_data.items() })
    dict_df.to_csv('weatherdata.csv')
    
    try:    
        driver.get(url)
        tables = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table")))
    except TimeoutException:
        print(f'No data for {i},{j}')
        weather_data['Rainfall'].append('no data')
        weather_data['Snowfall'].append('no data')
        weather_data['Precipitation'].append('no data')
        weather_data['Sunny'].append('no data')
        weather_data['Avg. July High'].append('no data')
        weather_data['Avg. Jan. Low'].append('no data')
        weather_data['Comfort Index (higher=better)'].append('no data')
        weather_data['UV Index'].append('no data')
        weather_data['Elevation'].append('no data')
        driver.quit()
        continue
    
    try:
        newTable = pd.read_html(tables[0].get_attribute('outerHTML'))
        elevation = newTable[0][1][9]
        print(f'Getting the data of Elevation for {i},{j}: it is equal to {elevation}')
        weather_data['Elevation'].append(elevation)
        rainfall = newTable[0][1][1]
        print(f'Getting the data of rainfall in  {i},{j}: it is equal to {rainfall}')
        weather_data['Rainfall'].append(rainfall)
        #getting snowfall
        snow = newTable[0][1][2]
        print(f'Getting the data of snowfall in {i},{j}: it is equal to {snow}')
        weather_data['Snowfall'].append(snow)
        #getting precipitation
        precipitation = newTable[0][1][3]
        print(f'Getting the data of precipitation {i},{j}: it is equal to {precipitation}')
        weather_data['Precipitation'].append(precipitation)
        # getting sunny
        sunny = newTable[0][1][4]
        print(f'Getting the data of sunny days in {i},{j}: it is equal to {sunny}')
        weather_data['Sunny'].append(sunny)
        # getting Avg. July High
        july_high = newTable[0][1][5]
        print(f'Getting the data of Avg. July High in {i},{j}: it is equal to {july_high}')
        weather_data['Avg. July High'].append(july_high)
        # getting Avg. Jan. Low
        jan_low = newTable[0][1][6]
        print(f'Getting the data of Avg. Jan. Low in {i},{j}: it is equal to {jan_low}')
        weather_data['Avg. Jan. Low'].append(jan_low)
        # getting Comfort Index (higher=better)
        comfort = newTable[0][1][7]
        print(f'Getting the data of Comfort Index (higher=better) for {i},{j}: it is equal to {comfort}')
        weather_data['Comfort Index (higher=better)'].append(comfort)
        # getting UV Index
        uv = newTable[0][1][8]
        print(f'Getting the data of UV Index for {i},{j}: it is equal to {uv}')
        weather_data['UV Index'].append(uv)
        # getting Elevation
        driver.quit()
    except KeyError:
        print(f'server issue with {i},{j} right now')
        weather_data['Rainfall'].append('server issue, perhaps collect later')
        weather_data['Snowfall'].append('server issue, perhaps collect later')
        weather_data['Precipitation'].append('server issue, perhaps collect later')
        weather_data['Sunny'].append('server issue, perhaps collect later')
        weather_data['Avg. July High'].append('server issue, perhaps collect later')
        weather_data['Avg. Jan. Low'].append('server issue, perhaps collect later')
        weather_data['Comfort Index (higher=better)'].append('server issue, perhaps collect later')
        weather_data['UV Index'].append('server issue, perhaps collect later')
        weather_data['Elevation'].append('server issue, perhaps collect later')
        driver.quit()