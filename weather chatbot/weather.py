import requests

def weath(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=567538a78f3c09e3c6582629248e66f6&q='
    url = api_address + city
    json_data = requests.get(url).json()
    temp = json_data['main']['temp']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    s1 = 'Temparature : '+str(temp)+'\nPressure : '+str(pressure)+'\nHumidity : '+str(humidity)
    return {'fulfillmentText': s1}

