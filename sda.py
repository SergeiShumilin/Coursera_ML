import pandas as pd
import matplotlib.pyplot as plt
import re

def count_MenWomen(df,whom):
    return  len(df[df['Sex']==whom])

def count_survivers(df):
    return (len(df[df['Survived']==1])/len(df))*100

def first_class_perc(df):
    return int((len(df[df['Pclass']==1])/len(df))*100)

def age_mean_median(df):
    return df['Age'].mean(),df['Age'].median()

def pearson_coeff(df):
    return df['SibSp'].corr(df['Parch'])

 

def my_interest(df):
    mens_perc = len(df[df['Sex']=='male'])
    men_died = len(df[(df['Sex']=='male') & (df['Survived']==1)])
    a = df[(df['Sex']=='male') & (df['Survived']==1)]
    print('Cредний возраст выжившего мужчины: ' + str(a['Age'].mean()))
    women_perc = len(df[df['Sex'] == 'female'])
    women_died = len(df[(df['Sex'] == 'female') & (df['Survived'] == 1)])
    return men_died/mens_perc, women_died/women_perc

def print_answers():
    df = pd.read_csv('titanic.csv',index_col='PassengerId')
    print('Число мужчин: ' + str(count_MenWomen(df,'male')))
    print('Число женщин: ' + str(count_MenWomen(df,'female')))
    print('Процент выживших: ' + str(count_survivers(df)))
    print('Процент пассажиров первого класса: ' + str(first_class_perc(df)))
    print('Среднее и медиана возраста: ' + str(age_mean_median(df)[0]) + ' и ' + str(age_mean_median(df)[1]))
    print('Коэффициент Пирсона между... ' + str(pearson_coeff(df)))


def plot_corr(df):
    sibl = df['SibSp']
    parch = df['Parch']
    plt.scatter(sibl,parch)
    plt.show()



print_answers()