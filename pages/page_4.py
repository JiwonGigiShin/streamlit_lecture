import streamlit as st

st.title("Session_state")

"st.session_state object", st.session_state

number = st.slider("A number", 1, 10, key="slider")

col1, buff, col2 = st.columns([1,0.5,3])

option_names = ["a", "b", "c"]

next_button = st.button("Next Option")

if next_button:
    if st.session_state['radio_option']=='a':
        st.session_state['radio_option'] = 'b'
    elif st.session_state['radio_option']=='b':
        st.session_state['radio_option'] = 'c'
    else:
        st.session_state['radio_option'] = 'a'


option = col1.radio("pick an option", option_names, key = 'radio_option')

st.session_state
