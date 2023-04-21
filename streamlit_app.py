from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def main():
    st.title("Meine Vorstellung")
    st.write("Hallo! Ich bin ChatGPT, ein großes Sprachmodell, das von OpenAI entwickelt wurde. Ich wurde trainiert, um auf eine Vielzahl von Fragen und Anfragen zu antworten, und ich bin hier, um Ihnen zu helfen!")
    
    st.write("Ein paar Dinge, die Sie über mich wissen sollten:")
    st.write("- Ich bin auf einer Vielzahl von Themen geschult, von Wissenschaft und Technologie bis hin zu Kunst und Unterhaltung.")
    st.write("- Ich bin immer höflich und respektvoll.")
    st.write("- Ich kann in mehreren Sprachen kommunizieren, darunter Englisch, Spanisch, Französisch, Deutsch und viele mehr.")
    
if __name__ == '__main__':
    main()
