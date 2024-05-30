import streamlit as st

# Function to open a URL in a new tab using query parameters
def open_url(url):
    st.experimental_set_query_params(url=url)
    st.markdown(f'<a href="{url}" target="_blank">{url}</a>', unsafe_allow_html=True)

# Streamlit app layout
st.title('Dashboard with Buttons')

# Create buttons
if st.button('Go to Google'):
    open_url('https://www.google.com')

if st.button('Go to YouTube'):
    open_url('https://www.youtube.com')

if st.button('Go to GitHub'):
    open_url('https://www.github.com')

if st.button('Go to OpenAI'):
    open_url('https://www.openai.com')
