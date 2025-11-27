import requests

city=input("Ingrese el nombre de la ciudad a la que desea consultar el clima: ").capitalize()

url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7a79dd3d5f62d67d5b7748d255209a2a&units=metric&lang=es"

response=requests.get(url)

data=response.json()

data_main=data["main"]
print(f"""
Los datos actuales para la ciudad de {city} son:
La temperatura actual es de: {data_main["temp"]:.1f}°C
La sensacion termica es de: {data_main['feels_like']:.1f} °C
La temperatura minima sera de: {data_main['temp_min']:.1f} °C
La temperatura maxima sera de: {data_main['temp_max']:.1f} °C
La humedad actual es de: {data_main['humidity']} %
Descripcion del clima es: {data['weather'][0]['description']}
""")

