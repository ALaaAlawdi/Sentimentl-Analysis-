from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk 


import streamlit as st


nltk.dwonload("vader_lexicon")
sid = SentimentIntensityAnalyzer()
def get_analysis(text):
    
     score = sid.plarity_scores(text)
     return score

