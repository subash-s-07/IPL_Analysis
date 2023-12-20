# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:24:51 2023

@author: DELL
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import mysql.connector
from PIL import Image
import time
def sql(statement):
   mydb = mysql.connector.connect(host='localhost',user='user1',password='1234',database='IPL')
   mycursor = mydb.cursor()
   mycursor.execute(statement)
   result = mycursor.fetchall()
   print(result)
   import pandas as pd
   query = statement
   data= pd.read_sql(query,mydb)
   data=pd.DataFrame(data)
   print(data.head(5))
   return data
# Set the page configuration to include a background image
#st.set_page_config(page_title="IPL Visuvalisations and Predictions", page_icon=":guardsman:", layout="wide", initial_sidebar_state="expanded",)

# Define the CSS style for the page background
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]
{
background_color: rgba(0,0,0,0);
background-image: url("https://c4.wallpaperflare.com/wallpaper/161/464/956/cricket-ball-cricket-bat-cork-ball-5k-wallpaper-preview.jpg");
background-size: cover;
}
</style>
'''
st.set_page_config(page_title="Model", layout="wide")
# Display the background image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add some text to the page
st.markdown("""
    # Welcome to Visuvalisation page :cricket_bat_and_ball:""")

tab1, tab2, tab3 = st.tabs(["Overview", "Data Visuvalisations","Prediction Model"])

with tab1:
   st.header("An Overview :writing_hand:")
   st.write(''' #####  The Indian Premier League (IPL) is a popular Twenty20 cricket league in India. 
      IPL data visualization can help to analyze and understand various aspects of the league such as team performance, player performance, and game statistics.
      Data visualization can be a useful tool for gaining insights into IPL data and understanding the trends and patterns in the league''')
   st.image("https://etimg.etb2bimg.com/photo/74508790.cms", width=1000)

with tab2:
   st.header("Data and Visuvalisation :technologist:")

   st.subheader("1.Best Bowling Economy")
   # Load the data
   chart_data = sql('SELECT * FROM `best bowling economy per innings all seasons combine`;')
   # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe1'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization1'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='Econ', ascending=False).head(30)
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["Econ"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Best Bowling Economy')
      ax.set_xlabel('Econ')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=5)
   
      # Display the plot
      st.pyplot(fig)

   st.subheader("2.Best Bowling Strike")
   chart_data = sql('SELECT * FROM `best bowling strike rate per innings all seasons combine`;')
   # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe2'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization2'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='SR', ascending=True).head(30) #
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["SR"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Best Bowling Strike')
      ax.set_xlabel('Strike Rating')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=5)
   
      # Display the plot
      st.pyplot(fig)

   st.subheader("3.Most Fours Per Innings")
   chart_data = sql('SELECT * FROM `most fours per innings all seasons combine`;')
   # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe3'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization3'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='4s', ascending=False).head(30) #
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["4s"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Most Fours Per Innings')
      ax.set_xlabel('Fours')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=4)
   
      # Display the plot
      st.pyplot(fig)

   st.subheader("4.Most Sixes Per Innings")
   chart_data =sql('SELECT * FROM `most sixes per innings all seasons combine`;')
   # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe4'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization4'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='6s', ascending=False).head(30) #
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["6s"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Most Sixs Per Innings')
      ax.set_xlabel('Sixs')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=5)
   
      # Display the plot
      st.pyplot(fig)

   st.subheader("5.Most Dot Balls Per Innings ")
   chart_data = sql('SELECT * FROM `most dot balls per innings all seasons combine`;')
   # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe5'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization5'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='Dots', ascending=False).head(30) #
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["Dots"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Most Dot Balls Per Innings')
      ax.set_xlabel('Dot Balls')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=5)
   
      # Display the plot
      st.pyplot(fig)

   st.subheader("6.Most Runs")
   chart_data =sql('SELECT * FROM `most runs all seasons combine`;')
      # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe6'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization6'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='Runs', ascending=False).head(30) #
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["Runs"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Most Runs')
      ax.set_xlabel('Runs')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=5)
   
      # Display the plot
      st.pyplot(fig)
   
   st.subheader("7.Most Wickets")
   chart_data =sql('SELECT * FROM `most wickets all seasons combine`;')
      # Display the dataframe if checkbox is selected
   if st.checkbox('Show dataframe7'):
      st.write(chart_data)

   # Display the visualization if checkbox is selected
   if st.checkbox('Show visualization7'):
      # Sort the data by economy rate in descending order and select the top 50 players
      top_players = chart_data.sort_values(by='Wkts', ascending=False).head(30) #
      
      # Define the x and y values for the bar chart
      x = top_players["Player"]
      y = top_players["Wkts"]
      
      # Create a bar chart with customized colors
      fig, ax = plt.subplots()
      ax.barh(x, y, color=['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#ffa600', '#ffa600', '#ffa600'])
      
      # Add a horizontal grid line and set the title and axis labels
      ax.yaxis.grid(True)
      ax.set_title('Most Wickets')
      ax.set_xlabel('Wickets')
      ax.set_ylabel('Player')
      plt.yticks(fontsize=5)
   
      # Display the plot
      st.pyplot(fig)

with tab3:
   col1, col2, col3 = st.columns([1,3,1])
   with col1:
      size=(500,1000)
      image_paths = ['D:\davl project\IPL\Code\pages\\all.jpg']
      image_placeholder = st.empty()
      index = 0
      st.markdown("<br><hr>", unsafe_allow_html=True)
      st.markdown(
         """
         <style>
         .icon-container {
               bottom: 20px;
               right: 20px;
         }
         .icon-container a {
               margin-left: 10px;
         }
         </style>
         """,unsafe_allow_html=True)
      path = image_paths[index]
      image = Image.open(path)
      image = image.resize(size)
      image_placeholder.image(image)
   with col2:
      st.markdown("<h1 style='text-align: center; color: teal;'>Start Predicting</h1>", unsafe_allow_html=True)
      match=pd.read_csv("D:\davl project\subash\prediction_data\matches.csv")
      delivery=pd.read_csv("D:\davl project\subash\prediction_data\deliveries.csv")
      total_score_df=delivery.groupby(["match_id","inning"]).sum()["total_runs"].reset_index()
      total_score_df=total_score_df[total_score_df["inning"]==1]
      match_df=match.merge(total_score_df[["match_id","total_runs"]],left_on="id",right_on="match_id")
      match_df["team1"].unique()
      teams=['Sunrisers Hyderabad', 
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']
      match_df['team1'] = match_df['team1'].str.replace('Delhi Daredevils','Delhi Capitals')
      match_df['team2'] = match_df['team2'].str.replace('Delhi Daredevils','Delhi Capitals')
      match_df['team1'] = match_df['team1'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
      match_df['team2'] = match_df['team2'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
      match_df = match_df[match_df['team1'].isin(teams)]
      match_df = match_df[match_df['team2'].isin(teams)]
      match_df = match_df[match_df['dl_applied'] == 0]
      match_df = match_df[['match_id','city','winner','total_runs']]
      delivery_df = match_df.merge(delivery,on='match_id')
      delivery_df=delivery_df[delivery_df["inning"]==2]
      delivery_df["current_score"]=delivery_df.groupby("match_id").cumsum()["total_runs_y"]
      delivery_df["Runs_left"]=delivery_df["total_runs_x"]-delivery_df["current_score"]+1
      delivery_df["balls_left"]=126 - delivery_df["over"]*6 - delivery_df["ball"]
      delivery_df['player_dismissed'] = delivery_df['player_dismissed'].fillna("0")
      delivery_df['player_dismissed'] = delivery_df['player_dismissed'].apply(lambda x:x if x == "0" else "1")
      delivery_df['player_dismissed'] = delivery_df['player_dismissed'].astype('int')
      wickets = delivery_df.groupby('match_id').cumsum()['player_dismissed'].values
      delivery_df['wickets_left'] = 10 - wickets
      delivery_df['crr'] = (delivery_df['current_score']*6)/(120 - delivery_df['balls_left'])
      delivery_df['rrr'] = (delivery_df['Runs_left']*6)/delivery_df['balls_left']
      def result(row):
         return 1 if row['batting_team'] == row['winner'] else 0
      delivery_df['result'] = delivery_df.apply(result,axis=1)
      final_df = delivery_df[['batting_team','bowling_team','city','Runs_left','balls_left','wickets_left','total_runs_x','crr','rrr','result']]
      st.selectbox('Select Batting team', teams)
      st.selectbox('Select Bowling Team', teams)
      if st.button('Predict'):
         st.image("https://whiteandblack.in/wp-content/uploads/2021/04/IPL-teams-logo-design-breakdown-scaled.jpg")
         st.markdown(''' ### Data for prediction ''')
         st.write(final_df)
         final_df = final_df.sample(final_df.shape[0])
         #final_df.head()
         final_df.dropna(inplace=True)
         final_df = final_df[final_df['balls_left'] != 0]
         X = final_df.iloc[:,:-1]
         y = final_df.iloc[:,-1]
         X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
         trf = ColumnTransformer([('trf',OneHotEncoder(sparse=False,drop='first'),['batting_team','bowling_team','city'])],remainder='passthrough')
         pipe =Pipeline(steps=[
         ("step1",trf),
         ("step2",LogisticRegression(solver="liblinear"))])
         pipe.fit(X_train,y_train)
         y_pred= pipe.predict(X_test)
         acc_score = accuracy_score(y_pred,y_test)
         st.write("##### The Accuravy Score is : %.5f"%acc_score)
         def match_progression(x_df,match_id,pipe):
            match = x_df[x_df['match_id'] == match_id]
            match = match[(match['ball'] == 6)]
            temp_df = match[['batting_team','bowling_team','city','Runs_left','balls_left','wickets_left','total_runs_x','crr','rrr']].dropna()
            temp_df = temp_df[temp_df['balls_left'] != 0]
            result = pipe.predict_proba(temp_df)
            temp_df['lose'] = np.round(result.T[0]*100,1)
            temp_df['win'] = np.round(result.T[1]*100,1)
            temp_df['end_of_over'] = range(1,temp_df.shape[0]+1)
            
            target = temp_df['total_runs_x'].values[0]
            runs = list(temp_df['Runs_left'].values)
            new_runs = runs[:]
            runs.insert(0,target)
            temp_df['runs_after_over'] = np.array(runs)[:-1] - np.array(new_runs)
            wickets = list(temp_df['wickets_left'].values)
            new_wickets = wickets[:]
            new_wickets.insert(0,10)
            wickets.append(0)
            w = np.array(wickets)
            nw = np.array(new_wickets)
            temp_df['wickets_in_over'] = (nw - w)[0:temp_df.shape[0]]
            
            print("Target-",target)
            temp_df = temp_df[['end_of_over','runs_after_over','wickets_in_over','lose','win']]
            return temp_df,target
         temp_df,target = match_progression(delivery_df,74,pipe)
         st.write('''### Match Progression DataFrame''')
         st.write(temp_df)
         plt.figure(figsize=(18,8))
         plt.plot(temp_df['end_of_over'],temp_df['wickets_in_over'],color='yellow',linewidth=3)
         plt.plot(temp_df['end_of_over'],temp_df['win'],color='#00a65a',linewidth=4)
         plt.plot(temp_df['end_of_over'],temp_df['lose'],color='red',linewidth=4)
         plt.bar(temp_df['end_of_over'],temp_df['runs_after_over'])
         plt.title('Target-' + str(target))
         st.write('''### Match Progression :chart_with_upwards_trend:''')
         st.pyplot(plt)

   with col3:
      size=(500,1000)
      image_paths = ['D:\davl project\IPL\Code\pages\\csk.jpg', 'D:\davl project\IPL\Code\pages\\dc.jpg','D:\davl project\IPL\Code\pages\\kol.jpg','D:\davl project\IPL\Code\pages\\mi.jpg','D:\davl project\IPL\Code\pages\\rcb.jpg','D:\davl project\IPL\Code\pages\\rr.jpg','D:\davl project\IPL\Code\pages\\rr.jpg']
      delay = 3
      image_placeholder = st.empty()
      index = 0
      st.markdown("<br><hr>", unsafe_allow_html=True)
      st.markdown(
         """
         <style>
         .icon-container {
               bottom: 20px;
               right: 20px;
         }
         .icon-container a {
               margin-left: 10px;
         }
         </style>
         """,unsafe_allow_html=True)
      #n=1
      while(True):
         path = image_paths[index]
         image = Image.open(path)
         image = image.resize(size)
         image_placeholder.image(image)
         time.sleep(delay)
         image_placeholder.empty()
         index = (index + 1) % len(image_paths)
         #n+=1
    