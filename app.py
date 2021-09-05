import streamlit as st
import streamlit_analytics
from service import data_loader
from service import polar_plot_service
import strings
import config

with streamlit_analytics.track():
    st.title(strings.get_string("app_title"))
    st.write(strings.get_string("app_credentials") + ", " + strings.get_string("donate"))

    mode = st.sidebar.selectbox('Mode', ["Single player", "Compare players"])
    season = st.sidebar.selectbox('Season', ["2021-2022", "2020-2021"])
    template = st.sidebar.selectbox('Position', ["Forwards", "Midfielders", "Defenders"])
    df = data_loader.load_data(config.template_to_position_mapping[season][template]["filter"],
                               min_matches=config.season_to_min_num_matches[season], season=season)
    player_names = df['Player'].unique().tolist()
    if mode == "Single player":
        player_name = st.sidebar.selectbox(
            'Player', player_names,
            player_names.index(config.template_to_position_mapping[season][template]["default_player"]))
        st.pyplot(polar_plot_service.draw_polar(df, player_name, template, season))
    else:
        player1_name = st.sidebar.selectbox(
            'Player 1', player_names,
            player_names.index(config.template_to_position_mapping[season][template]["default_player"]))
        player2_name = st.sidebar.selectbox(
            'Player 2', player_names,
            player_names.index(config.template_to_position_mapping[season][template]["default_compare_player"]))
        st.pyplot(polar_plot_service.draw_polar2(df, player1_name, player2_name, template, season))
