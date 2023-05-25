import requests
city = "Magas,RU"
appid = "ba436182fe02ac5a3196306dd4da2de2"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
      params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура ", data['main']['temp_max'])
print("Скорость ветра", data['wind']['speed'])
print("Видимость", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз на неделю:")
for i in data['list']:
      print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
            "> \r\nПогодные условия <", i['weather'][0]['description'], ">", " \r\nСкорость ветра < > ")
      print("Скорость ветра <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
      print("_____________________________________")
