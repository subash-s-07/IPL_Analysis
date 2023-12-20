import streamlit as st
import base64
# Set page layout
st.set_page_config(page_title="Chennai Super Kings", layout="wide")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/5/55/MA_Chidambaram_Stadium_in_the_Night.JPG");
background-size: 130%;
background-position: top left;
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
.sidebar {{
    color: white;
}}
</style>
"""
main_bg = "rgb(30, 30, 30)"
main_fg = "#F8F8FF"
st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {main_bg};
            color: {main_fg};
        }}
        .sidebar .sidebar-content {{
            background-color: {main_bg};
            color: {main_fg};
        }}
        .css-1aumxhk {{
            background-color: {main_bg};
            color: {main_fg};
        }}
        h1 {{
            font-family: 'Montserrat', sans-serif;
            font-size: 48px;
            color: #ffffff;
        }}
        h2 {{
            font-family: 'Montserrat', sans-serif;
            font-size: 36px;
            color: #ffffff;
        }}
        p {{
            font-family: 'Open Sans', sans-serif;
            font-size: 18px;
            line-height: 1.5;
            color: #ffffff;
        }}
        ul {{
            font-family: 'Open Sans', sans-serif;
            font-size: 18px;
            color: #ffffff;
            line-height: 1.5;
        }}
    </style>
""", unsafe_allow_html=True)
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
            background-color: #FFFFE0;
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
            <img class="msd-image" src="https://assets.iplt20.com/ipl/IPLHeadshot2022/1.png">
            <div>
                <h1>Chennai Super Kings</h1>
                <p>Chennai Super Kings (CSK) is a franchise cricket team based in Chennai, Tamil Nadu, India. The team plays in the Indian Premier League (IPL) and has won the tournament three times in 2010, 2011, and 2018.</p>
                <p>The team is captained by MS Dhoni and coached by Stephen Fleming. The home ground of CSK is M. A. Chidambaram Stadium, which has a capacity of 50,000.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_social_media():
    st.header("Social Media")
    st.write("Stay connected with Chennai Super Kings on social media:")
    
    # Define the social media links and their corresponding icons
    social_media_links = [
        {"name": "Twitter", "url": "https://twitter.com/ChennaiIPL", "icon": "https://cdn3.iconfinder.com/data/icons/social-icons-5/607/Twitterbird.png"},
        {"name": "Facebook", "url": "https://www.facebook.com/TheChennaiSuperKings", "icon": "fab fa-facebook"},
        {"name": "Instagram", "url": "https://www.instagram.com/chennaiipl/", "icon": "fab fa-instagram"},
        {"name": "YouTube", "url": "https://www.youtube.com/channel/UCzxjVDZmpoybOiNtJGj1Oyw", "icon": "fab fa-youtube"},
        {"name": "Website", "url": "https://www.chennaisuperkings.com/", "icon": "fas fa-globe"},
    ]
    
    # Loop through the social media links and display them with icons
    for link in social_media_links:
        st.markdown(f'<a href="{link["url"]}" target="_blank"><i class="{link["icon"]} fa-2x"></i> {link["name"]}</a>', unsafe_allow_html=True)

# Call the function to display the social media links with icons


def display_players():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Players</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<h2 style="font-size: 30px;">CSK has a strong squad of players, consisting of both experienced and young talent. Here are some of the key players in the team:</h2>', unsafe_allow_html=True)
    #st.write("<h3style=font-size: 40px; color: yellow;>CSK has a strong squad of players, consisting of both experienced and young talent. Here are some of the key players in the team:</h3>")
    name=[ 'MS Dhoni', 'Devon Conway', 'Ruturaj Gaikwad', 'Subhranshu Senapati', 'Ambati Rayudu', 'Ravindra Jadeja', 'Dwaine Pretorius', 'Mitchell Santner', 'K Bhagath Varma', 'Moeen Ali', 'Rajvardhan Hangargekar', 'Shivam Dube', 'Deepak Chahar', 'Maheesh Theekshana', 'Mukesh Choudhary', 'Prashant Solanki', 'Simarjeet Singh', 'Ajinkya Rahane', 'Tushar Deshpande', 'Ben Stokes', 'Matheesha Pathirana','Shaik Rasheed', 'Nishant Sindhu', 'Kyle Jamieson', 'Ajay Mandal']
    link=[
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/1.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20572.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/5443.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20574.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/100.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/9.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20573.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/1903.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/1735.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20571.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/5431.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/140.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20570.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20575.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20576.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/10789.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/3257.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://assets.iplt20.com/ipl/IPLHeadshot2022/20627.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png',
    'https://www.iplt20.com/assets/images/default-headshot.png']
    image_html = ''
    for url in range(len(link)):
        image_html += f"""<div style="display: inline-block; margin-right: 20px;">
    <div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: yellow;border-radius: 20px 20px 0 0;">
            <img src="{link[url]}" width="300" height="300" />
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
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
            background-color: #FFFF33;
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
        "https://app.powerbi.com/reportEmbed?reportId=7036297e-3e18-4a56-a298-8dc7e1ab456c&autoAuth=true&ctid=8f9927dc-9983-4774-8a14-9223e3da6244",
        height=900,
        scrolling=True,
        width=1800,
)

def gallery():
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:40px'>Gallery</p>", unsafe_allow_html=True)
    st.markdown("<<hr>", unsafe_allow_html=True)
    images1=["https://images.hindustantimes.com/img/2021/10/16/550x309/Dhoni_CSK_1634361836426_1634361847778.JPG","https://www.manatelangana.news/wp-content/uploads/2021/10/ipl.gif","https://ss-i.thgim.com/public/incoming/ra9f7p/article54681289.ece/alternates/FREE_1200/WhatsApp-Image-2021-09-19-at-225157jpeg","https://img.republicworld.com/republic-prod/stories/promolarge/xhdpi/296rolhketvcu1dl_1634325339.jpeg","https://images.indiafantasy.com/wp-content/uploads/20230215130616/f77a8776-bebb-4b5d-b129-c88a582b.jpg","https://static.toiimg.com/thumb/msid-81822314,imgsize-81818,width-400,resizemode-4/81822314.jpg"]
    image_html1 = ''
    for url1 in images1:
        image_html1 += f'<img src="{url1}" style="width:1000px; height:300px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html1}</div>""", unsafe_allow_html=True )
# Display page sections


display_header()
display_team_info1()
display_players()
power_bi()
gallery()
display_social_media()
st.sidebar.video("https://youtu.be/2dPDFcvVZy0", start_time=0)
