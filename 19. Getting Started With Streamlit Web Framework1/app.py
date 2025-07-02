import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title("Hello Streamlit!")

# display simple text 
st.write("This is my first Streamlit app!")

# Create a simple dataframe
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40],
})

# display the dataframe
st.write("Here is a simple dataframe:")
st.dataframe(df)

# create a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(chart_data)