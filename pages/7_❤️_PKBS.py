import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Punjab Kings", layout="wide")
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("PKBS.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img1.hscicdn.com/image/upload/f_auto,t_ds_w_1200/lsci/db/PICTURES/CMS/346200/346264.jpg");
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
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/PBKS/Banner/PBKSbanner.png"
logo_image = "https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg"

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
        .rishabh-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="rishabh-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/41.png">
            <div>
                <h1>Punjab Kings</h1>
                <p>Punjab Kings (PBKS) are a franchise cricket team based in Mohali, Punjab, that plays in the Indian Premier League (IPL)..</p>
                <p> Established in 2008 as the Kings XI Punjab (KXIP), the franchise is jointly owned by Mohit Burman, Ness Wadia, Preity Zinta and Karan Paul. The team plays its home matches at the PCA Stadium, Mohali</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Punjab Kings on social media:")
    
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
"https://assets.iplt20.com/ipl/IPLHeadshot2022/41.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/20604.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/3185.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/506.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/5436.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/20603.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/5441.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/3644.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/20601.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/1088.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/7779.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/4698.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/20607.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/1664.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/17118.png",
"https://assets.iplt20.com/ipl/IPLHeadshot2022/3763.png",
"https://www.iplt20.com/assets/images/default-headshot.png",
"https://www.iplt20.com/assets/images/default-headshot.png",
"https://www.iplt20.com/assets/images/default-headshot.png",
"https://www.iplt20.com/assets/images/default-headshot.png",
"https://www.iplt20.com/assets/images/default-headshot.png",
"https://www.iplt20.com/assets/images/default-headshot.png"]
    name=[
'Shikhar Dhawan',
'Bhanuka Rajapaksa',
'Jitesh Sharma',
'Jonny Bairstow',
'Prabhsimran Singh',
'Atharva Taide',
'Harpreet Brar',
'Liam Livingstone',
'Raj Angad Bawa',
'Rishi Dhawan',
'Shahrukh Khan',
'Arshdeep Singh',
'Baltej Dhanda',
'Kagiso Rabada',
'Nathan Ellis',
'Rahul Chahar',
'Sam Curran',
'Sikandar Raza',
'Harpreet Bhatia',
'Vidwath Kaverappa',
'Mohit Rathee',
'Shivam singh']
    image_html = ''
    for url in range(len(link)):
            image_html += f"""<div style="display: inline-block; margin-right: 20px;">
        <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: red;border-radius: 20px 20px 0 0;">
                <img src="{link[url]}" width="300" height="300" />
                <img src="https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
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
        "https://app.powerbi.com/reportEmbed?reportId=8cd1e194-20fb-488d-8a0a-b0b70bbd8a04&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
player()
power_bi()
display_social_media()