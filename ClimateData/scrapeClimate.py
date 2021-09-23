
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








climate_data = {'city': city_scrape[5410:], 'state':state_scrape[5410:],'JanHigh':[],'JanLow':[],'FebHigh':[],'FebLow':[],\
                      'MarHigh':[], 'MarLow':[], 'AprHigh':[], 'AprLow':[],\
               'MayHigh':[], 'MayLow':[], 'JunHigh':[], 'JunLow':[], 'JulHigh':[], 'JulLow':[], 'AugHigh':[], 'AugLow':[],\
               'SepHigh':[], 'SepLow':[], 'OctHigh':[], 'OctLow':[],\
               'NovHigh':[], 'NovLow':[], 'DecHigh':[], 'DecLow':[],\
               'JanHotDays':[], 'JanFreezingDays':[], 'JanRainyDays':[], 'JanSnowyDays':[],\
               'FebHotDays':[], 'FebFreezingDays':[], 'FebRainyDays':[], 'FebSnowyDays':[],\
               'MarHotDays':[], 'MarFreezingDays':[], 'MarRainyDays':[], 'MarSnowyDays':[],\
               'AprHotDays':[], 'AprFreezingDays':[], 'AprRainyDays':[], 'AprSnowyDays':[],\
               'MayHotDays':[], 'MayFreezingDays':[], 'MayRainyDays':[], 'MaySnowyDays':[],\
               'JunHotDays':[], 'JunFreezingDays':[], 'JunRainyDays':[], 'JunSnowyDays':[],\
               'JulHotDays':[], 'JulFreezingDays':[], 'JulRainyDays':[], 'JulSnowyDays':[],\
               'AugHotDays':[], 'AugFreezingDays':[], 'AugRainyDays':[], 'AugSnowyDays':[],\
               'SepHotDays':[], 'SepFreezingDays':[], 'SepRainyDays':[], 'SepSnowyDays':[],\
               'OctHotDays':[], 'OctFreezingDays':[], 'OctRainyDays':[], 'OctSnowyDays':[],\
               'NovHotDays':[], 'NovFreezingDays':[], 'NovRainyDays':[], 'NovSnowyDays':[],\
               'DecHotDays':[], 'DecFreezingDays':[], 'DecRainyDays':[], 'DecSnowyDays':[]}



from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


for i, j in zip(climate_data['city'],climate_data['state']):
    url = f'https://www.bestplaces.net/weather/city/{j}/{i}'
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("enable-features=NetworkServiceInProcess")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    
    # This part will be to see where the Excel is stored
    dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in climate_data.items() })
    dict_df.to_csv('climateData.csv')
    
    try:    
        driver.get(url) 
        tables = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table")))
    except TimeoutException:
        print(f'No data for {i},{j}')
        climate_data['JanHigh'].append('no data')
        climate_data['JanLow'].append('no data')
        climate_data['FebHigh'].append('no data')
        climate_data['FebLow'].append('no data')
        climate_data['MarHigh'].append('no data')
        climate_data['MarLow'].append('no data')
        climate_data['AprHigh'].append('no data')
        climate_data['AprLow'].append('no data')
        climate_data['MayHigh'].append('no data')
        climate_data['MayLow'].append('no data')
        climate_data['JunHigh'].append('no data')
        climate_data['JunLow'].append('no data')
        climate_data['JulHigh'].append('no data')
        climate_data['JulLow'].append('no data')
        climate_data['AugHigh'].append('no data')
        climate_data['AugLow'].append('no data')
        climate_data['SepHigh'].append('no data')
        climate_data['SepLow'].append('no data')
        climate_data['OctHigh'].append('no data')
        climate_data['OctLow'].append('no data')
        climate_data['NovHigh'].append('no data')
        climate_data['NovLow'].append('no data')
        climate_data['DecHigh'].append('no data')
        climate_data['DecLow'].append('no data')
        climate_data['JanHotDays'].append('no data')
        climate_data['JanFreezingDays'].append('no data')
        climate_data['JanRainyDays'].append('no data')
        climate_data['JanSnowyDays'].append('no data')
        climate_data['FebHotDays'].append('no data')
        climate_data['FebFreezingDays'].append('no data')
        climate_data['FebRainyDays'].append('no data')
        climate_data['FebSnowyDays'].append('no data')
        climate_data['MarHotDays'].append('no data')
        climate_data['MarFreezingDays'].append('no data')
        climate_data['MarRainyDays'].append('no data')
        climate_data['MarSnowyDays'].append('no data')
        climate_data['AprHotDays'].append('no data')
        climate_data['AprFreezingDays'].append('no data')
        climate_data['AprRainyDays'].append('no data')
        climate_data['AprSnowyDays'].append('no data')
        climate_data['MayHotDays'].append('no data')
        climate_data['MayFreezingDays'].append('no data')
        climate_data['MayRainyDays'].append('no data')
        climate_data['MaySnowyDays'].append('no data')
        climate_data['JunHotDays'].append('no data')
        climate_data['JunFreezingDays'].append('no data')
        climate_data['JunRainyDays'].append('no data')
        climate_data['JunSnowyDays'].append('no data')
        climate_data['JulHotDays'].append('no data')
        climate_data['JulFreezingDays'].append('no data')
        climate_data['JulRainyDays'].append('no data')
        climate_data['JulSnowyDays'].append('no data')
        climate_data['AugHotDays'].append('no data')
        climate_data['AugFreezingDays'].append('no data')
        climate_data['AugRainyDays'].append('no data')
        climate_data['AugSnowyDays'].append('no data')
        climate_data['SepHotDays'].append('no data')
        climate_data['SepFreezingDays'].append('no data')
        climate_data['SepRainyDays'].append('no data')
        climate_data['SepSnowyDays'].append('no data')
        climate_data['OctHotDays'].append('no data')
        climate_data['OctFreezingDays'].append('no data')
        climate_data['OctRainyDays'].append('no data')
        climate_data['OctSnowyDays'].append('no data')
        climate_data['NovHotDays'].append('no data')
        climate_data['NovFreezingDays'].append('no data')
        climate_data['NovRainyDays'].append('no data')
        climate_data['NovSnowyDays'].append('no data')
        climate_data['DecHotDays'].append('no data')
        climate_data['DecFreezingDays'].append('no data')
        climate_data['DecRainyDays'].append('no data')
        climate_data['DecSnowyDays'].append('no data')
        driver.quit()
        continue
    try:
        newTable1 = pd.read_html(tables[1].get_attribute('outerHTML'))
        newTable2 = pd.read_html(tables[2].get_attribute('outerHTML'))
        #getting decsnow
        decsnow = newTable2[0]['SnowyDays'][11]
        print(f'Getting the decsnow for {i},{j}: it is equal to {decsnow}')
        climate_data['DecSnowyDays'].append(decsnow)
        janhigh = newTable1[0][1][1]
        print(f'Getting the data of janhigh in  {i},{j}: it is equal to {janhigh}')
        climate_data['JanHigh'].append(janhigh)
        #getting janlow
        janlow = newTable1[0][2][1]
        print(f'Getting the data of janlow in {i},{j}: it is equal to {janlow}')
        climate_data['JanLow'].append(janlow)
        #getting febhigh
        febhigh = newTable1[0][1][2]
        print(f'Getting the data of febhigh {i},{j}: it is equal to {febhigh}')
        climate_data['FebHigh'].append(febhigh)
        # getting feblow
        feblow = newTable1[0][2][2]
        print(f'Getting the data of feblow in {i},{j}: it is equal to {feblow}')
        climate_data['FebLow'].append(feblow)
        # getting marhigh
        marhigh = newTable1[0][1][3]
        print(f'Getting the data of marhigh in {i},{j}: it is equal to {marhigh}')
        climate_data['MarHigh'].append(marhigh)
        # getting marlow
        marlow = newTable1[0][2][3]
        print(f'Getting the data of marlow in {i},{j}: it is equal to {marlow}')
        climate_data['MarLow'].append(marlow)
        # getting transportation
        aprhigh = newTable1[0][1][4]
        print(f'Getting the data of aprhigh for {i},{j}: it is equal to {aprhigh}')
        climate_data['AprHigh'].append(aprhigh)
        # getting misc
        aprlow = newTable1[0][2][4]
        print(f'Getting the aprlow for {i},{j}: it is equal to {aprlow}')
        climate_data['AprLow'].append(aprlow)
        mayhigh = newTable1[0][1][5]
        print(f'Getting the data of mayhigh in  {i},{j}: it is equal to {mayhigh}')
        climate_data['MayHigh'].append(mayhigh)
        #getting maylow
        maylow = newTable1[0][2][5]
        print(f'Getting the data of maylow in {i},{j}: it is equal to {maylow}')
        climate_data['MayLow'].append(maylow)
        #getting febhigh
        junehigh = newTable1[0][1][6]
        print(f'Getting the data of febhigh {i},{j}: it is equal to {junehigh}')
        climate_data['JunHigh'].append(junehigh)
        # getting feblow
        junlow = newTable1[0][2][6]
        print(f'Getting the data of junlow in {i},{j}: it is equal to {junlow}')
        climate_data['JunLow'].append(junlow)
        # getting julhigh
        julhigh = newTable1[0][1][7]
        print(f'Getting the data of julhigh in {i},{j}: it is equal to {julhigh}')
        climate_data['JulHigh'].append(julhigh)
        # getting julow
        jullow = newTable1[0][2][7]
        print(f'Getting the data of jullow in {i},{j}: it is equal to {jullow}')
        climate_data['JulLow'].append(jullow)
        # getting aughigh
        aughigh = newTable1[0][1][8]
        print(f'Getting the data of aughigh for {i},{j}: it is equal to {aughigh}')
        climate_data['AugHigh'].append(aughigh)
        # getting auglow
        auglow = newTable1[0][2][8]
        print(f'Getting the auglow for {i},{j}: it is equal to {auglow}')
        climate_data['AugLow'].append(auglow)
        #getting septhigh
        sephigh = newTable1[0][1][9]
        print(f'Getting the data of sephigh in  {i},{j}: it is equal to {sephigh}')
        climate_data['SepHigh'].append(sephigh)
        #getting maylow
        seplow = newTable1[0][2][9]
        print(f'Getting the data of seplow in {i},{j}: it is equal to {seplow}')
        climate_data['SepLow'].append(seplow)
        #getting febhigh
        octhigh = newTable1[0][1][10]
        print(f'Getting the data of octhigh {i},{j}: it is equal to {octhigh}')
        climate_data['OctHigh'].append(octhigh)
        # getting octlow
        octlow = newTable1[0][2][10]
        print(f'Getting the data of octlow in {i},{j}: it is equal to {octlow}')
        climate_data['OctLow'].append(octlow)
        # getting novhigh
        novhigh = newTable1[0][1][11]
        print(f'Getting the data of novhigh in {i},{j}: it is equal to {novhigh}')
        climate_data['NovHigh'].append(novhigh)
        # getting julow
        novlow = newTable1[0][2][11]
        print(f'Getting the data of novlow in {i},{j}: it is equal to {novlow}')
        climate_data['NovLow'].append(novlow)
        # getting aughigh
        dechigh = newTable1[0][1][12]
        print(f'Getting the data of dechigh for {i},{j}: it is equal to {dechigh}')
        climate_data['DecHigh'].append(dechigh)
        # getting auglow
        declow = newTable1[0][2][12]
        print(f'Getting the declow for {i},{j}: it is equal to {declow}')
        climate_data['DecLow'].append(declow)
        #getting Janhotdays
        janhot = newTable2[0]['HotDays'][0]
        print(f'Getting the janhotdays for {i},{j}: it is equal to {janhot}')
        climate_data['JanHotDays'].append(janhot)
        #getting janfreezingdays
        janfreezing = newTable2[0]['FreezingDays'][0]
        print(f'Getting the janfreezing for {i},{j}: it is equal to {janfreezing}')
        climate_data['JanFreezingDays'].append(janfreezing)
        #getting janrain
        janrain = newTable2[0]['RainyDays'][0]
        print(f'Getting the janrain for {i},{j}: it is equal to {janrain}')
        climate_data['JanRainyDays'].append(janrain)
        #getting jansnow
        jansnow = newTable2[0]['SnowyDays'][0]
        print(f'Getting the jansnow for {i},{j}: it is equal to {jansnow}')
        climate_data['JanSnowyDays'].append(jansnow)
                #getting febhotdays
        febhot = newTable2[0]['HotDays'][1]
        print(f'Getting the febhotdays for {i},{j}: it is equal to {febhot}')
        climate_data['FebHotDays'].append(febhot)
        #getting janfreezingdays
        febfreezing = newTable2[0]['FreezingDays'][1]
        print(f'Getting the febfreezing for {i},{j}: it is equal to {febfreezing}')
        climate_data['FebFreezingDays'].append(febfreezing)
        #getting janrain
        febrain = newTable2[0]['RainyDays'][1]
        print(f'Getting the febrain for {i},{j}: it is equal to {febrain}')
        climate_data['FebRainyDays'].append(febrain)
        #getting jansnow
        febsnow = newTable2[0]['SnowyDays'][1]
        print(f'Getting the febsnow for {i},{j}: it is equal to {febsnow}')
        climate_data['FebSnowyDays'].append(febsnow)
        #getting marhot
        marhot = newTable2[0]['HotDays'][2]
        print(f'Getting the marhotdays for {i},{j}: it is equal to {marhot}')
        climate_data['MarHotDays'].append(marhot)
        #getting janfreezingdays
        marfreezing = newTable2[0]['FreezingDays'][2]
        print(f'Getting the marfreezing for {i},{j}: it is equal to {marfreezing}')
        climate_data['MarFreezingDays'].append(marfreezing)
        #getting janrain
        marrain = newTable2[0]['RainyDays'][2]
        print(f'Getting the marrain for {i},{j}: it is equal to {marrain}')
        climate_data['MarRainyDays'].append(febrain)
        #getting jansnow
        marsnow = newTable2[0]['SnowyDays'][2]
        print(f'Getting the marsnow for {i},{j}: it is equal to {marsnow}')
        climate_data['MarSnowyDays'].append(marsnow)
        #getting aprhot
        aprhot = newTable2[0]['HotDays'][3]
        print(f'Getting the aprhotdays for {i},{j}: it is equal to {aprhot}')
        climate_data['AprHotDays'].append(aprhot)
        #getting janfreezingdays
        aprfreezing = newTable2[0]['FreezingDays'][3]
        print(f'Getting the aprfreezing for {i},{j}: it is equal to {aprfreezing}')
        climate_data['AprFreezingDays'].append(aprfreezing)
        #getting janrain
        aprrain = newTable2[0]['RainyDays'][3]
        print(f'Getting the aprrain for {i},{j}: it is equal to {aprrain}')
        climate_data['AprRainyDays'].append(aprrain)
        #getting jansnow
        aprsnow = newTable2[0]['SnowyDays'][3]
        print(f'Getting the aprsnow for {i},{j}: it is equal to {aprsnow}')
        climate_data['AprSnowyDays'].append(aprsnow)
        #getting mayhot
        mayhot = newTable2[0]['HotDays'][4]
        print(f'Getting the mayhotdays for {i},{j}: it is equal to {mayhot}')
        climate_data['MayHotDays'].append(mayhot)
        #getting janfreezingdays
        mayfreezing = newTable2[0]['FreezingDays'][4]
        print(f'Getting the mayfreezing for {i},{j}: it is equal to {mayfreezing}')
        climate_data['MayFreezingDays'].append(mayfreezing)
        #getting janrain
        mayrain = newTable2[0]['RainyDays'][4]
        print(f'Getting the mayrain for {i},{j}: it is equal to {mayrain}')
        climate_data['MayRainyDays'].append(mayrain)
        #getting jansnow
        maysnow = newTable2[0]['SnowyDays'][4]
        print(f'Getting the maysnow for {i},{j}: it is equal to {maysnow}')
        climate_data['MaySnowyDays'].append(maysnow)
                #getting junhot
        junhot = newTable2[0]['HotDays'][5]
        print(f'Getting the junhotdays for {i},{j}: it is equal to {junhot}')
        climate_data['JunHotDays'].append(junhot)
        #getting janfreezingdays
        junfreezing = newTable2[0]['FreezingDays'][5]
        print(f'Getting the junfreezing for {i},{j}: it is equal to {junfreezing}')
        climate_data['JunFreezingDays'].append(junfreezing)
        #getting janrain
        junrain = newTable2[0]['RainyDays'][5]
        print(f'Getting the junrain for {i},{j}: it is equal to {junrain}')
        climate_data['JunRainyDays'].append(junrain)
        #getting jansnow
        junsnow = newTable2[0]['SnowyDays'][5]
        print(f'Getting the junsnow for {i},{j}: it is equal to {junsnow}')
        climate_data['JunSnowyDays'].append(junsnow)
                #getting julhot
        julhot = newTable2[0]['HotDays'][6]
        print(f'Getting the julhotdays for {i},{j}: it is equal to {julhot}')
        climate_data['JulHotDays'].append(julhot)
        #getting janfreezingdays
        julfreezing = newTable2[0]['FreezingDays'][6]
        print(f'Getting the julfreezing for {i},{j}: it is equal to {julfreezing}')
        climate_data['JulFreezingDays'].append(julfreezing)
        #getting janrain
        julrain = newTable2[0]['RainyDays'][6]
        print(f'Getting the julrain for {i},{j}: it is equal to {julrain}')
        climate_data['JulRainyDays'].append(julrain)
        #getting jansnow
        julsnow = newTable2[0]['SnowyDays'][6]
        print(f'Getting the julsnow for {i},{j}: it is equal to {julsnow}')
        climate_data['JulSnowyDays'].append(julsnow)
                #getting aughot
        aughot = newTable2[0]['HotDays'][7]
        print(f'Getting the aughotdays for {i},{j}: it is equal to {aughot}')
        climate_data['AugHotDays'].append(aughot)
        #getting janfreezingdays
        augfreezing = newTable2[0]['FreezingDays'][7]
        print(f'Getting the augfreezing for {i},{j}: it is equal to {augfreezing}')
        climate_data['AugFreezingDays'].append(augfreezing)
        #getting janrain
        augrain = newTable2[0]['RainyDays'][7]
        print(f'Getting the augrain for {i},{j}: it is equal to {augrain}')
        climate_data['AugRainyDays'].append(augrain)
        #getting jansnow
        augsnow = newTable2[0]['SnowyDays'][7]
        print(f'Getting the augsnow for {i},{j}: it is equal to {augsnow}')
        climate_data['AugSnowyDays'].append(julsnow)
                #getting sephot
        sephot = newTable2[0]['HotDays'][8]
        print(f'Getting the sephotdays for {i},{j}: it is equal to {sephot}')
        climate_data['SepHotDays'].append(sephot)
        #getting janfreezingdays
        sepfreezing = newTable2[0]['FreezingDays'][8]
        print(f'Getting the sepfreezing for {i},{j}: it is equal to {sepfreezing}')
        climate_data['SepFreezingDays'].append(sepfreezing)
        #getting janrain
        seprain = newTable2[0]['RainyDays'][8]
        print(f'Getting the seprain for {i},{j}: it is equal to {seprain}')
        climate_data['SepRainyDays'].append(seprain)
        #getting jansnow
        sepsnow = newTable2[0]['SnowyDays'][8]
        print(f'Getting the sepsnow for {i},{j}: it is equal to {sepsnow}')
        climate_data['SepSnowyDays'].append(sepsnow)
                        #getting octhot
        octhot = newTable2[0]['HotDays'][9]
        print(f'Getting the octhotdays for {i},{j}: it is equal to {octhot}')
        climate_data['OctHotDays'].append(octhot)
        #getting janfreezingdays
        octfreezing = newTable2[0]['FreezingDays'][9]
        print(f'Getting the octfreezing for {i},{j}: it is equal to {octfreezing}')
        climate_data['OctFreezingDays'].append(octfreezing)
        #getting janrain
        octrain = newTable2[0]['RainyDays'][9]
        print(f'Getting the octrain for {i},{j}: it is equal to {octrain}')
        climate_data['OctRainyDays'].append(octrain)
        #getting jansnow
        octsnow = newTable2[0]['SnowyDays'][9]
        print(f'Getting the octsnow for {i},{j}: it is equal to {octsnow}')
        climate_data['OctSnowyDays'].append(octsnow)
                                #getting novhot
        novhot = newTable2[0]['HotDays'][10]
        print(f'Getting the novhotdays for {i},{j}: it is equal to {novhot}')
        climate_data['NovHotDays'].append(novhot)
        #getting janfreezingdays
        novfreezing = newTable2[0]['FreezingDays'][10]
        print(f'Getting the novfreezing for {i},{j}: it is equal to {novfreezing}')
        climate_data['NovFreezingDays'].append(novfreezing)
        #getting janrain
        novrain = newTable2[0]['RainyDays'][10]
        print(f'Getting the novrain for {i},{j}: it is equal to {novrain}')
        climate_data['NovRainyDays'].append(novrain)
        #getting jansnow
        novsnow = newTable2[0]['SnowyDays'][10]
        print(f'Getting the novsnow for {i},{j}: it is equal to {novsnow}')
        climate_data['NovSnowyDays'].append(novsnow)
            #getting dechot
        dechot = newTable2[0]['HotDays'][11]
        print(f'Getting the dechotdays for {i},{j}: it is equal to {dechot}')
        climate_data['DecHotDays'].append(dechot)
        #getting janfreezingdays
        decfreezing = newTable2[0]['FreezingDays'][11]
        print(f'Getting the decfreezing for {i},{j}: it is equal to {decfreezing}')
        climate_data['DecFreezingDays'].append(decfreezing)
        #getting janrain
        decrain = newTable2[0]['RainyDays'][11]
        print(f'Getting the decrain for {i},{j}: it is equal to {decrain}')
        climate_data['DecRainyDays'].append(decrain)
        driver.quit()
        
    except IndexError or KeyError:
        print(f'server issue with {i},{j} right now')
        climate_data['JanHigh'].append('server issue right now, maybe try later')
        climate_data['JanLow'].append('server issue right now, maybe try later')
        climate_data['FebHigh'].append('server issue right now, maybe try later')
        climate_data['FebLow'].append('server issue right now, maybe try later')
        climate_data['MarHigh'].append('server issue right now, maybe try later')
        climate_data['MarLow'].append('server issue right now, maybe try later')
        climate_data['AprHigh'].append('server issue right now, maybe try later')
        climate_data['AprLow'].append('server issue right now, maybe try later')
        climate_data['MayHigh'].append('server issue right now, maybe try later')
        climate_data['MayLow'].append('server issue right now, maybe try later')
        climate_data['JunHigh'].append('server issue right now, maybe try later')
        climate_data['JunLow'].append('server issue right now, maybe try later')
        climate_data['JulHigh'].append('server issue right now, maybe try later')
        climate_data['JulLow'].append('server issue right now, maybe try later')
        climate_data['AugHigh'].append('server issue right now, maybe try later')
        climate_data['AugLow'].append('server issue right now, maybe try later')
        climate_data['SepHigh'].append('server issue right now, maybe try later')
        climate_data['SepLow'].append('server issue right now, maybe try later')
        climate_data['OctHigh'].append('server issue right now, maybe try later')
        climate_data['OctLow'].append('server issue right now, maybe try later')
        climate_data['NovHigh'].append('server issue right now, maybe try later')
        climate_data['NovLow'].append('server issue right now, maybe try later')
        climate_data['DecHigh'].append('server issue right now, maybe try later')
        climate_data['DecLow'].append('server issue right now, maybe try later')
        climate_data['JanHotDays'].append('server issue right now, maybe try later')
        climate_data['JanFreezingDays'].append('server issue right now, maybe try later')
        climate_data['JanRainyDays'].append('server issue right now, maybe try later')
        climate_data['JanSnowyDays'].append('server issue right now, maybe try later')
        climate_data['FebHotDays'].append('server issue right now, maybe try later')
        climate_data['FebFreezingDays'].append('server issue right now, maybe try later')
        climate_data['FebRainyDays'].append('server issue right now, maybe try later')
        climate_data['FebSnowyDays'].append('server issue right now, maybe try later')
        climate_data['MarHotDays'].append('server issue right now, maybe try later')
        climate_data['MarFreezingDays'].append('server issue right now, maybe try later')
        climate_data['MarRainyDays'].append('server issue right now, maybe try later')
        climate_data['MarSnowyDays'].append('server issue right now, maybe try later')
        climate_data['AprHotDays'].append('server issue right now, maybe try later')
        climate_data['AprFreezingDays'].append('server issue right now, maybe try later')
        climate_data['AprRainyDays'].append('server issue right now, maybe try later')
        climate_data['AprSnowyDays'].append('server issue right now, maybe try later')
        climate_data['MayHotDays'].append('server issue right now, maybe try later')
        climate_data['MayFreezingDays'].append('server issue right now, maybe try later')
        climate_data['MayRainyDays'].append('server issue right now, maybe try later')
        climate_data['MaySnowyDays'].append('server issue right now, maybe try later')
        climate_data['JunHotDays'].append('server issue right now, maybe try later')
        climate_data['JunFreezingDays'].append('server issue right now, maybe try later')
        climate_data['JunRainyDays'].append('server issue right now, maybe try later')
        climate_data['JunSnowyDays'].append('server issue right now, maybe try later')
        climate_data['JulHotDays'].append('server issue right now, maybe try later')
        climate_data['JulFreezingDays'].append('server issue right now, maybe try later')
        climate_data['JulRainyDays'].append('server issue right now, maybe try later')
        climate_data['JulSnowyDays'].append('server issue right now, maybe try later')
        climate_data['AugHotDays'].append('server issue right now, maybe try later')
        climate_data['AugFreezingDays'].append('server issue right now, maybe try later')
        climate_data['AugRainyDays'].append('server issue right now, maybe try later')
        climate_data['AugSnowyDays'].append('server issue right now, maybe try later')
        climate_data['SepHotDays'].append('server issue right now, maybe try later')
        climate_data['SepFreezingDays'].append('server issue right now, maybe try later')
        climate_data['SepRainyDays'].append('server issue right now, maybe try later')
        climate_data['SepSnowyDays'].append('server issue right now, maybe try later')
        climate_data['OctHotDays'].append('server issue right now, maybe try later')
        climate_data['OctFreezingDays'].append('server issue right now, maybe try later')
        climate_data['OctRainyDays'].append('server issue right now, maybe try later')
        climate_data['OctSnowyDays'].append('server issue right now, maybe try later')
        climate_data['NovHotDays'].append('server issue right now, maybe try later')
        climate_data['NovFreezingDays'].append('server issue right now, maybe try later')
        climate_data['NovRainyDays'].append('server issue right now, maybe try later')
        climate_data['NovSnowyDays'].append('server issue right now, maybe try later')
        climate_data['DecHotDays'].append('server issue right now, maybe try later')
        climate_data['DecFreezingDays'].append('server issue right now, maybe try later')
        climate_data['DecRainyDays'].append('server issue right now, maybe try later')
        climate_data['DecSnowyDays'].append('server issue right now, maybe try later')
        driver.quit()