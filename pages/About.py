import streamlit as st

# Set page config
st.set_page_config(
    page_title="About Us - IPL Analysis",
    page_icon=":guardsman:",
    layout="wide"
)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #DCD0FF;
background-size: 130%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Define the CSS style
css = """
body {
    color: #333;
    background-color: #F8F8FF;
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    line-height: 1.5;
}

a {
    color: #0071C5;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    line-height: 1.2;
    margin-top: 0;
}

h1 {
    font-size: 48px;
    text-align: center;
}

h2 {
    font-size: 36px;
    margin-bottom: 30px;
}

p {
    margin-bottom: 20px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px 20px;
}

.section {
    margin-bottom: 50px;
    padding: 30px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.section h2 {
    font-size: 30px;
    margin-bottom: 20px;
}

.section p {
    font-size: 18px;
    line-height: 1.5;
    margin-bottom: 30px;
    font-color: pink
}

.section ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.section li {
    font-size: 18px;
    line-height: 1.5;
    margin-bottom: 10px;
}

.footer {
    background-color: #01F9C6;
    color: #fff;
    text-align: center;
    padding: 20px;
}

.section-1 {
    background-color: #FFA500;
    border-radius: 20px 20px;
}

.section-1 h2 {
    color: #000080;
}
.section-1 p {
font-size: 25px;
    color: black;
}
.section-2 {
    background-color: #FFE4B5;
    border-radius: 20px 20px;
}

.section-2 h2 {
    color: #A0522D;
}
.section-2 p {
    font-size: 40px;
    color: black;
}
.section-2 li {
    font-size: 25px;
    color: black;
}
.section-3 {
    background-color: #F5F5DC;
    border-radius: 20px 20px;
}

.section-3 h2 {
    color: #808000;
}
.section-3 p {
font-size: 10px;
    color: black;
}
.section-4 {
    background-color: #ADD8E6;
    border-radius: 20px 20px;
}

.section-4 h2 {
    color: #008080;
}
.section-4 p {
    color: black;
}
.section-5 {
    background-color: #01F9C6;
    border-radius: 20px 20px;
    padding: 20px;
}

.section-5 h2 {
    color: #008080;
}
.section-5 p {
    color: black;
}
.section-6 {
    background-color: #98FF98;
    border-radius: 20px 20px;
    padding: 20px;
}

.section-6 h2 {
    color: white;
}
.section-6 h3 {
    color: #38ACEC;
}
.section-6 p {
    color: black;
}
.section-7 {
    background-color: #FFFF33;
    border-radius: 20px 20px;
    padding: 20px;
}

.section-7 h2 {
    color: orange;
}
.section-7 h3 {
    color: #38ACEC;
}
.section-7 p {
    color: black;
}
  .container {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .container img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-right: 20px;
  }
  
  .container div {
    font-size: 25px;
    font-weight: bold;
  }
  
  .container div p {
    margin: 0;
    padding: 5px 0;
  }
  
  .container div p:first-child {
    color: #333;
  }
  
  .container div p:last-child {
    color: #999;
  }

</style>
"""


# Define the HTML content
html_content = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - Ipl Analysis</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:700|Open+Sans&display=swap" rel="stylesheet">
    <style>
    </style>
  </head>
  <body>
  <div class="section section-5">
  <h1>About Us</h1>
</div>
      <div class="section section-1">
        <h2>Our Mission</h2>
        <p>
          Welcome to our IPL analysis website, dedicated to providing comprehensive coverage and insightful analysis of one of the most popular T20 cricket leagues in the world. Our team of experienced analysts and passionate cricket fans strive to bring you the latest news, match previews, player statistics, and much more, all in one convenient location. Whether you're a die-hard fan or a casual observer, we have everything you need to stay on top of the action and make the most of the IPL season.
        </p>
      </div>
 <div class="section section-7">
  <h2>Libraries Used</h2>
  <ul>
    <li>Pandas</li>
    <li>Numpy</li>
    <li>Matplotlib</li>
    <li>Streamlit</li>
    <li>Pickle</li>
    <li>Sklearn-RandomForest</li>
    <li>Season</li>
  </ul>
      </div>
            <div class="section section-6">
       <h2>References</h2>
  <h3>Streamlit</h3>
  <ul>
    <li>https://streamlit.io/</li>
    <li>https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/</li>
    <li>https://www.analyticsvidhya.com/blog/2021/06/build-web-app-instantly-for-machine-learning-using-streamlit/</li>
  </ul>
  <h3>HTML</h3>
  <ul>
    <li>https://www.w3schools.com/html/</li>
    <li>https://www.javatpoint.com/html-tutorial</li>
    <li>https://www.geeksforgeeks.org/html/</li>
    <li>https://www.tutorialspoint.com/html/index.htm</li>
    <br><br>
      </div>
    <div class="section section-2">
  <h2>Our Team</h2>
  <div class="container">
    <img src="https://www.pngitem.com/pimgs/m/537-5372558_flat-man-icon-png-transparent-png.png" alt="Subash S">
    <div>
      <p>Subash S</p>
      <p>Email: 21pd36@psgtech.ac.in</p>
    </div>
  </div>
  <div class="container">
    <img src="https://www.pngitem.com/pimgs/m/248-2483089_ubud-monkey-forest-flat-design-flat-icon-person.png" alt="Deeksha V K">
    <div>
      <p>Deeksha V K</p>
      <p>Email: 21pd37@psgtech.ac.in</p>
    </div>
  </div>
</div>
    <div class="section section-4">
        <h2>Contact Us</h2>
        <p>
          If you have any questions or feedback, please don't hesitate to reach out to us.
        </p>
        <p>
          Email: 21pd36@psgtech.ac.in<br>   21pd37@psgtech.ac.in<br>
          Phone: 555-555-5555<br>
          Address: PSG COLLEGE OF TECHNOLOGY,CBE-641004
        </p>
      </div>
    </div>
    <footer class="footer">
      <p>&copy; 2023 IPL ANALYSIS</p>
    </footer>
  </body>
</html>

"""

st.markdown(html_content, unsafe_allow_html=True)

st.write(f'<style>{css}</style>', unsafe_allow_html=True)
