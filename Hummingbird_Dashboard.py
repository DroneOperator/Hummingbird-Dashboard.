import streamlit as st

# Streamlit app layout
st.title('Drone Dashboard with Buttons')

# Create buttons and iframes for the specified drone websites
if st.button('Go to Navdrone Portal'):
    st.write('<iframe src="https://portal.navdrone.ca/auth/realms/OperatorPortal/protocol/openid-connect/auth?client_id=NavcanPortal&redirect_uri=https%3A%2F%2Fportal.navdrone.ca%2F%23%2F&state=4ed62398-af8c-42df-8265-9c3dc21f64bd&response_mode=fragment&response_type=code&scope=openid&nonce=5ab2a115-bb8c-47d5-8971-c1617ea533d3" width="100%" height="600"></iframe>', unsafe_allow_html=True)

if st.button('Go to Cheqroom'):
    st.write('<iframe src="https://login.cheqroom.com/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

if st.button('Go to NRC Drone Tool'):
    st.write('<iframe src="https://nrc.canada.ca/en/drone-tool/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

if st.button('Go to SafetyCulture'):
    st.write('<iframe src="https://auth.safetyculture.com/login?state=hKFo2SBUTnBhNXMwbXgzNkpuc0hReFhhMERWdXJOR2RxaWFqbqFupWxvZ2luo3RpZNkgdHh4eHNZSjF0WFlVdjBxblJReGIyOV9Fc0xlQWJTclqY2lk2SBpVGh3ZWRFaVZXMGdkcVc2czZ3d2ZJeXVPQVJWeXNQSQ&client=iThwedEiVW0gdqW6s6wwfIyuOARVysPI&protocol=oauth2&nonce=f-xc0Na09qhGzOHN&redirect_uri=https%3A%2F%2Fapp.safetyculture.com%2Fauth-callback&response_type=code&sc_state=eyJ0b2tlbiI6IjFmYmZhNTlkLTM1YTAtNDU4ZC04Y2NkLWUwYzA3YzE4NTE4MyIsImNsaWVudElEIjoiaVRod2VkRWlWVzBnZHFXNnM2d3dmSXl1T0FSVnlzUEkiLCJkZXN0aW5hdGlvblVSSSI6Ii8iLCJxdWVyeSI6Ij8iLCJ0aW1lSXNzdWVkIjoiMjAyNC0wNS0yOSAxNjoyNDoyNC4yMDI5NjgwNjMgKzAwMDAgVVRDIG09KzIzMDM0LjY4MDU3NTQxOCJ9&scope=openid%20profile%20email&version=2." width="100%" height="600"></iframe>', unsafe_allow_html=True)
