
import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Kolkata Knight Riders", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("kkr.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/c/ce/Eden_Gardens%2C_Kolkata_%2805%29.jpg");
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/KKR/Banner/KKRbanner.png"
logo_image = "https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg"

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
            background-color: #7B1FA9;
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
            <img class="samson-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/1563.png">
            <div>
                <h1>Kolkata Knight Riders</h1>
                <p>Kolkata Knight Riders (KKR) are a franchise cricket team representing the city of Kolkata in the Indian Premier League.</p>
                <p> The franchise is owned by Bollywood actor Shah Rukh Khan, actress Juhi Chawla and her spouse Jay Mehta. The Knight Riders play at the Eden Gardens stadium.</p>
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
    link=[
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/1563.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/3830.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/2738.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/3774.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/177.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/8540.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/59.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20626.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/307.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/203.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/5432.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png']
   
    name=[ 'Shreyas Iyer', 'Rinku Singh', 'Rahmanullah Gurbaz', 'David Wiese', 'Kulwant Khejroliya', 'Suyash Sharma', 'Nitish Rana', 'Anukul Roy', 'Lockie Ferguson', 'Andre Russell', 'Venkatesh Iyer', 'Umesh Yadav', 'Harshit Rana', 'Tim Southee', 'Shardul Thakur', 'Sunil Narine', 'Vaibhav Arora', 'Varun Chakaravarthy', 'Narayan Jagadeesan', 'Litton Das', 'Mandeep Singh', 'Shakib Al Hasan', 'Shreyas Iyer', 'Rinku Singh', 'Rahmanullah Gurbaz', 'David Wiese', 'Kulwant Khejroliya', 'Suyash Sharma', 'Nitish Rana', 'Anukul Roy', 'Lockie Ferguson', 'Andre Russell', 'Venkatesh Iyer', 'Umesh Yadav', 'Harshit Rana', 'Tim Southee', 'Shardul Thakur', 'Sunil Narine', 'Vaibhav Arora', 'Varun Chakaravarthy', 'Narayan Jagadeesan', 'Litton Das', 'Mandeep Singh', 'Shakib Al Hasan','Narayan Jagadeesan', 'Litton Das', 'Mandeep Singh', 'Shakib Al Hasan',]
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: purple;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
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
        "https://app.powerbi.com/reportEmbed?reportId=34c14883-9514-4d6a-8ff8-c0f0d84b856a&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
player()
power_bi()
display_social_media()


