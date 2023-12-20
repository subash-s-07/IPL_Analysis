import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Lucknow Super Giants", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("D:\\davl project\\2474773.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("");
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/LSG/Banner/LSGbanner.png"
logo_image = "https://iplmatcheslive.com/wp-content/uploads/2023/03/Lucknow-Super-Giants-2048x2048.png"

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
            background-color: #FFA500;
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
            <img class="rishabh-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/1125.png">
            <div>
                <h1>Lucknow Super Giants</h1>
                <p>Lucknow Super Giants is a franchise cricket team based in Lucknow, Uttar Pradesh. They play in the Indian Premier League (IPL). The Lucknow franchise formed in 2021. Sanjeev Goenka is its principal owner. </p>
                <p>The team is captained by KL Rahul and coached by Andy Flower.[1] The team mentor is Gautam Gambhir. In its debut season, Lucknow Super Giants qualified for the play-offs.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Lucknow Super Giants on social media:")
    
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
    link=[    "https://assets.iplt20.com/ipl/IPLHeadshot2022/1125.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/1085.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/834.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20586.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/1556.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/3834.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20588.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/3183.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20587.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/964.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/1561.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20585.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/4952.png",    "https://assets.iplt20.com/ipl/IPLHeadshot2022/19351.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png","https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png",    "https://www.iplt20.com/assets/images/default-headshot.png"]
    name=[      "KL Rahul",    "Manan Vohra",    "Quinton de Kock",    "Ayush Badoni",    "Deepak Hooda",    "Krishnappa Gowtham",    "Karan Sharma",    "Krunal Pandya",    "Kyle Mayers",    "Marcus Stoinis",    "Avesh Khan",    "Mark Wood",    "Mayank Yadav",    "Mohsin Khan",    "Ravi Bishnoi",    "Jaydev Unadkat",    "Yash Thakur",    "Romario Shepherd",    "Nicholas Pooran",    "Amit Mishra",    "Daniel Sams", "Swapnil Singh",    "Prerak Mankad",    "Naveen Ul Haq",    "Yudhvir Singh"]
    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color:orange;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://iplmatcheslive.com/wp-content/uploads/2023/03/Lucknow-Super-Giants-2048x2048.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
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
        "https://app.powerbi.com/reportEmbed?reportId=f93c065c-6ff5-4c1c-b64f-6080e2701f75&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
player()
power_bi()
display_social_media()