import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Rajasthan Royals", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://www.sportsadda.com/static-assets/waf-images/25/e1/7d/16-9/PwVwBXYrnX.jpg?v=1.2&w=900");
background-size: 130%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/RR/Banner/RRbanner.png"
logo_image = "https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Rajasthan_Royals_Logo.svg/1024px-Rajasthan_Royals_Logo.svg.png"

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
            background-color: pink;
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
        .samson-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="samson-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/258.png">
            <div>
                <h1>Rajasthan Royals</h1>
                <p>Rajasthan Royals (RR) is a franchise cricket team based in Jaipur, Rajasthan, India. The team plays in the Indian Premier League (IPL) and won the inaugural tournament in 2008.</p>
                <p>The team is captained by Sanju Samson and coached by Kumar Sangakkara. The home ground of RR is Sawai Mansingh Stadium, which has a capacity of 30,000.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Rajasthan Royals on social media:")

    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/rajasthanroyals", "icon": "fab fa-twitter"},
        {"name": "Facebook", "url": "https://www.facebook.com/RajasthanRoyals", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/rajasthanroyals/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/user/TheRajasthanRoyals", "icon": "fab fa-youtube"},
        {"name": "Website", "url": "https://www.rajasthanroyals.com/", "icon": "fas fa-globe"},
    ]

    # Loop through the social media links and display them with icons
    for link in social_media_links:
        st.markdown(f'<a href="{link["url"]}" target="_blank"><i class="{link["icon"]} fa-2x"></i> {link["name"]}</a>', unsafe_allow_html=True)


def player():
    link = [

    "https://assets.iplt20.com/ipl/IPLHeadshot2022/258.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/5430.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/509.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/1705.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/13538.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20620.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/8.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/4445.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/2743.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20616.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/12480.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/3824.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20618.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/5105.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/969.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/111.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",]
    name=[ "Sanju Samson", "Devdutt Padikkal", "Jos Buttler", "Shimron Hetmyer", "Yashasvi Jaiswal", "Dhruv Jurel", "Ravichandran Ashwin", "Riyan Parag", "KC Cariappa", "Kuldeep Sen", "Kuldip Yadav", "Navdeep Saini", "Obed McCoy", "KM Asif", "Prasidh Krishna", "Trent Boult", "Murugan Ashwin", "Yuzvendra Chahal", "Jason Holder", "Akash Vashisht", "Kunal Rathore","Donovan Ferreira", "Adam Zampa", "Abdul P A", "Joe Root"]
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: pink;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Rajasthan_Royals_Logo.svg/1024px-Rajasthan_Royals_Logo.svg.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
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
        "https://app.powerbi.com/reportEmbed?reportId=21e20fc1-3a30-4fb0-9716-140a7154330b&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
player()
power_bi()
display_social_media()
st.sidebar.video("https://youtu.be/clIYzqDDyY4", start_time=0)


