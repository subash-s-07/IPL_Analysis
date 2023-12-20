import streamlit as st
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpaperaccess.com/full/1947558.jpg");
background-size: 100%;
background-position: top left;
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
st.markdown("""
    <style>
    .img1 {
        max-width: 300px;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color : #00008B; font-size:55px'>IPL AND T20 ANALYSIS</h1>", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center;">
        <a href="http://localhost:8501/CSK" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/DC" target="_blank"><img src="https://www.delhicapitals.in/static-assets/images/cssimages/logo.png" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/GT" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/0/09/Gujarat_Titans_Logo.svg" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/KKR" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/LSG" target="_blank"><img src="https://iplmatcheslive.com/wp-content/uploads/2023/03/Lucknow-Super-Giants-2048x2048.png" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/MI" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/PKBS" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/RR" target="_blank"><img src="https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/RR/Logos/Medium/RR.png" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/RCB" target="_blank"><img src="https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/RCB/Logos/Medium/RCB.png" alt="Your Image" class="img1"></a>
        <a href="http://localhost:8501/SRH" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/en/e/eb/Sunrisers_Hyderabad.png" alt="Your Image" class="img"></a>

    </div>
""", unsafe_allow_html=True)