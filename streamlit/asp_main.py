import streamlit as st
from asp_functions import *

st.sidebar.image('https://raw.githubusercontent.com/NikhilSingh45612/Airline_Passenger_Satisfaction/main/streamlit/images/download.jpg', width=250)
st.sidebar.header('Airline Satisfaction Analysis')
st.sidebar.markdown('Prediction of passenger satisfaction')


menu = st.sidebar.radio(
    "Menu:",
    ("Intro", "Data", "Analysis", "Classification Model"),
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Project Submitted By: Nikhil Kumar')
st.sidebar.write('Github Repositories:')
st.sidebar.write('[Nikhil Github Repository Link]()')

if menu == 'Intro':
    set_home()
elif menu == 'Data':
    set_data()
elif menu == 'Analysis':
    set_analysis()
elif menu == 'Classification Model':
    set_classmod()