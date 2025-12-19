#API REST con FastAPI
from fastapi import FastAPI, HTTPException
from weather import get_temperature, get_all_temperatures, CITIES

app = FastAPI(title="Weather API")

@app.get("/temperatura/{city}")
def get_temp(city: str):
    data = get_temperature(city.lower())
    if not data:
        raise HTTPException(404, f"Ciudad no encontrada: {city}")
    return data #FastAPI ya convierte los JSON en dict de python

@app.get("/todas")
def get_all():
    return get_all_temperatures()

@app.get("/ciudades")
def get_cities():
    return {"ciudades": list(CITIES.keys())}
