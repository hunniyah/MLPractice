import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def loadfile():
    path=".\\tasks\\files\\Titanic-Dataset.csv"  
    global df
    df=pd.read_csv(path)
    print(df)
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

def Zscore(column):
    mean=df[column].mean()
    std_dev=df[column].std()
    z_scores=[(x-mean)/std_dev for x in df[column]]
    print("genrally the threshhold of z score is +3 or -3")
    threshhold=3
    return df[np.abs(z_scores)>threshhold]

def Zscoredetection():
    print("we will perform out outlier detetction on the columns age and fare")
    print("the outlier os Age column are ")
    print(Zscore("Age"))
    print("the outlier of fare column are ")
    print(Zscore("Fare"))

def IQR(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    #we say any data below or above 0.5*IQR is outlier so
    lower_bound = Q1 - 0.5 * IQR
    upper_bound = Q3 + 0.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

def IQRdetection():
    print("the outlier os Age column are ")
    print(IQR("Age"))
    print("the outlier of fare column are ")
    print(IQR("Fare"))

def boxplot(column):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.show()
    outliers=IQR(column)
    print("Outliers in {column}: ")
    print(outliers[[column]])



loadfile()
imputation()
Zscoredetection()
IQRdetection()
boxplot("Age")