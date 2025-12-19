#Interfaz gráfica Streamlit
import streamlit as st
from weather import get_temperature, get_all_temperatures

st.set_page_config(page_title="🌤️ Temperaturas", layout="wide")
st.title("Ivan - FastAPI - OpenMeteo") 

cols = st.columns(4)
for i, city in enumerate(get_all_temperatures().keys()):
    with cols[i]:
        st.subheader(f"**{city.title()}**")
        if st.button(f"🔄", key=f"btn_{city}"):
            st.cache_data.clear()
            
        @st.cache_data(ttl=120)
        def cached_temp(city_key):
            return get_temperature(city_key)
        
        data = cached_temp(city)
        if data:
            emoji = "🥶" if data["temperatura"] < 5 else "🧊" if data["temperatura"] < 10 else "🌤️" if data["temperatura"] < 20 else "☀️"
            st.metric("Temperatura", f"{data['temperatura']}°C {emoji}", delta=None)
            st.caption(data['actualizado'])
        else:
            st.error("❌ Error")
