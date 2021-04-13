import streamlit as st
from service import data_loader
from service import polar_plot_service
import strings
import config

st.title(strings.get_string("app_title"))
st.write(strings.get_string("app_credentials"))

template = st.sidebar.selectbox('Position', ["Forwards", "Midfielders", "Defenders"])
df = data_loader.load_data(config.template_to_position_mapping[template]["filter"])
player_names = df['Player'].unique().tolist()
player_name = st.sidebar.selectbox(
    'Player', player_names,
    player_names.index(config.template_to_position_mapping[template]["default_player"]))
st.pyplot(polar_plot_service.draw_polar(df, player_name, template))
