import base64
import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import json
import requests
st.set_page_config(layout="wide")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("107468-bouncing-cricket-ball.json")


st.markdown("<h1 style='text-align: center; color : #00008B; font-size:55px'>IPL ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<br><hr>", unsafe_allow_html=True)
#st.image("LOGO.png")
st.markdown("""
    <style>
    .img1 {
        max-width: 500px;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center;">
        <img src="https://wallpaperaccess.in/public/uploads/preview/tata-ipl-2022-logo-png-images-z.png" alt="Your Image" class="img1">
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    .img {
        max-width: 100px;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)
#st_lottie(lottie_coding,key="HELLO",width=500)
st.markdown("""
    <div style="text-align:center;">
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png" alt="Your Image" class="img">
        <img src="https://www.delhicapitals.in/static-assets/images/cssimages/logo.png" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/0/09/Gujarat_Titans_Logo.svg" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg" alt="Your Image" class="img">
        <img src="https://iplmatcheslive.com/wp-content/uploads/2023/03/Lucknow-Super-Giants-2048x2048.png" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Rajasthan_Royals_Logo.svg/1024px-Rajasthan_Royals_Logo.svg.png" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Royal_Challengers_Bangalore_2020.svg/800px-Royal_Challengers_Bangalore_2020.svg.png" alt="Your Image" class="img">
        <img src="https://upload.wikimedia.org/wikipedia/en/e/eb/Sunrisers_Hyderabad.png" alt="Your Image" class="img">

    </div>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:35px'>Highlights</p>", unsafe_allow_html=True)

images = ["https://www.mumbaiindians.com/static-assets/waf-images/d1/85/18/21-9/1200-675/icOTMY7y37.jpeg", "https://images.thequint.com/thequint%2F2021-04%2F15d4fcf5-7c0e-481e-9dc6-37e444c58fef%2FIPL21M8_55.JPG?rect=0%2C0%2C3872%2C2178&auto=format%2Ccompress&fmt=webp&width=720","https://img1.hscicdn.com/image/upload/f_auto,t_ds_w_1280,q_70/lsci/db/PICTURES/CMS/346400/346456.4.jpg","https://c.ndtvimg.com/2023-03/7v2ldgro_rahul-dravid_625x300_13_March_23.jpg?im=FeatureCrop,algorithm=dnn,width=806,height=605"]
urls=["https://news.abplive.com/sports/ipl/ipl-2023-mumbai-indians-unveil-new-blue-gold-jersey-watch-1587567","https://www.msn.com/en-in/sports/cricket/ms-dhoni-was-quickest-runner-between-wickets-after-ab-de-villiers-virat-kohli-makes-big-revelation/ar-AA18SMjA","https://www.republicworld.com/sports-news/cricket-news/ben-stokes-left-fuming-as-his-luggage-gets-stolen-in-london-shares-angry-post-on-twitter-articleshow.html","http://localhost:8503"]
image_html = ''
for url in range(len(images)):
    image_html += f'<a href={urls[url]} target = "_blank"><img src="{images[url]}" style="width:1000px; height:500px; object-fit: cover; display: block;margin-right: 40px;"></a>'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr>", unsafe_allow_html=True)
images = ["https://www.insidesport.in/wp-content/uploads/2023/02/1676632383158_TATA-IPL-2023-Match-Schedule_page-0001-1.jpg","https://www.insidesport.in/wp-content/uploads/2023/02/1676632383158_TATA-IPL-2023-Match-Schedule_page-0002-2.jpg"]
st.markdown("<p style='text-align: center; font-size:35px'>Schedule</p>", unsafe_allow_html=True)
image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:1000px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><br><br><hr>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size:35px'>EPIC MOMENTS</p>", unsafe_allow_html=True)
images1=["https://www.sportzcraazy.com/wp-content/uploads/2020/09/144806-pebhcuszkw-1595405483.jpg","https://www.sportzcraazy.com/wp-content/uploads/2020/09/CSKjpg.jpg","https://www.sportzcraazy.com/wp-content/uploads/2020/09/with-a-bloodied-knee-amp-immense-pain-shane-watson-almost-won-the-ipl-for-csk-amp-deserves-respect1200-1557815180_1200x900.jpg","https://www.sportzcraazy.com/wp-content/uploads/2020/09/i.jpg","https://www.sportzcraazy.com/wp-content/uploads/2020/08/Chris-Gayle-in-IPL.jpg","https://www.sportzcraazy.com/wp-content/uploads/2020/09/0.7617508193272753.jpeg","https://www.sportzcraazy.com/wp-content/uploads/2020/09/maxresdefault.jpg","https://c.ndtvimg.com/2021-04/gpvre1p8_ms-dhoni-yuzvendra-chahal-twitter_625x300_26_April_21.jpg?output-quality=80&downsize=639:*"]
image_html1 = ''
for url1 in images1:
    image_html1 += f'<img src="{url1}" style="width:1000px; height:300px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html1}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:35px'>2022 SEASON</p>", unsafe_allow_html=True)
images = [ "https://scores.iplt20.com/ipl/playerimages/182.png","https://scores.iplt20.com/ipl/playerimages/10.png","https://scores.iplt20.com/ipl/playerimages/170.png","https://scores.iplt20.com/ipl/playerimages/9.png","https://scores.iplt20.com/ipl/playerimages/182.png","https://scores.iplt20.com/ipl/playerimages/190.png"]
urls=["https://scores.iplt20.com/ipl/teamlogos/RR.png","https://scores.iplt20.com/ipl/teamlogos/RR.png","https://scores.iplt20.com/ipl/teamlogos/LSG.png","https://scores.iplt20.com/ipl/teamlogos/MI.png","https://scores.iplt20.com/ipl/teamlogos/RR.png","https://scores.iplt20.com/ipl/teamlogos/RR.png"]
color=["orange","purple","blue","red","pink","green"]
topic=["Orange cap-863 RUNS","Purple cap-27 WICKETS","Highest Score-140*","Best Bowling Figure-5/10","Most Valube Player","Paytm Fairplay"]
name=["Jos Buttler",'Y Chahal','Quinton de Kock','Jasprit Bumrah','Jos Buttler','Sanju Samson']
image_html = ''
for url in range(len(images)):
    image_html += f"""<div style="display: inline-block; margin-right: 20px;">
<div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background-color: {color[url]};border-radius: 20px 20px 0 0;">
        <img src="{images[url]}" />
        <img src="{urls[url]}" style="position: absolute; top: 10px; right: 10px; width: 50px; height: 50px; object-fit: cover;" />
        <div style="position: absolute; bottom: 10px; left: 10px; background-color: white; color: {color[url]}; padding: 10px; border-radius: 20px;">"{topic[url]}"</div>
        </div>
        <div style="background-color: black; color: white; padding: 10px; width: 250px;border-radius: 0 0 20px 20px;">"{name[url]}"</div>
        </div>"""
st.markdown(f"""<div style="white-space: nowrap; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:35px'>WINNERS</p>", unsafe_allow_html=True)
ipl_winners = {
    2008: "Rajasthan Royals",
    2009: "Deccan Chargers",
    2010: "Chennai Super Kings",
    2011: "Chennai Super Kings",
    2012: "Kolkata Knight Riders",
    2013: "Mumbai Indians",
    2014: "Kolkata Knight Riders",
    2015: "Mumbai Indians",
    2016: "Sunrisers Hyderabad",
    2017: "Mumbai Indians",
    2018: "Chennai Super Kings",
    2019: "Mumbai Indians",
    2020: "Mumbai Indians",
    2021: "Chennai Super Kings",
    2022:"Gujarat Titans"
}

# Define the images and colors
images = [
    "https://scores.iplt20.com/ipl/teamlogos/RR.png",
    "https://upload.wikimedia.org/wikipedia/en/a/a6/HyderabadDeccanChargers.png",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png",
    "https://scores.iplt20.com/ipl/teamlogos/KKR.png",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg",
    "https://scores.iplt20.com/ipl/teamlogos/KKR.png",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg",
    "https://scores.iplt20.com/ipl/teamlogos/SRH.png",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png",
    "https://scores.iplt20.com/ipl/teamlogos/MI.png",
    "https://scores.iplt20.com/ipl/teamlogos/MI.png",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/300px-Chennai_Super_Kings_Logo.svg.png",
    "https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/GT/Logos/Medium/GTmedium.png"
]

colors = [
    "pink",
    "purple",
    "yellow",
    "yellow",
    "purple",
    "blue",
    "purple",
    "blue",
    "orange",
    "blue",
    "yellow",
    "blue",
    "blue",
    "yellow",
    "blue"
]


element_html = ''
for year, team in ipl_winners.items():
    index = list(ipl_winners.keys()).index(year)
    element_html += f"""<div style="display: inline-block; margin-right: 20px;">
<div style="position: relative; height: 300px; width: 250px; overflow: hidden; object-fit: cover; background: linear-gradient(to bottom, {colors[index]}, #ffffff); border-radius: 20px 20px 0 0;">
        <img src="{images[index]}" style="max-height:100%; max-width:100%;" />
        <div style="position: absolute; bottom: 10px; left: 10px; background-color: white; color: {colors[index]}; padding: 10px; border-radius: 20px;">{year}</div>
        </div>
        <div style="background-color: black; color: white; padding: 10px; width: 250px;border-radius: 0 0 20px 20px;">{team}</div>
        </div>"""

st.markdown(f"""<div style="white-space: nowrap; overflow-x: scroll; padding: 10px 0;">{element_html}</div>""", unsafe_allow_html=True )
#Latest News
st.markdown("""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="container">
  <h2>News</h2>
  <ul class="cards">
    <li class="card">
    <img src="https://img1.hscicdn.com/image/upload/f_auto,t_ds_w_1280,q_70/lsci/db/PICTURES/CMS/309900/309901.4.jpg" style="width:98%">
      <div><br>
        <h4 class="card-title">IPL insists on seven-day isolation period for Covid-19 cases</h4>
        <div class="card-content">
          <p>While the Covid-19 vaccines are saving lives, some side effects related to heart has been reported..</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://www.espncricinfo.com/story/ipl-insists-on-seven-day-isolation-period-for-covid-19-cases-1364178" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
    <img src="https://static.tnn.in/photo/msid-98741914,imgsize-1473501,updatedat-1679084522394,width-1280,height-720,resizemode-75/98741914.jpg" alt="news2" style="width:98%">
      <div><br>
        <h4 class="card-title">It's happening, everybody stay calm! Ben Stokes' latest update ahead of IPL 2023 sends CSK fans into frenzy</h4>
        <div class="card-content">
          <p>The Chennai Super Kings (CSK) fans have been waiting with bated breath to see England Test captain Ben Stokes in yellow since the star..</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://www.timesnownews.com/sports/cricket/its-happening-everybody-stay-calm-ben-stokes-latest-update-ahead-of-ipl-2023-sends-ms-dhoni-led-csk-fans-into-frenzy-article-98741876" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://english.cdn.zeenews.com/sites/default/files/styles/zm_700x400/public/2023/03/18/1169460-dhoni.png" alt="news3" style="width:98%">
      <div><br>
        <h4 class="card-title">IPL 2023: Harbhajan Singh Breaks Silence On Rift Rumours With MS Dhoni</h4>
        <div class="card-content">
          <p> 2011 World Cup winner of Team India, Harbhajan Singh recently cleared the air on having a bad relationship with former India captain MS Dhoni. ..</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://zeenews.india.com/cricket/ipl-2023-harbhajan-singh-breaks-silence-on-rift-rumours-with-ms-dhoni-2585143.html" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://static.toiimg.com/thumb/msid-98751728,imgsize-31782,width-400,resizemode-4/98751728.jpg" alt="news4" style="width:98%">
      <div><br>
        <h4 class="card-title">IPL 2023: Michael Bracewell replaces injured Will Jacks in RCB squad</h4>
        <div class="card-content">
          <p>New Zealand all-rounder Michael Bracewell has injured in RCB.</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://timesofindia.indiatimes.com/sports/cricket/ipl/top-stories/ipl-2023-michael-bracewell-replaces-injured-will-jacks-in-rcb-squad/articleshow/98751744.cms" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://resize.indiatvnews.com/en/resize/newbucket/730_-/2023/03/e7a5009e-a77d-460e-954a-cd4a4155ef5e-compressed-1-1679055816.jpg" alt="news5" style="width:98%">
      <div><br>
        <h4 class="card-title">Shreyas Iyer advised 10-day rest before IPL availability call is taken </h4>
        <div class="card-content">
          <p>Kolkata Knight Riders are waiting on the fitness condition of Shreyas Iyer and there is no indication if their captain will be able to participate in the forthcoming season of the Indian Premier League (IPL).</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://www.indiatvnews.com/health/chronic-heart-diseases-prevent-heart-problems-with-these-essential-cooking-methods-2023-03-15-854722" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://www.hindustantimes.com/ht-img/img/2023/03/18/550x309/dhoni-new-csk-ipl_1648651191324_1679140011450_1679140011450.jpg" alt="news6" style="width:98%">
      <div><br>
        <h4 class="card-title">'Had 13 successful years in IPL. Still, Dhoni said that to my face': Ex-CSK star  </h4>
        <div class="card-content">
          <p>The 2023 Indian Premier League begins on March 31 with a blockbuster opening clash, as defending champions Gujarat Titans take on the Chennai Super Kings in Ahmedabad. </p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://www.hindustantimes.com/cricket/i-had-13-successful-years-in-ipl-still-he-said-that-to-my-face-ex-csk-star-robin-uthappa-s-brutal-chat-with-ms-dhoni-before-ipl-2021-101679137037964.html" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
     <img src="https://www.hindustantimes.com/ht-img/img/2023/03/17/550x309/image_-_2023-03-17T211244935_1679067887586_1679067887836_1679067887836.jpg" alt="news7" style="width:98%">
      <div><br>
        <h3 class="card-title">Warner leaves priceless message for Rishabh Pant after being appointed Delhi Capitals captain for IPL 2023</h3>
        <div class="card-content">
          <p>Rishabh Pant will not be part of the impending 2023 edition of the Indian Premier League. And unfortunate accident last December ruled him out of Delhi Capitals' campaign for the 16th IPL season..</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://www.hindustantimes.com/cricket/david-warner-leaves-priceless-message-for-rishabh-pant-after-being-appointed-delhi-capitals-captain-for-ipl-2023-101679067795204.html" class="card-link">Learn More</a>
      </div>
    </li>
  </ul>
</div>
</body>
</html>
<style>
:root {
  --red: #ef233c;
  --darkred: #c00424;
  --platinum: #e5e5e5;
  --black: #ADD8E6;
  --white: #fff;
  --thumb: #edf2f4;
}
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
body {
  font: 16px / 24px "Rubik", sans-serif;
  color: var(--white);
  background: var(--black);
  margin: 50px 0;
}
.container {
layout:left
  width: 1200px;
  height:1100px;
  padding: 0 15px;
  margin: 0 auto;
}
h2 {
  font-size: 32px;
  margin-bottom: 1em;
}
.cards {
    width: 1420px;
  height:700px;
  display: flex;
  padding: 25px 0px;
  list-style: none;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
}
.card {
    width: 1220px;
  height:600px;
  display: flex;
  flex-direction: column;
  flex: 0 0 100%;
  padding: 20px;
  background: var(--black);
  border-radius: 12px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 15%);
  scroll-snap-align: start;
  transition: all 0.2s;
}
.card:not(:last-child) {
  margin-right: 10px;
}
.card:hover {
  color: var(--white);
  background:#fe8267;
}
.card .card-title {
  font-size: 20px;
  font-color:red;
}
.card .card-content {
  margin: 20px 0;
  max-width: 85%;
}
.card .card-link-wrapper {
  margin-top: auto;
}
.card .card-link {
  display: inline-block;
  text-decoration: none;
  color: white;
  background: var(--red);
  padding: 6px 12px;
  border-radius: 8px;
  transition: background 0.2s;
}
.card:hover .card-link {
  background: var(--darkred);
}
.cards::-webkit-scrollbar {
  height: 12px;
}
.cards::-webkit-scrollbar-thumb,
.cards::-webkit-scrollbar-track {
  border-radius: 92px;
}
.cards::-webkit-scrollbar-thumb {
  background: var(--darkred);
}
.cards::-webkit-scrollbar-track {
  background: var(--thumb);
}
@media (width: 200%) {
  .card {
    flex-basis: calc(50% - 10px);
  }
  .card:not(:last-child) {
    margin-right: 20px;
  }
}
@media (min-width: 700px) {
  .card {
    flex-basis: calc(calc(100% / 3) - 20px);
  }
  .card:not(:last-child) {
    margin-right: 30px;
  }
}
@media (min-width: 1100px) {
  .card {
    flex-basis: calc(25% - 30px);
  }
  .card:not(:last-child) {
    margin-right: 40px;
  }
}
/* FOOTER STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.page-footer {
  position: fixed;
  right: 0;
  bottom: 50px;
  display: flex;
  align-items: center;
  padding: 5px;
  z-index: 1;
}
.page-footer a {
  display: flex;
  margin-left: 4px;
}
</style>
""",unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.sidebar.video("https://www.youtube.com/watch?v=4I3tRnZDaAc", start_time=0)
st.sidebar.markdown("<br><hr>", unsafe_allow_html=True)
