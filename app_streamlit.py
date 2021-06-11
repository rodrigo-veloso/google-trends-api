import os
import subprocess
import requests
import json
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

def recursive_text_input(i):
    keyword = st.text_input('Enter some text', key = i)
    button = st.button('more', key = i)
    if button:
        return recursive_text_input(i+1)

#col1, col2, col3, col4, col5 = st.beta_columns((0.6,0.2,0.4,0.2,0.5))

#col1.image('patrus.png', width =240)
#col2.markdown("<h1 style='font-size: 48px;text-align: center;'>+</h1>", unsafe_allow_html=True)
#col3.image('a3.png', width =120)
#col4.markdown("<h1 style='font-size: 48px;text-align: center;'>=</h1>", unsafe_allow_html=True)
#col5.image('The_Flash_png.png', width =200)

st.write("""# Google Trends API""")

pytrends = TrendReq(hl='pt-BR', tz=360)
st.write("""### Digite as palavras chave separadas por vírgula""")
keywords = st.text_input('')
keywords = keywords.split(',')
if keywords[0] != '':
    pytrends.build_payload(kw_list = keywords, cat=0, timeframe='today 5-y', geo='', gprop='')
    data = pytrends.interest_over_time()
    ax = data.plot()
    st.pyplot(ax.figure)
