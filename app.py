import streamlit as st
from service import data_loader
from service import polar_plot_service

st.title('Polar Bear')
# st.write("Soccer player performance visualization")
st.write("Created by [Roaming Playmaker](https://t.me/Ivan_xG) и [Футбол в цифрах](https://t.me/markstats)")

template = st.sidebar.selectbox('Position', ["Forwards", "Midfielders", "Defenders"])
template_to_position_mapping = {
    "Forwards": {"filter": "FW", "default_player": "Lionel Messi"},
    "Midfielders": {"filter": "MF", "default_player": "Kevin De Bruyne"},
    "Defenders": {"filter": "DF", "default_player": "Juan Cuadrado"},
}
df = data_loader.load_data(template_to_position_mapping[template]["filter"])
player_names = df['Player'].unique().tolist()
player_name = st.sidebar.selectbox('Player', player_names,
                                   player_names.index(template_to_position_mapping[template]["default_player"]))

# st.write(df[df["Player"] == player_name])
st.pyplot(polar_plot_service.draw_polar(df, player_name, template))
