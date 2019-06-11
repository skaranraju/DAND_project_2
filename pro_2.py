import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def display (df):
    print(df.head())
    print(df.tail())

def boxp (df,var,tit):
    df[var].plot(kind = 'box',title = tit)

def scat (df,xv,yv,xl,yl,tit):
    plt.scatter(x = df[xv], y = df[yv],color = 'red', alpha=0.5)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(tit)
    plt.show()

def linec (df,xv,yv,xl,yl,tit):
    plt.plot(df_combined['year'],df_combined['life_expectancy'])
    plt.xlabel('year')
    plt.ylabel('life Expectancy')
    plt.title('life expectancy over years')
    plt.show()

# loading the datasets

df_life_expectancy = pd.read_csv('life_expectancy_years.csv')
df_income = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
df_death_rate = pd.read_csv('sp_dyn_cdrt_in.csv')
df_co2_emission = pd.read_csv('co2_emissions_tonnes_per_person.csv')

# checking the datasets

display(df_life_expectancy)
display(df_income)
display(df_death_rate)
display(df_co2_emission)

df_life_expectancy.info()
df_income.info()
df_death_rate.info()
df_co2_emission.info()

# Data Wrangling

# extracting stats of only india

df_life_expectancy = df_life_expectancy[df_life_expectancy['country'] == 'India']
df_income = df_income[df_income['country'] == 'India']
df_death_rate = df_death_rate[df_death_rate['country'] == 'India']
df_co2_emission = df_co2_emission[df_co2_emission['country'] == 'India']

display(df_life_expectancy)
display(df_income)
display(df_death_rate)
display(df_co2_emission)

# melting the dfs

df_life_expectancy = pd.melt(df_life_expectancy,id_vars=["country"],var_name="year",value_name="life_expectancy")
df_income = pd.melt(df_income,id_vars=["country"],var_name="year",value_name="income")
df_death_rate = pd.melt(df_death_rate,id_vars=["country"],var_name="year",value_name="death_rate")
df_co2_emission = pd.melt(df_co2_emission,id_vars=["country"],var_name="year",value_name="co2_emission")

display(df_life_expectancy)
display(df_income)
display(df_death_rate)
display(df_co2_emission)

# converting data type of year column from string to int

df_life_expectancy['year'] = df_life_expectancy['year'].astype(int)
df_income['year'] = df_income['year'].astype(int)
df_death_rate['year'] = df_death_rate['year'].astype(int)
df_co2_emission['year'] = df_co2_emission['year'].astype(int)

df_life_expectancy.info()

# leveling no. of years in all datasets from 1960 to 2014

df_life_expectancy = df_life_expectancy[(df_life_expectancy['year']>1959) & (df_life_expectancy['year']<2015)]
df_income = df_income[(df_income['year']>1959) & (df_income['year']<2015)]
df_death_rate = df_death_rate[(df_death_rate['year']>1959) & (df_death_rate['year']<2015)]
df_co2_emission = df_co2_emission[(df_co2_emission['year']>1959) & (df_co2_emission['year']<2015)]

display(df_life_expectancy)

df_life_expectancy.info()
df_income.info()
df_death_rate.info()
df_co2_emission.info()

df_life_expectancy.describe()
df_income.describe()
df_death_rate.describe()
df_co2_emission.describe()

# removing country column from all datasets

df_life_expectancy.drop(columns=['country'], inplace = True)
df_income.drop(columns=['country'], inplace = True)
df_death_rate.drop(columns=['country'], inplace = True)
df_co2_emission.drop(columns=['country'], inplace = True)

display(df_life_expectancy)

# merging all the datasets

df_combined = df_life_expectancy.merge(df_income, on='year', how='outer' )
df_combined = df_combined.merge(df_death_rate, on='year', how='outer' )
df_combined = df_combined.merge(df_co2_emission, on='year', how='outer' )

display(df_combined)

# save the cleaned dataset

df_combined.to_csv('combined_dataset.csv', index=False)

# analysis part

# box plot

boxp (df_combined,'life_expectancy','life expectancy')
boxp (df_combined,'income','income')
boxp (df_combined,'death_rate','death rate')
boxp (df_combined,'co2_emission','co2 emission')

# scatter plot

scat (df_combined,'income','life_expectancy','income','life expectancy','life expectancy vs income')
scat (df_combined,'death_rate','life_expectancy','death rate','life expectancy','life expectancy vs death rate')
scat (df_combined,'co2_emission','life_expectancy','co2 emission','life expectancy','life expectancy vs co2 emission')

# line chart over the years

linec (df_combined,'year','life_expectancy','year','life expectancy','life expectancy over years')
linec (df_combined,'year','income','year','income','income over years')
linec (df_combined,'year','death_rate','year','death rate','death rate over years')
linec (df_combined,'year','co2_emission','year','co2 emission','co2 emission over years')