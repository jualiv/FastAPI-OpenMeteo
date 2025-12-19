# FastAPI-OpenMeteo

Aplicación en **Python** con **FastAPI** que consume la API de Open‑Meteo para obtener la temperatura actual de cuatro ciudades europeas y la muestra en un dashboard con Streamlit. 

## Tecnologías

- FastAPI  
- Uvicorn  -> servidor
- Streamlit  -> UI
- Open‑Meteo API 

## Puesta en marcha

### 1. Crear entorno e instalar dependencias

pip install -r requirements.txt

### 2. Levantar la API (FastAPI)

uvicorn  main:app --reload --host 0.0.0.0 --port 8000

### 3. Ejecutar el dashboard (Streamlit)

En otra terminal (con el servidor levantado): 
streamlit run dashboard.py