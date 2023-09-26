import streamlit as st 
from  notebooks.sentimentl_analysis import get_analysis


score = get_analysis( st.text_input("Please Rate Our Servics  >>"))


if score == 0 :
    st.write("# Normal")
elif score['neg'] != 0 :
    st.write("# Negative")
elif score['pos'] != 0 :
    st.write("# Positive")