import numpy as np
import pandas as pd

def loadfile():
    path=".\\tasks\\files\\Titanic-Dataset.csv"  
    global df
    df=pd.read_csv(path)
    print(df)

def dropping():
    global df
    print(df.isnull().sum())
    print("here we see that age column has 177 missing values and that there were 687 passengers without a recorded cabin")
    print("we shall drop the column cabin")
    df_dropped=df.drop(columns=['Cabin'])
    print("also dropping other unnecessary columns")
    df_dropped = df_dropped.drop(columns=['SibSp', 'Parch', 'Ticket', 'Pclass'])  
    print(df_dropped)
    df=df_dropped

def imputation():
    print("for filling the missing values in age we can use mean or median")
    meanage=df['Age'].mean()
    medianage=df['Age'].median()
    print("mean will be:",meanage)  
    print("median will be:",medianage)
    print("since mean and median are almost equal we can use w=either but in case of outliers median is preferred")
    df["Age"] = df["Age"].fillna(medianage)  
    print("for filling the missing values in Embarked we shall use mode")  
    modeembarked=df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(modeembarked)
    print(df)

loadfile()
dropping()
imputation()
print("finally as seen below we dont have any missing values")
print(df.isnull().sum())
