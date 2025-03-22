import requests
import datetime

def get_iss_position():
    """Получает текущие координаты МКС и время обновления"""
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        
        return {
            'latitude': data['iss_position']['latitude'],
            'longitude': data['iss_position']['longitude'],
            'timestamp': datetime.datetime.fromtimestamp(data['timestamp'])
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка получения данных МКС: {e}")

def get_people_in_space():
    """Получает количество людей в космосе"""
    url = "http://api.open-notify.org/astros.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'number': data['number'],
            'people': data['people']  # Дополнительная информация о космонавтах
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка получения данных о космонавтах: {e}")


try:
    print('Для выхода напишите exit')
    while True:
        a=input("Для того чтобы узнать положение МКС, нажмите 1, чтобы узнать людей в космосе нажмите 2:")
        if a=='1':
            iss_data = get_iss_position()
            print("\nМеждународная космическая станция:")
            print(f"Время обновления: {iss_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S UTC')}")
            print(f"Текущие координаты:")
            print(f"Широта: {iss_data['latitude']}")
            print(f"Долгота: {iss_data['longitude']}")
        
        elif a=='2':
            people_data = get_people_in_space()
            print("\nЛюди в космосе:")
            print(f"Всего человек: {people_data['number']}")
            print("\nСписок космонавтов и их корабли:")
            for person in people_data['people']:
                print(f"{person['name']} — {person['craft']}")
        elif a=='exit':
            break
        else:
            print('не понял тебя')

except Exception as e:
    print(f"\nПроизошла ошибка: {e}") 