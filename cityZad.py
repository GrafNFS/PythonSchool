from tkinter import *
from opencage.geocoder import OpenCageGeocode
import webbrowser

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')

        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components'].get('country', 'Страна не определена')
            valute = results[0]['annotations']['currency'].get('name', 'Валюта не определена')
            region = results[0]['components'].get('state', 'Регион не определен')

            # Получаем URL для OpenStreetMap
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            return {
                "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nВалюта: {valute}\nРегион: {region}",
                "map_url": osm_url
            }
        else:
            return {"coordinates": "Город не найден", "map_url": None}
    except Exception as e:
        return {"coordinates": f"Ошибка: {e}", "map_url": None}

def show_coordinates(event=None):
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=result["coordinates"])
    global map_url
    map_url = result["map_url"]

def show_map():
    if map_url:
        webbrowser.open(map_url)

def clear_enr():
    global map_url
    entry.delete(0, END)
    label.config(text="Введите город и нажмите Поиск")
    map_url = None

if __name__ == "__main__":
    window = Tk()
    window.title("Поиск координат города")

    key = 'c7a3a784ed1e49aea74870e1a1106753'
    map_url = None

    entry = Entry()
    entry.pack()
    entry.bind("<Return>", show_coordinates)

    button = Button(text="Поиск", command=show_coordinates)
    button.pack()

    label = Label(text="Введите город и нажмите Поиск")
    label.pack()

    map_btn = Button(text="Показать карту", command=show_map)
    map_btn.pack()

    clear_btn = Button(text="Очистить", command=clear_enr)
    clear_btn.pack()

    window.mainloop()