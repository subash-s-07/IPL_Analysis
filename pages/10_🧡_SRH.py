import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Sunrisers Hyderabad", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("D:\\davl project\\2474773.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://cdn-wp.thesportsrush.com/2023/01/155f2883-untitled-design-2023-01-18t123424.750.jpg");
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/SRH/Banner/SRHbanner.png"
logo_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/SRH/Logos/Medium/SRH.png"

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
            background-color: #F55E10;
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
        .david-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="david-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/1667.png">
            <div>
                <h1>Sunrisers Hyderabad</h1>
                <p>Sunrisers Hyderabad (SRH) is a franchise cricket team based in Hyderabad, Telangana, India. The team plays in the Indian Premier League (IPL) and has won the tournament once in 2016.</p>
                <p>The team is captained by Aiden Markram and coached by Trevor Bayliss. The home ground of SRH is Rajiv Gandhi International Cricket Stadium, which has a capacity of 55,000.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Sunrisers Hyderabad on social media:")

    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/SunRisers", "icon": "fab fa-twitter"},
        {"name": "Facebook", "url": "https://www.facebook.com/SunRisersHyderabad", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/sunrisershyd/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/channel/UCG5MQdP5oGFCbwHtgW8oEgA", "icon": "fab fa-youtube"},
        {"name": "Website", "url": "https://www.sunrisershyderabad.in/", "icon": "fas fa-globe"},
    ]

    # Loop through the social media links and display them with icons
    for link in social_media_links:
        st.markdown(f'<a href="{link["url"]}" target="_blank"><i class="{link["icon"]} fa-2x"></i> {link["name"]}</a>', unsafe_allow_html=True)


def player():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    name = [ 'Abdul Samad', 'Aiden Markram', 'Rahul Tripathi', 'Glenn Phillips', 'Abhishek Sharma', 'Marco Jansen', 'Washington Sundar', 'Bhuvneshwar Kumar', 'Fazalhaq Farooqi', 'Kartik Tyagi', 'T Natarajan', 'Umran Malik', 'Harry Brook', 'Mayank Agarwal', 'Akeal Hosein', 'Heinrich Klaasen', 'Anmolpreet Singh', 'Adil Rashid', 'Mayank Markande', 'Vivrant Sharma', 'Mayank Dagar','Samarth Vyas', 'Sanvir Singh', 'Upendra Singh Yadav', 'Nitish Kumar Reddy']

    link = [
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/19352.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/1667.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/3838.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/3027.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/3760.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/17068.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/2973.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/116.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/20610.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/10059.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/3831.png',
         'https://assets.iplt20.com/ipl/IPLHeadshot2022/15154.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png',
         'https://www.iplt20.com/assets/images/default-headshot.png']
    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: Orange;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/SRH/Logos/Medium/SRH.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
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
        "https://app.powerbi.com/reportEmbed?reportId=d03dcfa2-e98e-4c85-86b2-cd6f11db07b7&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
player()
power_bi()
display_social_media()
