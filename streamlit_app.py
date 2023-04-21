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
    st.title("Hi, ich bin Stella!")
    st.write("Ein paar Dinge, die ihr über mich wissen solltet:")

    st.write("Ich bin 22 Jahre alt und studiere Wirtschaftsinformatik im 2. Semester.")
    st.write("- Ich bin gebürtige Hamburgerin und habe portugiesische Wurzeln.")
    st.write("- Ich habe eine große Schwester und einen Kater.")
    
if __name__ == '__main__':
    main()
