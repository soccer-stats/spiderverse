import streamlit as st
from service import data_loader
from service import polar_plot_service

# 1. load data
df = data_loader.load_data()

# 2. set up application user interface
st.title('Spiderverse')
st.write("An application that helps creating radars for soccer players")

option = st.sidebar.selectbox('Chose the player', df['Player'])

st.write('Radar for: ', option)

st.write(df[df["Player"] == option])
st.pyplot(polar_plot_service.draw_polar(df, option, ["SCA90", "GCA90", "PassLive", "Drib"]))
