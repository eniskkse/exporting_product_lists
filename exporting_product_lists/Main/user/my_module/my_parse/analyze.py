import xml.etree.ElementTree as ET
import pandas as pd



class Decider():

    def __init__(self,arg):
        
        print("1")
        self.arg=arg
        print(self.arg[-3:])
        print("2")
        if self.arg[-3:]=='csv':
            self.convert_csv()

        if self.arg[-3:]=='xml':
            self.convert_xml(self.arg)

    def convert_csv(self):
        df=pd.read_csv(filepath_or_buffer)
        return df

        


    def convert_xml(self,a):
        tree=ET.parse(a)
        root=tree.getroot()
        parser = ET.XMLPullParser(['start', 'end'])
        parser.feed('<mytag>sometext')
        list(parser.read_events())
        
        parser.feed(' more text</mytag>')
        for event, elem in parser.read_events():
            print(event)
            print(elem.tag, 'text=', elem.text)







Decider("CustomersOrdersInNamespace.xml")


