import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Mumbai Indians", layout="wide")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/6/6e/Wankhede_ICC_WCF.jpg");
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/CSK/Banner/CSK.png"
logo_image = "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png"

page_bg_img = '''
<style>
body {
background-image: url("https://upload.wikimedia.org/wikipedia/commons/5/55/MA_Chidambaram_Stadium_in_the_Night.JPG");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
# Define images
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/MI/Banner/MIbanner.jpg"
logo_image = "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Mumbai_Indians_Logo.svg/1200px-Mumbai_Indians_Logo.svg.png"

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
            background-color: #5050DB;
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
        .rohit-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="rohit-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/107.png">
            <div>
                <h1>Mumbai Indians</h1>
                <p>Mumbai Indians (MI) is a franchise cricket team based in Mumbai, Maharashtra, India. The team plays in the Indian Premier League (IPL) and has won the tournament five times in 2013, 2015, 2017, 2019, and 2020.</p>
                <p>The team is captained by Rohit Sharma and coached by Mahela Jayawardene. The home ground of MI is Wankhede Stadium, which has a capacity of 33,108.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Mumbai Indians on social media:")
    
    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/mipaltan", "icon": "fab fa-twitter"},
        {"name": "Facebook", "url": "https://www.facebook.com/mumbaiindians/", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/mumbaiindians/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/channel/UCjX5_ie5zhbzB2UJjgsefhw", "icon": "fab fa-youtube"},
        {"name": "Website", "url": "https://www.mumbaiindians.com/", "icon": "fas fa-globe"},
    ]
    
    # Loop through the social media links and display them with icons
    for link in social_media_links:
        st.markdown(f'<a href="{link["url"]}" target="_blank"><i class="{link["icon"]} fa-2x"></i> {link["name"]}</a>', unsafe_allow_html=True)
def power_bi():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Team Analysis</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.components.v1.iframe(
        "https://app.powerbi.com/reportEmbed?reportId=964fff08-181c-4b81-acce-50add9094755&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
)


def gallery():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Gallery</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    images = ["https://www.enca.com/sites/default/files/styles/media_image/public/2019-05/000_1GE2IK.jpg?h=6da2c5b1&itok=pu603vNk", 
              "https://img.cricketworld.com/images/f-075531/ipl-winner-mi.jpg", 
              "https://images.thequint.com/thequint%2F2022-11%2F44b87ec5-dac1-4549-86be-f193545cae3f%2F_RAJ4902.jpg?auto=format%2Ccompress&fmt=webp&width=720", 
              "https://bl-i.thgim.com/public/incoming/gr60mu/article65271100.ece/alternates/FREE_1200/PTI03_27_2022_000174B.jpg"]
    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:1000px; height:300px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
def display_players():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<h2 style="font-size: 30px;">MI has a strong squad of players, consisting of both experienced and young talent. Here are some of the key players in the team:</h2>', unsafe_allow_html=True)
    #st.write("<h3style=font-size: 40px; color: yellow;>CSK has a strong squad of players, consisting of both experienced and young talent. Here are some of the key players in the team:</h3>")
    name = ["Rohit Sharma",         "Dewald Brevis",         "Suryakumar Yadav",         "Ishan Kishan",         "Arjun Tendulkar",         "Hrithik Shokeen",         "Jofra Archer",         "Mohd. Arshad Khan",         "N. Tilak Varma",         "Ramandeep Singh",         "Tim David",         "Jasprit Bumrah",         "Cameron Green",         "Jhye Richardson",         "Kumar Kartikeya Singh",         "Tristan Stubbs",         "Piyush Chawla",         "Akash Madhwal",         "Shams Mulani",         "Jason Behrendorff","Nehal Wadhera",         "Vishnu Vinod",         "Raghav Goyal",         "Duan Jansen",         ]
    link = [
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/107.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20593.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/108.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/2975.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/10244.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20598.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20599.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20594.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20595.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/4524.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/1124.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20629.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20631.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://assets.iplt20.com/ipl/IPLHeadshot2022/20681.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png",
    "https://www.iplt20.com/assets/images/default-headshot.png"]
    image_html = ''
    for url in range(len(link)):
        image_html += f"""<div style="display: inline-block; margin-right: 20px;">
    <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: blue;border-radius: 20px 20px 0 0;">
            <img src="{link[url]}" width="300" height="300" />
            <img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
            <div style="position: absolute; bottom: 10px; left: 10px; background-color: white; color: yellow; padding: 10px; border-radius: 20px;">"{name[url]}"</div>
            </div>
            <div style="background-color: black; color: white; padding: 10px; width: 250px;border-radius: 0 0 20px 20px;">"{name[url]}"</div>
            </div>"""
    st.markdown(f"""<div style="white-space: nowrap; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

display_header()
display_team_info()
display_players()
power_bi()
gallery()
display_social_media()
