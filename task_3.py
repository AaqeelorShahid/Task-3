from mongoengine import *
from mongoengine.document import Document, DynamicDocument
import csv
from mongoengine.fields import DateField, FloatField, IntField, ListField, StringField

connect ("Global-Warming_2")

class TempInfo (DynamicDocument):
    region = StringField()
    country = StringField()
    city = StringField()
    day = IntField()
    month = IntField()
    year = IntField()
    averageTemp =  FloatField()


    def getCSVData ():
        with open('city_temperature.csv', newline="", ) as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=',')
            line_count = 0
            for row in csv_reader:
                print (f"Progress - importing .... {line_count}")
                TempInfo(
                    region = row [0],
                    country = row [1],
                    city = row [3],
                    day = row [5],     
                    month = row[4],    
                    year = row [6],
                    averageTemp = row [7],
                ).save()
                line_count += 1
            return print("Done")

    meta = {
        "ordering" : ["-date"]
    }

TempInfo.getCSVData()