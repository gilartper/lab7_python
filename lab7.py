import json
import requests
print('Для завершения программы напишите exit')
key = '3de60ff699e5251a032caabd06626f8a'
while True:
    try:
        city_name = input('Введите название города: ')
        if city_name=='exit':
            break
        response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
        result = json.loads(response.text)
        temp = round(result.get('main').get('temp')-273 , 1)
        feel = round(result.get('main').get('feels_like')-273 , 1)
        pressure = result.get('main').get('pressure')
        humidity = result.get('main').get('humidity')
        print(f"Температура в городе {city_name}: {str(temp)+chr(8451)}, ощущается как {str(feel)+chr(8451)}")
        print(f"Давление:{pressure} мм рт ст, влажность:{humidity}%")
    except AttributeError:
        print('Такого города я не знаю :)')
        
    
