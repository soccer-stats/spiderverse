import streamlit as st
from service import data_loader
from service import polar_plot_service

st.title('Polar Bear')
# st.write("Soccer player performance visualization")
st.write("Created by [Roaming Playmaker](https://t.me/Ivan_xG) и [Футбол в цифрах](https://t.me/markstats)")

template = st.sidebar.selectbox('Template', ["forwards"])
template_to_position_mapping = {
    "forwards": {"filter": "FW", "default_player": "Lionel Messi"},
}
df = data_loader.load_data(template_to_position_mapping[template]["filter"])
player_names = df['Player'].unique().tolist()
player_name = st.sidebar.selectbox('Player', player_names,
                                   player_names.index(template_to_position_mapping[template]["default_player"]))

# st.write(df[df["Player"] == player_name])
st.pyplot(polar_plot_service.draw_polar(df, player_name, template))
