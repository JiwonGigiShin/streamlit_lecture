import streamlit as st
import requests


st.markdown("""# This is Page 2: Connection to an API 🚀!
""")

#query

url = "https://api.giphy.com/v1/gifs/search"

query = st.text_input("Search a gif")
#params
params = {
    "api_key": st.secrets["api_key"],
        "q":query,
        "limit":1

}




#response
response = requests.get(url, params=params)


while not query:
    st.warning('Please enter a search term')
    st.stop()

gif_url = response.json()['data'][0]['embed_url']

st.markdown(f'<iframe src="{gif_url}" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/{query}">via GIPHY</a></p>', unsafe_allow_html=True)
