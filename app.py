import streamlit as st
import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text

this is a list:

- item 1

blah blah

""")
st.markdown("""
---
""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10),
    'third column': np.random.randn(10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 5)
st.text(line_count)

# and used to select the displayed lines
head_df = df.head(line_count)

# head_df
st.dataframe(head_df)

def get_data():
    return pd.DataFrame(
            np.random.randn(3, 3),
            columns=['a', 'b', 'c'])

@st.cache
def get_cached_data():
    return get_data()

columns = st.columns(2)
columns[0].write("Uncached dataframe")
columns[0].write(get_data())

columns[1].write("Cached dataframe")
columns[1].write(get_cached_data())


@st.cache
def get_plotly_data():

    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    return x, y, z

import plotly.graph_objects as go

x, y, z = get_plotly_data()

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)
