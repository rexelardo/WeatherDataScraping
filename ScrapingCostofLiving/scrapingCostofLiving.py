






cost_of_living_data = {'city': city_scrape, 'state':state_scrape,'county':[], 'Overall':[],'Grocery':[],'Health':[],\
                       'Housing':[],\
                      'Median Home Cost':[], 'Utilities':[], 'Transportation':[], 'Miscellaneous':[]}




for i, j in zip(cost_of_living_data['city'],cost_of_living_data['state']):
    url = f'https://www.bestplaces.net/cost_of_living/city/{j}/{i}'
    driver = webdriver.Chrome()
    driver.get(url) 
    try:    
        tables = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table")))
    except TimeoutException:
        print(f'No data for {i},{j}')
        cost_of_living_data['Overall'].append('no data')
        cost_of_living_data['Grocery'].append('no data')
        cost_of_living_data['Health'].append('no data')
        cost_of_living_data['Housing'].append('no data')
        cost_of_living_data['Median Home Cost'].append('no data')
        cost_of_living_data['Utilities'].append('no data')
        cost_of_living_data['Transportation'].append('no data')
        cost_of_living_data['Miscellaneous'].append('no data')
        cost_of_living_data['county'].append('no data')
        driver.quit()
        continue
    newTable = pd.read_html(tables[0].get_attribute('outerHTML'))
    try:
        overall = newTable[0][1][1]
        print(f'Getting the data of overall in  {i},{j}: it is equal to {overall}')
        cost_of_living_data['Overall'].append(overall)
        #getting grocery
        grocery = newTable[0][1][2]
        print(f'Getting the data of grocery in {i},{j}: it is equal to {grocery}')
        cost_of_living_data['Grocery'].append(grocery)
        #getting health
        health = newTable[0][1][3]
        print(f'Getting the data of health {i},{j}: it is equal to {health}')
        cost_of_living_data['Health'].append(health)
        # getting housing
        housing = newTable[0][1][4]
        print(f'Getting the data of housing in {i},{j}: it is equal to {housing}')
        cost_of_living_data['Housing'].append(housing)
        # getting median home cost
        median = newTable[0][1][5]
        print(f'Getting the data of median home cost in {i},{j}: it is equal to {median}')
        cost_of_living_data['Median Home Cost'].append(median)
        # getting utilities
        utilities = newTable[0][1][6]
        print(f'Getting the data of utilities in {i},{j}: it is equal to {utilities}')
        cost_of_living_data['Utilities'].append(utilities)
        # getting transportation
        transportation = newTable[0][1][7]
        print(f'Getting the data of transportation for {i},{j}: it is equal to {transportation}')
        cost_of_living_data['Transportation'].append(transportation)
        # getting misc
        misc = newTable[0][1][8]
        print(f'Getting the data misc {i},{j}: it is equal to {misc}')
        cost_of_living_data['Miscellaneous'].append(misc)
        County = driver.find_elements_by_xpath('//div[@class="col-md-7 mt-2 mb-4"]')[0].text
        getCounty = County.split('/')[3].strip()
        weather_data['county'].append(getCounty)
        driver.quit()
    except KeyError:
        print(f'server issue with {i},{j} right now')
        cost_of_living_data['Overall'].append('server issue right now, maybe try later')
        cost_of_living_data['Grocery'].append('server issue right now, maybe try later')
        cost_of_living_data['Health'].append('server issue right now, maybe try later')
        cost_of_living_data['Housing'].append('server issue right now, maybe try later')
        cost_of_living_data['Median Home Cost'].append('server issue right now, maybe try later')
        cost_of_living_data['Utilities'].append('server issue right now, maybe try later')
        cost_of_living_data['Transportation'].append('server issue right now, maybe try later')
        cost_of_living_data['Miscellaneous'].append('server issue right now, maybe try later')
        cost_of_living_data['county'].append('server issue right now, maybe try later')
        driver.quit()