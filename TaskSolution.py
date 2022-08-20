"""
1) Read Airpassanger.csv file into python
2) Create a dropdown for year st.selectbox()
3) Show Table of values for that year only (hint: st.table(df))
"""

import streamlit as st
import pandas as pd


def main():
    st.title("Air Passengers CSV")
    
    data = pd.read_csv("AirPassengers.csv")
    data['Year'] = data['Month'].apply(lambda x: x.split('-')[0])
    year = st.selectbox('Select Year',data['Year'].unique())
    button = st.button('Show Results')
    if button:
        subset = data[data['Year']==year]
        st.table(subset)

if __name__ == '__main__':
    main()
