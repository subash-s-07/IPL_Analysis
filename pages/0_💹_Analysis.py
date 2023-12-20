import streamlit as st
import webbrowser
st.set_page_config(page_title="IPL Analysis", page_icon=":cricket_game:")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/wp/wp5315423.jpg");
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
def open_powerbi():
    # Replace the URL below with your Power BI report URL
    url = "youtube.com"
    webbrowser.open_new_tab(url)

# Set page title and favicon

# Set page background color and font
st.markdown(
    """
    <style>
    body {
        font-family: 'Open Sans', sans-serif;
        background-color: pink;
        color: #444444;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 15px;
    }
    .header {
        padding: 30px 0;
        text-align: center;
    }
    .header h1 {
        font-size: 56px;
        margin-bottom: 20px;
        color: #009933;
        text-shadow: 2px 2px #eeeeee;
    }
    .header p {
        font-size: 24px;
        margin-bottom: 0;
        color: #333333;
        text-shadow: 1px 1px #eeeeee;
    }
    .analysis-container {
        margin-top: 50px;
        padding: 30px;
        background-color: orange;
        box-shadow: 2px 2px 5px #cccccc;
        border-radius: 10px;
    }
    .analysis-container h2 {
        font-size: 40px;
        margin-bottom: 20px;
        color: #009933;
        text-shadow: 2px 2px #eeeeee;
    }
    .analysis-container img {
        display: block;
        margin: 0 auto;
        max-width: 100%;
        margin-bottom: 20px;
        box-shadow: 2px 2px 5px #cccccc;
    }
    .analysis-container p {
        font-size: 24px;
        color: #444444;
        text-shadow: 1px 1px #eeeeee;
    }
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 50px;
    }
    .button-container a {
        background-color: #009933;
        color: #ffffff;
        padding: 15px 30px;
        font-size: 24px;
        font-weight: bold;
        text-decoration: none;
        border-radius: 5px;
        box-shadow: 2px 2px 5px #cccccc;
        transition: all 0.2s ease-in-out;
    }
    .button-container a:hover {
        background-color: #006622;
        box-shadow: 2px 2px 10px #cccccc;
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add page header and description
st.markdown("<div class='container header'><h1>IPL Analysis</h1><p>Explore IPL data and insights.</p></div>", unsafe_allow_html=True)

# Add container for batting stats
with st.container():
    st.markdown("<div class='container analysis-container'><h2>Batting Stats</h2><img src='https://media.tenor.com/Jtxu6lwxDLkAAAAC/dhoni-finishing-with-a-six---story-that-never-ends-dhoni.gif' alt='MS Dhoni' /><p>Explore batting statistics for IPL teams and players.</p></div>", unsafe_allow_html=True)
#Add container for bowling stats

with st.container():
    st.markdown("<div class='container analysis-container'><h2>Bowling Stats</h2><img src='https://media.tenor.com/UoMR7q_GpkwAAAAC/what-make-rcb-loose-ipl-2020-abd.gif' alt='Lasith Malinga' /><p>Explore bowling statistics for IPL teams and players.</p></div>", unsafe_allow_html=True)
#Add container for fielding stats

with st.container():
    st.markdown("<div class='container analysis-container'><h2>Fielding Stats</h2><img src='https://images.jagran.com/naidunia/catch.gif_18_05_2018.jpg' alt='Suresh Raina' /><p>Explore fielding statistics for IPL teams and players.</p></div>", unsafe_allow_html=True)
#Add button to open Power BI report
st.image('https://tactanalytics.com/wp-content/uploads/2023/01/power-BI-icon-1536x864.png')

st.markdown("<div class='container button-container'><a href='https://app.powerbi.com/reportEmbed?reportId=6e749d58-26a4-4694-b323-28132d339f73&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244' onclick='open_powerbi()'>View Full Analysis</a></div>", unsafe_allow_html=True)
