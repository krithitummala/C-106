import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    temperature = []
    iceCreamSales = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            temperature.append(float(row["Temperature"]))
            iceCreamSales.append(float(row["Ice-cream Sales"]))
    return{
         "x" : temperature,
         "y" : iceCreamSales
    }

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between temperature and ice cream sales is",correlation[0,1])

def setup():
    data_path = "temp.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()
