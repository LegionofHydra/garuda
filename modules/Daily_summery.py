import requests
from xmljson import parker as bf
import xml.etree.ElementTree as ET
from datetime import date

def daily():
    URL =  'http://isc.sans.edu/api/dailysummary/2022-10-01/2022-10-01'

    response = requests.get(url=URL)


    g = bf.data(ET.fromstring(response.text))

    print("Date: " + g['daily']['date'])
    print("Records: " + str(g['daily']['records']))
    print("Sources: " + str(g['daily']['sources']))
    print("Targets: " + str(g['daily']['targets']))

