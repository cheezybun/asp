import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from asp_intro import *

# Importing data
#eda_data = pd.read_csv(r'https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/notebook/airline_passenger_satisfaction.csv')
data = pd.read_csv(r'https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/notebook/airline_passenger_satisfaction.csv', index_col=False)
#df = pd.read_csv(r'https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/notebook/airline_passenger_satisfaction.csv')





def set_home():
    st.image("https://raw.githubusercontent.com/NikhilSingh45612/Airline_Passenger_Satisfaction/main/streamlit/images/pexels-pascal-renet-113017.jpg")
    st.write(intro, unsafe_allow_html=True)
    st.write(intro_herramientas_fuentes, unsafe_allow_html=True)


def set_data():
    st.title("DataFrame:")
    st.write("This dataset designed to understand the factors that lead a person to Satisfaction or Neutral (dissatisfied). By using classification models we will predict the probability of a passenger being satisfied or neutral, as well as interpreting affected factors on passenger comfort.")
    st.write(">***21287 entries | 15 columns***")
    st.dataframe(data)
    st.write(">***Let's analyize the dataframe.***")
    st.dataframe(data.describe())
    st.text("")
    st.title("*Satisfaction Distribution:*")
    st.write("By analyizing the satisfaction distribution we can understand that the 43.4% of the airline passengers were satisfied.")
    col1, col2 = st.columns(2)
    with col1:
        total = data['Satisfaction'].value_counts()
        fig1 = total.plot.pie(shadow=True, explode=(0, 0.1), startangle=0, autopct='%1.1f%%')
        labels = ['Not Satisfied','Satisfied']
        plt.legend(labels)
        plt.axis('equal')
        st.pyplot(fig1.figure)
    with col2:
        st.markdown(' ')
    st.write(">***Now we will analyize which factors/attributes effects these passenger satisfaction decisions.***")

def set_analysis():
    st.title("*Analyizing Passengers that were Satisfied:*")
    st.write("*We are focusing on passengers who were satisfied with the airline services, lets analyze which factors effects their decission.*")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1: Satisfaction Rating provided by the various Passengers On: ")
        st.markdown('Arrival Delay, Departure and Arrival Time Convenience, Ease of Online Booking AND Check-in Service.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/1.png")

    with col2:
        st.markdown("#### 2: Satisfaction Rating provided by the various Passengers On: ")
        st.markdown('Online Boarding, Gate Location, On-board Service AND Seat Comfort.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/2.png")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 3: Satisfaction Rating provided by the various Passengers On: ")
        st.markdown('Leg Room Service, Cleanliness, Food and Drink AND In-flight Service.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/3.png")

    with col2:
        st.markdown("#### 4: Satisfaction Rating provided by the Various Passengers On: ")
        st.markdown('In-flight Wifi Service, In-flight Entertainment AND Baggage Handling.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/4.png")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 5: Satisfaction Level of Passengers On:")
        st.markdown('Cleanliness.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/5.png")
    with col2:
        st.write("#### 6: Satisfaction Level of Passengers On:")
        st.markdown('Baggage Handling.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/6.png")

    col1, col2 = st.columns(2)
    with col1:
        st.write("#### 7: Satisfaction Level of Passengers On:")
        st.markdown('Food and Drink.')
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/7.png")

    with col2:
        st.markdown("#### 8: Satisfaction Indicator")
        st.markdown('Satisfied or Dissatisfied')
        ##st.write("*From this graph you can understand that most*")
        st.image("https://github.com/NikhilSingh45612/Airline_Passenger_Satisfaction/blob/d2ad0881103e3e5f314eea1cb1a4d7730f15573b/streamlit/images/8.png")

    col1, col2 = st.columns(2)

def set_classmod():
    st.title("*Classification Model*")
    st.write("We applied Four classification models, logistics regression, random forest model, Decision tree and Naive bayes . They gave a mean absolute error of ***0.186*** and ***0.074*** For the models. These results can be improved further by optimizing")
    st.subheader("*Prediction Using Logistic Regression Model*")
    st.write("##### Mean absolute error:")
    st.write("0.18627592512391125")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.subheader("*Prediction Using Random Forest*")
    st.write("##### Mean absolute error:")
    st.write("0.07434868389394159")

    st.subheader("*Prediction Using Decision Tree Classifier*")
    st.write("##### Accuracy:")
    st.write("93.10324915306436")

    st.subheader("*Prediction Using Naive Bayes*")
    st.write("##### Accuracy:")
    st.write("81.68982907299045")
