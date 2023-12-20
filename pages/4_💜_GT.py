import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Gujarat Titans", layout="wide")

# Define images
background_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/GT/Banner/GTBanner.png"
logo_image = "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/GT/Logos/Medium/GTmedium.png"

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/f/fd/IMG-20230312-WA0001.jpg");
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
    st.markdown(
    """
    <style>
    .streamlit-header > .toolbar > .title-container > h1 {
        color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.header("Team Information")
    st.markdown(
        f"""
        <style>
        .info {{
            background-color: #51DBAD;
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
        .msd-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="msd-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/2740.png">
            <div>
                <h1>Gujarat Titans</h1>
                <p>Gujarat Titans is a franchise cricket team based in Ahmedabad, Gujarat, India. The Titans compete in the Indian Premier League (IPL). Founded in 2021, Gujarat Titans' home ground is Narendra Modi Stadium in Motera. </p>
                <p>The franchise is owned by CVC Capital Partners.The team is captained by Hardik Pandya and coached by Ashish Nehra. The Gujarat Titans are the current IPL champions, having won their maiden title in the 2022 season.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with GT on social media:")

    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/RCBTweets", "icon": "fab fa-twitter"},
        {"name": "Facebook", "url": "https://www.facebook.com/RoyalChallengersBangalore", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/royalchallengersbangalore/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/user/royalchallengers", "icon": "fab fa-youtube"},
        {"name": "Website", "url": "https://www.royalchallengers.com/", "icon": "fas fa-globe"},
    ]
def display_players():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    #st.markdown('<h2 style="font-size: 30px;">GT has a strong squad of players, consisting of both experienced and young talent. Here are some of the key players in the team:</h2>', unsafe_allow_html=True)
    name = ['Hardik Pandya', 'Abhinav Manohar', 'David Miller', 'Shubman Gill', 'Matthew Wade', 'Wriddhiman Saha', 'B. Sai Sudharsan', 'Darshan Nalkande', 'Jayant Yadav', 'Pradeep Sangwan', 'Rahul Tewatia', 'Shivam Mavi', 'Vijay Shankar', 'Alzarri Joseph', 'Mohammad Shami', 'Noor Ahmad', 'Sai Kishore', 'Rashid Khan', 'Yash Dayal', 'Kane Williamson', 'Joshua Little','Odean Smith', 'Urvil Patel', 'K.S Bharat', 'Mohit Sharma']
    link = ['https://assets.iplt20.com/ipl/IPLHeadshot2022/2740.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/20589.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/187.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/3761.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/290.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/16.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/20592.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/4447.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/1740.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/91.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/1749.png', 'https://www.iplt20.com/assets/images/default-headshot.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/1083.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/3098.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/94.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/20590.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/7123.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/2885.png', 'https://assets.iplt20.com/ipl/IPLHeadshot2022/20591.png', 'https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png','https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png', 'https://www.iplt20.com/assets/images/default-headshot.png']
    image_html = ''
    for url in range(len(link)):
        image_html += f"""<div style="display: inline-block; margin-right: 20px;">
    <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: #51DBAD;border-radius: 20px 20px 0 0;">
            <img src="{link[url]}" width="300" height="300" />
            <img src="https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/GT/Logos/Medium/GTmedium.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
            <div style="position: absolute; bottom: 10px; left: 10px; background-color: white; color: yellow; padding: 10px; border-radius: 20px;">"{name[url]}"</div>
            </div>
            <div style="background-color: black; color: white; padding: 10px; width: 250px;border-radius: 0 0 20px 20px;">"{name[url]}"</div>
            </div>"""
    st.markdown(f"""<div style="white-space: nowrap; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
def display_team_info1():
    st.header("Team Information")
    st.markdown(
        f"""
        <style>
        .info {{
            background-color: #51DBAD;
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
            font-family: Arial, sans-serif;
            color: white;
            text-shadow: 2px 2px #888888;
        }}
        .info p {{
            margin-bottom: 10px;
            margin-left: 30px;
            font-family: Arial, sans-serif;
            color: black;
        }}
        .msd-image {{
            max-width: 300px;
            max-height: 300px;
            margin-right: 30px;
        }}
        </style>
        <div class="info">
            <img class="msd-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/1.png">
            <div>
                <h1>Chennai Super Kings</h1>
                <p>Chennai Super Kings (CSK) is a franchise cricket team based in Chennai, Tamil Nadu, India. The team plays in the Indian Premier League (IPL) and has won the tournament three times in 2010, 2011, and 2018.</p>
                <p>The team is captained by <span style="color: #fdb813; font-style: italic;">MS Dhoni</span> and coached by Stephen Fleming. The home ground of CSK is M. A. Chidambaram Stadium, which has a capacity of 50,000.</p>
            </div>
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
        "https://app.powerbi.com/reportEmbed?reportId=c5322236-4261-43da-9c06-3c37a040f301&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
    )
display_header()
display_team_info()
display_players()
power_bi()
