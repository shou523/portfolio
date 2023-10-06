# -*- coding: utf-8 -*-
"""Python_演習.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Roe0Wnn6okeNbaCIAnOuFb1kFOyEgwai
"""

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/データセット/I社/data.csv")

print('データのデータ数は{}、変数は{}種類です。'.format(df.shape[0], df.shape[1]))

print(df.info())

df.head(10)

df.isnull().sum()

f,ax=plt.subplots(1,2,figsize=(18,8))
df['Attrition'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Attrition')
ax[0].set_ylabel('')
sns.countplot(x=df['Attrition'],ax=ax[1])
ax[1].set_title('Attrition')
plt.show()

df.columns[df.dtypes.values == "object"]

categ_nominal =['Attrition', 'BusinessTravel', 'Department', 'EducationField', 'Gender',
       'JobRole', 'MaritalStatus', 'Over18', 'OverTime', 'HowToEmploy']

for i in categ_nominal:
    df = pd.concat([df, pd.get_dummies(df[i], prefix=i, dummy_na=True)], sort=False, axis=1)
df = df.drop(categ_nominal, axis=1)
df.info()

df.head(1)

import re

new_names = {col: re.sub(r'[^A-Za-z0-9_]+', '', col) for col in df.columns}
df.rename(columns=new_names, inplace=True)
df.head(2)

from sklearn.model_selection import train_test_split
import lightgbm as lgb

from sklearn.model_selection import train_test_split
import lightgbm as lgb

X = df.drop('Attrition_Yes',axis=1)
y = df['Attrition_Yes'] # 目的変数
# トレーニングデータ,テストデータの分割
X_train, X_valid, y_train, y_valid = train_test_split(X, y,test_size=0.2, random_state=0)

# 学習に使用するデータを設定
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_valid, y_valid, reference=lgb_train)

# パラメータ
params = {
    'objective': 'binary',
    'metric': 'auc',
    'verbosity': -1,
}


# モデルの学習
model = lgb.train(params,
                  train_set=lgb_train, # トレーニングデータの指定
                  valid_sets=lgb_eval, # 検証データの指定
                  )

# テストデータの予測
y_pred = model.predict(X_valid)

lgb.plot_importance(model, height=0.5, figsize=(30,40))

df.groupby(["Attrition_Yes"])["DailyAchievement"].mean()

df.groupby(["Attrition_Yes"])["DailyAchievement"].median()

sns.barplot(x='Attrition_Yes', y='DailyAchievement', data=df)

df.groupby('Attrition_Yes')['DailyAchievement'].plot.hist(bins=20, alpha=0.5, legend=True)

from scipy import stats
df_copy=df.copy()
df_copy.dropna(inplace=True)
s, pvalue = stats.mannwhitneyu(df_copy[df_copy["Attrition_Yes"]==1]["DailyAchievement"]
                , df_copy[df_copy["Attrition_Yes"]==0]["DailyAchievement"]
                ,alternative='two-sided')
pvalue < 0.05

df.groupby(["Attrition_Yes"])["Age"].mean()

df.groupby(["Attrition_Yes"])["Age"].median()

sns.barplot(x='Attrition_Yes', y='Age', data=df)

df.groupby(["Attrition_Yes"])["Age"].plot.hist(bins=20, alpha=0.5, legend=True)

s, pvalue = stats.mannwhitneyu(df[df["Attrition_Yes"]==1]["HourlyAchievement"]
                , df[df["Attrition_Yes"]==0]["HourlyAchievement"]
                ,alternative='two-sided')
pvalue < 0.05

df.groupby(["Attrition_Yes"])["RemoteWork"].mean()

df.groupby(["Attrition_Yes"])["RemoteWork"].median()

sns.barplot(x='Attrition_Yes', y='RemoteWork', data=df)

df.groupby(["Attrition_Yes"])["RemoteWork"].plot.hist(bins=20, alpha=0.5, legend=True)

s, pvalue = stats.mannwhitneyu(df[df["Attrition_Yes"]==1]["RemoteWork"]
                , df[df["Attrition_Yes"]==0]["RemoteWork"]
                ,alternative='two-sided')
pvalue < 0.05

df.groupby(["Attrition_Yes"])["Gender_Female"].mean()

df.groupby(["Attrition_Yes"])["Gender_Female"].median()

sns.barplot(x='Attrition_Yes', y='Gender_Female', data=df)

df.groupby(["Attrition_Yes"])["Gender_Female"].plot.hist(bins=20, alpha=0.5, legend=True)

s, pvalue = stats.mannwhitneyu(df[df["Attrition_Yes"]==1]["Gender_Female"]
                , df[df["Attrition_Yes"]==0]["Gender_Female"]
                ,alternative='two-sided')
pvalue < 0.05

df.groupby(["Attrition_Yes"])["Gender_Male"].mean()

df.groupby(["Attrition_Yes"])["Gender_Male"].median()

sns.barplot(x='Attrition_Yes', y='Gender_Male', data=df)

df.groupby(["Attrition_Yes"])["Gender_Male"].plot.hist(bins=20, alpha=0.5, legend=True)

df['All_Gender']=df['Gender_Female']/df['MaritalStatus_Married']
df.groupby(["Attrition_Yes"])["All_Gender"].mean()

df.groupby(["Attrition_Yes"])["All_Gender"].median()

sns.barplot(x='Attrition_Yes', y='All_Gender', data=df)

df.groupby('Attrition_Yes')['All_Gender'].plot.hist(bins=20, alpha=0.5, legend=True)

df.groupby(["Attrition_Yes"])["MaritalStatus_Single"].mean()

df.groupby(["Attrition_Yes"])["MaritalStatus_Single"].median()

sns.barplot(x='Attrition_Yes', y='MaritalStatus_Single', data=df)

df.groupby(["Attrition_Yes"])["MaritalStatus_Single"].plot.hist(bins=20, alpha=0.5, legend=True)

df.groupby(["Attrition_Yes"])["MaritalStatus_Married"].mean()

df.groupby(["Attrition_Yes"])["MaritalStatus_Married"].median()

sns.barplot(x='Attrition_Yes', y='MaritalStatus_Married', data=df)

df.groupby(["Attrition_Yes"])["MaritalStatus_Married"].plot.hist(bins=20, alpha=0.5, legend=True)