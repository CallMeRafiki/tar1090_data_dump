import requests
from time import gmtime, strftime, sleep
import os
import json

intv = 60

while True:
    daySaved = strftime("%d %b %Y", gmtime());
    timeSaved = strftime("%H%M", gmtime());
    
    if not os.path.exists(daySaved):
        os.mkdir("./" + daySaved);
    
    url = "http://adsbexchange.local/tar1090/data/aircraft.json"
    r = requests.get(url)
    
    data = r.json()
    with open('./'+daySaved+'/'+timeSaved+'.json', 'w') as f:
        json.dump(data, f)
        
    sleep(intv)
