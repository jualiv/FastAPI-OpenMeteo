# Lógica 
import requests

#diccionario con las coordenadas de cada ciudad (requerido para OpenMeteo)
CITIES = {
    "madrid":    {"lat": 40.4168, "lon": -3.7038},
    "barcelona": {"lat": 41.3874, "lon": 2.1686},
    "paris":     {"lat": 48.8566, "lon": 2.3522},
    "londres":   {"lat": 51.5074, "lon": -0.1278},
}

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def get_temperature(city_key: str):
    """Obtiene temperatura actual de una ciudad. Devuelve dict o None si error""" #documentación docstring
    if city_key not in CITIES:
        return None
    
    coords = CITIES[city_key]
    params = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "current": ["temperature_2m"],
        "timezone": "Europe/Madrid"
    }
    
    try:
        #GET
        response = requests.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()
        data = response.json() # ← aquí pasa de JSON (texto HTTP) a dict de Python
        current = data.get("current", {})
        temp = current.get("temperature_2m")
        
        if temp is None:
            return None
            
        return {
            "ciudad": city_key.title(),
            "temperatura": round(temp, 1),
            "unidad": "°C",
            "actualizado": current.get("time", "")
        }
    except:
        return None

def get_all_temperatures():
    """Obtiene temperaturas de todas las ciudades""" #documentación docstring
    return {city: get_temperature(city) for city in CITIES}
