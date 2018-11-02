from tkinter import *
from PIL import ImageTk, Image
import requests
import xmltodict


#returnt een lijst met alle vertrektijden als strings
def vertrekTijd(code):
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    vertrekXML = xmltodict.parse(response.text)
    vertrekList = []
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        str = vertrek['EindBestemming'] + ';'
        str += vertrek['VertrekTijd'][11:16] + ';'
        str += vertrek['TreinSoort'] + ';'
        #voor het geval er geen spoor bekend is
        try:
            str += vertrek['VertrekSpoor']['#text']
        except:
            str += 'onbekend'
        vertrekList.append(str)
    return vertrekList

#reisinformatie Utrecht
def reisInfoUtrecht():
    reisInformatie('ut')



#inloggegevens om bij de NS api te kunnen
inlogGegevens = ('akram.tarioui@student.hu.nl', 'zmIyWhZ3ycFGkRYVAWPFV9KYQZYwnZbuBuYSEsfAkkMI6oAUAnjCfg')
response = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=inlogGegevens)
