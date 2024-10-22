import numpy as np
import pandas as pd
import json as json


def menu():
    print("List of files that you can upload")
    print("1. CSV") 
    print("2. JSON")  
    print("3. TXT")  
    print("4. XLSX") 
    x= input("Enter which file you want to upload: ")
    return int(x)
def loadfile():
    file_type=menu()
    file_path=".\\tasks\\files"
    df=None
    if file_type==1:
        file_path+="\\csvfile.csv"
        df=pd.read_csv(file_path,encoding='latin1')
    elif file_type==2:
        file_path+="\\jsonfile.json"
        with open(file_path,'r') as jsonfile:
            df=json.load(jsonfile)
    elif file_type==3:
        file_path+="\\txtfile.txt"
        with open(file_path,'r') as txtfile:
            df=txtfile.read()
    elif file_type==4:
        file_path+="\\excelfile.xlsx"
        df=pd.read_excel(file_path)
    else:
        print("invalid file type")
    return df

dataframe=loadfile()
print(dataframe)
        

