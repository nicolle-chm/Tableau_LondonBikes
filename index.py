import pandas as pd
import numpy as np 

bikes = pd.read_csv("london_merged.csv")

#Checking data
bikes.info()
print(bikes.shape)
print(bikes)

print(bikes.weather_code.value_counts())
print(bikes.season.value_counts())

#Renaming the columns
dictionary = {
    'timestamp' : 'time',
    'cnt' :'count',
    't1' :'temp_real_C',
    't2' :'temp_feels_like_C',
    'hum' :'humidity_perc',
    'wind_speed' :'wind_speed_kph',
    'weather_code' :'weather',
    'is_holiday' :'is_holiday',
    'is_weekend' :'is_weekend',
    'season' :'season'
    }

bikes.rename(dictionary, axis=1, inplace=True)

#humidity in percentage
bikes.humidity_perc = bikes.humidity_perc / 100

#Creating season and weather dictionary to map the integers to the actual written values
season_dic = {
  '0.0' : 'spring',
  '1.0' : 'summer',
  '2.0' : 'autumn',
  '3.0' : 'winter'
 }

weather_dic = {
    '1.0' : 'Clear',
    '2.0' : 'Scattered Clouds',
    '3.0' : 'Broken Clouds',
    '4.0' : 'Cloudy',
    '7.0' : 'Rain',
    '10.0' : 'Rain with Thunderstorm',
    '26.0' : 'Snowfall'
}

bikes.season = bikes.season.astype('str')
bikes.season = bikes.season.map(season_dic)

bikes.weather = bikes.weather.astype('str')
bikes.weather = bikes.weather.map(weather_dic)

#Checking
print(bikes.head)

#Export
bikes.to_excel('london_bikes_cleaned.xlsx', sheet_name='Data')