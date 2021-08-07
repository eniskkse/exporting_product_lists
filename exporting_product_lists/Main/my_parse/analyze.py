import xml.etree.ElementTree as ET
import pandas as pd
import xml.etree.ElementInclude as EI
from odoo import models
from . import API
import os
from urllib.request import urlopen
from os.path import isfile, join
from datetime import datetime
from odoo import models, fields, api, _




class Decider(models.Model):
    _name='analyze'

    def __init__(self,arg):
        
        print("1")
        self.arg=arg
        print(self.arg[-3:])
        print("2")
        if self.arg.endswith('csv'):
            self.convert_csv(self.arg)

        if self.arg.endswith('xml'):
            express=r"C:\Users\enisk\Desktop\src\Main\my_parse\{}".format(self.arg)
            self.convert_xml(express)
        try:
            if bool(urlopen(self.arg)):
                print(bool(urlopen(self.arg)),"booooooooolllllllllll")
                self.convert_fromurl(self.arg)
        except ValueError:
            #bu hata mesajı odoo içinde verilmeli
            print("beklenen tip gönderilmedi")


    def convert_csv(self,a):
        #csv dosası çevirm e
        print("csccscsc","csvden dönüyor")
        df=pd.read_csv(a)
        return df

    
    def convert_fromurl(self,url):
        #urli başka dosyadan(arayüzden olabilir) alcak parametre olarak
        print("urlden dönüyor")
        EI.default_loader(url, "xml")
        #pass


    def convert_xml(self,a):
        #gelen dosya doğrudan xml dosyası ise çalışacak
        print("xmlxmlx","burası xml kkısmı ")
        
        tree=ET.parse(a)
        root=tree.getroot()
        parser = ET.XMLPullParser(['start', 'end'])
        parser.feed('<mytag>sometext')
        list(parser.read_events())
        
        parser.feed(' more text</mytag>')
        for event, elem in parser.read_events():
            print(event)
            print(elem.tag, 'text=', elem.text)







#Decider("CustomersOrdersInNamespace.xml")
xmlns_ds = 'http://www.w3.org/2000/09/xmldsig#'


Decider("CustomersOrdersInNamespace.xml")
#onlyfiles = [f for f in listdir("C:/Users/enisk/Desktop/Yeni klasör/Test/pictures") if isfile(join("C:/Users/enisk/Desktop/Yeni klasör/Test/pictures", f))]
#onlyfiles.remove("calculate.py")
#onlyfiles.remove("convert.py")

