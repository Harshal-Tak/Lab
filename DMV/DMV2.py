import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = '0bd28a89c65ba3b13dfa38bf638e99e6'

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print("Requesting URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving data")
        print(f"Status Code: {response.status_code}, Message: {response.json()}")
    

def parse_weather_data(data):
    if data:
        weather = {
            'Temperature': data['main']['temp'],
            'Humidity': data['main']['humidity'],
            'Wind Speed':data['wind']['speed'],
            'City':data['name'],
            'Country':data['sys']['country']
        }

        return weather
    
    return {}


cities = ['New York', 'London', 'Tokyo', 'Delhi']
weather_data = [parse_weather_data(get_weather_data(city)) for city in cities]

df = pd.DataFrame(weather_data)

df.head()

df.dropna(inplace=True)

avg_temp = df['Temperature'].mean()
avg_temp

plt.bar(df['City'],df['Temperature'],color='skyblue')

max_temp = df.groupby('City')['Temperature'].max()
max_temp


sns.heatmap(df[['Temperature', 'Humidity', 'Wind Speed']].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation between Temperature, Humidity, and Wind Speed")
plt.show()