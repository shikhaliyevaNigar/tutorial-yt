# -*- coding: utf-8 -*-
"""Covid-19deaths.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oIjcODpo0tswuCNb3REtooSCsWbM2CRq
"""

import plotly
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('time_series_covid19_deaths_global.csv')
df.head()

df.info()

df.describe()

covid_df_last_week_columns =df.iloc[:,-8:].columns.to_list() 
covid_df_last_week_by_countries = df.iloc[:,[1]+[*range(-8,0,1)]] 
topdata=covid_df_last_week_by_countries.nlargest(n=10, columns=['3/29/22'])
print(topdata)

topdata.plot(x="Country/Region", y=["3/30/22", "3/31/22", "4/1/22","4/2/22","4/3/22","4/4/22","4/5/22"], kind="bar")