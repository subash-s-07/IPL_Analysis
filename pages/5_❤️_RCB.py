import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Royal Challengers Bangalore", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/c/c2/India_vs_Australia_Test_Match_at_Bengaluru_%2813_March_2017%29.jpg");
background-size: 150%;
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/RCB/Banner/RCBbanner.png"
logo_image = "https://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Royal_Challengers_Bangalore_2020.svg/800px-Royal_Challengers_Bangalore_2020.svg.png"

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
def power_bi():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Team Analysis</p>", unsafe_allow_html=True)
    st.markdown("<<hr>", unsafe_allow_html=True)
    st.write("Here's your embedded Power BI report:")
    st.components.v1.iframe(
        "https://app.powerbi.com/reportEmbed?reportId=870afc69-e024-4263-b5e1-8946fc8700d9&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
)
def gallery():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Gallery</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    images = ["https://pbs.twimg.com/media/FksNa0TVQAABchW?format=jpg&name=900x900", 
              "https://images.indianexpress.com/2021/04/RCBbeatSRH.jpg?w=640", 
              "https://images.hindustantimes.com/img/2022/05/28/550x309/kohli-ipl-rcb-new_1652985401184_1653750259132.jpg", 
              "https://img.republicworld.com/republic-prod/stories/promolarge/xhdpi/xaqql88vymxvelp4_1652859431.jpeg"]
    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:1000px; height:300px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
def display_team_info():
    st.header("Team Information")
    st.markdown(
        f"""
        <style>
        .info {{
            background-color: #E41B17;
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
        .vk-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="vk-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/24.png">
            <div>
                <h1>Royal Challengers Bangalore</h1>
                <p>Royal Challengers Bangalore (RCB) is a franchise cricket team based in Bangalore, Karnataka, India. The team plays in the Indian Premier League (IPL) and has reached the final three times in 2009, 2011, and 2016 but has never won the tournament.</p>
                <p>The team is captained by Faf du Plessis and coached by Mike Hesson. The home ground of RCB is M. Chinnaswamy Stadium, which has a capacity of 35,000.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Royal Challengers Bangalore on social media:")

    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/RCBTweets", "icon": "fab fa-twitter"},
        {"name": "Facebook", "url": "https://www.facebook.com/RoyalChallengersBangalore", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/royalchallengersbangalore/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/user/royalchallengers", "icon": "fab fa-youtube"},
        {"name": "Website", "url": "https://www.royalchallengers.com/", "icon": "fas fa-globe"},
    ]

    # Loop through the social media links and display them with icons
    for link in social_media_links:
        st.markdown(f'<a href="{link["url"]}" target="_blank"><i class="{link["icon"]} fa-2x"></i> {link["name"]}</a>', unsafe_allow_html=True)

    

def player():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    name = [ 'Faf du Plessis', 'Finn Allen', 'Rajat Patidar', 'Virat Kohli', 'Anuj Rawat', 'Dinesh Karthik', 'David Willey', 'Glenn Maxwell', 'Harshal Patel', 'Mahipal Lomror', 'Shahbaz Ahamad', 'Suyash S Prabhudessai', 'Wanindu Hasaranga', 'Akash Deep', 'Josh Hazlewood', 'Karn Sharma', 'Siddharth Kaul', 'Mohammed Siraj', 'Reece Topley', 'Himanshu Sharma', 'Will Jacks','Rajan Kumar', 'Avinash Singh', 'Sonu Yadav', 'Manoj Bhandage']

    link = [ 'https://assets.iplt20.com/ipl/IPLHeadshot2022/24.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/3020.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/5471.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/164.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/10788.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/102.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/2758.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/282.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/157.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/2970.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/13803.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/7002.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/3082.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/14800.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/857.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/1118.png', "https://assets.iplt20.com/ipl/IPLHeadshot2022/1086.png","https://assets.iplt20.com/ipl/IPLHeadshot2022/3840.png",'https://www.iplt20.com/assets/images/default-headshot.png','https://www.iplt20.com/assets/images/default-headshot.png','https://www.iplt20.com/assets/images/default-headshot.png','https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png']
    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: red;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Royal_Challengers_Bangalore_2020.svg/800px-Royal_Challengers_Bangalore_2020.svg.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
                <div style="position: absolute; bottom: 10px; left: 10px; background-color: white; color: yellow; padding: 10px; border-radius: 20px;">"{name[url]}"</div>
                </div>
                <div style="background-color: black; color: white; padding: 10px; width: 250px;border-radius: 0 0 20px 20px;">"{name[url]}"</div>
                </div>"""
    st.markdown(f"""<div style="white-space: nowrap; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
display_header()
display_team_info()
player()
power_bi()
gallery()
display_social_media()
st.sidebar.video("https://youtu.be/yxGsg_n_j0Y", start_time=0)
st.markdown(
    """
    <div class="icon-container">
      <a href="#" onclick="showAccount('instagram')"><img src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/instagram_circle-512.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('whatsapp')"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-whatsapp-circle-512.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('twitter')"><img src="https://cdn3.iconfinder.com/data/icons/social-icons-5/607/Twitterbird.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('mail')"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/gmail-512.png" width="30" height="30"></a>
    </div>
    """,
    unsafe_allow_html=True
)
