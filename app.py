import streamlit as st
from service import data_loader
from service import polar_plot_service
import strings
import config


def prepare_and_read_input_params(season_label_name, player_label_name, default_player="default_player"):
    season = st.sidebar.selectbox(
        season_label_name,
        ["2021-2022", "2020-2021", "2019-2020", "2018-2019", "2017-2018"])
    players_df = data_loader.load_data(
        config.template_to_position_mapping[season][template]["filter"],
        min_matches=config.season_to_min_num_matches[season], season=season)
    player_names = players_df['Player'].unique().tolist()
    name = st.sidebar.selectbox(
        player_label_name, player_names,
        player_names.index(config.template_to_position_mapping[season][template][default_player]))
    return season, players_df, name


st.title(strings.get_string("app_title"))
st.write(strings.get_string("app_credentials") + ", " + strings.get_string("donate"))

mode = st.sidebar.selectbox('Mode', ["Single player", "Compare players"])
template = st.sidebar.selectbox('Position', ["Forwards", "Midfielders", "Defenders"])

if mode == "Single player":
    season, df, player_name = prepare_and_read_input_params('Season', 'Player')
    st.pyplot(polar_plot_service.draw_polar(df, player_name, template, season))
else:
    season1, df1, player1_name = prepare_and_read_input_params(
        'Season 1', 'Player 1')
    season2, df2, player2_name = prepare_and_read_input_params(
        'Season 2', 'Player 2', 'default_compare_player')
    df = df1 if season1 == season2 else df1.append(df2)
    st.pyplot(polar_plot_service.draw_polar2(
        df, player1_name, player2_name, template, season1, season2))

st.write("'Pass - xPass completion %' - difference between ACTUAL and EXPECTED Pass Completion")
st.write("Expected Pass Completion calculated based on various passing metrics using linear regression")
st.write("The height of the dueling sectors is calculated using Bayesian estimator, which builds on successful actions throughout the season")
