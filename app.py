import streamlit as st
import pandas as pd

# Takes in a username and prints out a greeting text
st.title('A Simple Streamlit Web App')
name = st.text_input('Your name', '')
if len(name) > 0:
    st.write(f'Hello {name}!')

st.header("Let's do some math")
# Takes in two slider inputs of integers ranging from 0 to 10
x = st.slider('Select an integer X', 0, 10, 3)
y = st.slider('Select an integer Y', 0, 10, 5)
df = pd.DataFrame(
    {'x': [x], 'y': [y], 'x + y': [x + y]}, 
    index = ['addition row'],
)
# Prints out the variables and their sums
st.write(df)
