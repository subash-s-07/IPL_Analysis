import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Delhi Capitals", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("mi.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/0/0c/Arun_Jaitley_Stadium_during_India_vs_Australia_2019_ODI.jpg");
background-size: 130%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
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
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Define images
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/DC/Banner/DCbanner.png"
logo_image = "https://www.delhicapitals.in/static-assets/images/cssimages/logo.png"

# Define page sections
def display_header():
    st.markdown(
        f"""
        <style>
        .header {{
            background-image: url("{background_image}");
            background-repeat: no-repeat;
            background-size: 100% 100%;
            display: flex;
            justify-content: left;
            align-items: center;
            height: 300px;
        }}
        .logo {{
            max-width: 80%;
            max-height: 80%;
        }}
        </style>
        <div class="header">
            <img class="logo" src="{logo_image}">
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_team_info():
    st.header("Team Information")
    st.markdown(
        f"""
        <style>
        .info {{
            background-color: #1BB3FF;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 5px 5px 10px #888888;
            font-size: 18px;
            line-height: 1.5;
            margin-top: 50px;
            display: flex;
            align-items: center;
        }}
        .info h1 {{
            font-size: 40px;
            margin-bottom: 20px;
        }}
        .info p {{
            margin-bottom: 10px;
            margin-left: 30px;
        }}
        .rishabh-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="rishabh-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/2972.png">
            <div>
                <h1>Delhi Capitals</h1>
                <p>Delhi Capitals (DC) is a franchise cricket team based in Delhi, India. The team plays in the Indian Premier League (IPL) and has never won the tournament.</p>
                <p>The team is captained by Rishabh Pant and coached by Ricky Ponting. The home ground of DC is Arun Jaitley Stadium, which has a capacity of 41,820.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Delhi Capitals on social media:")
    
    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/DelhiCapitals", "icon": "fab fa-twitter"},
        {"name": "Facebook", "url": "https://www.facebook.com/DelhiCapitals/", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/delhicapitals/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/channel/UC0UzD6UjeH9pVxGKhI/","icon": "fab fa-youtube"}]
    for link in social_media_links:
        st.markdown(f'<a href="{link["url"]}" target="_blank"><i class="{link["icon"]} fa-2x"></i> {link["name"]}</a>', unsafe_allow_html=True)
def player():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    link=[
'https://assets.iplt20.com/ipl/IPLHeadshot2022/2972.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/170.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/3764.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/3333.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/1113.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/3766.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/6870.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/221.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/3188.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/17191.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/1564.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/20624.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/20623.png',
'https://www.iplt20.com/assets/images/default-headshot.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/5433.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/11062.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/261.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/3746.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/1594.png',
'https://assets.iplt20.com/ipl/IPLHeadshot2022/2964.png',
'https://www.iplt20.com/assets/images/default-headshot.png',
'https://www.iplt20.com/assets/images/default-headshot.png',
'https://www.iplt20.com/assets/images/default-headshot.png',
'https://www.iplt20.com/assets/images/default-headshot.png',
'https://www.iplt20.com/assets/images/default-headshot.png']
    name=[
'Rishabh Pant',
'David Warner',
'Prithvi Shaw',
'Rovman Powell',
'Axar Patel',
'Kamlesh Nagarkoti',
'Lalit Yadav',
'Mitchell Marsh',
'Pravin Dubey',
'Ripal Patel',
'Sarfaraz Khan',
'Vicky Ostwal',
'Yash Dhull',
'Aman Khan',
'Anrich Nortje',
'Chetan Sakariya',
'Kuldeep Yadav',
'Lungi Ngidi',
'Mustafizur Rahman',
'Khaleel Ahmed',
'Phil Salt',
'Ishant Sharma',
'Mukesh Kumar',
'Manish Pandey',
'Rilee Rossouw']
    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: blue;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://www.delhicapitals.in/static-assets/images/cssimages/logo.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
                <div style="position: absolute; bottom: 10px; left: 10px; background-color: white; color: yellow; padding: 10px; border-radius: 20px;">"{name[url]}"</div>
                </div>
                <div style="background-color: black; color: white; padding: 10px; width: 250px;border-radius: 0 0 20px 20px;">"{name[url]}"</div>
                </div>"""
    st.markdown(f"""<div style="white-space: nowrap; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
def power_bi():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Team Analysis</p>", unsafe_allow_html=True)
    st.markdown("<<hr>", unsafe_allow_html=True)
    st.write("Here's your embedded Power BI report:")
    st.components.v1.iframe(
        "https://app.powerbi.com/reportEmbed?reportId=f644212a-a8c0-4373-8286-6cc64815ac49&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
player()
power_bi()
display_social_media()
