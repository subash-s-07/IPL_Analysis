import streamlit as st
st.set_page_config(page_title="Standing", layout="wide")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/7130560/pexels-photo-7130560.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
background-size: 130%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
.slider {{
    color: white;
}}
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
.sidebar {{
    color: white;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.components.v1.iframe(
        "https://app.powerbi.com/reportEmbed?reportId=018afea7-f406-4909-b23d-a404de1e0008&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=1000,
        scrolling=True,
        width=1700,
)