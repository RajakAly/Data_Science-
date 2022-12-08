import pandas as pd
import streamlit as st
import pickle
team=['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
       'Kolkata Knight Riders', 'Kings XI Punjab',
       'Chennai Super Kings', 'Rajasthan Royals', 
       'Delhi Capitals']
City=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah','Mohali', 'Bengaluru']
pipe=pickle.load(open(r'C:\Users\rajak\OneDrive\Documents\DATA\Data_Science\PROJECTS\IPL_WIN_PREDICTOR\pipe.pkl','rb'))
st.title('IPL WIN PREDICTOR')
col1,col2=st.columns(2)
with col1:
    Batting_Team=st.selectbox('Select the batting team',sorted(team))
with col2:
    Bowling_Team=st.selectbox('Select the bowling team',sorted(team))
City=st.selectbox('Select the venue of the match',sorted(City))   
Target=st.number_input('Target',step='int')
col3,col4,col5=st.columns(3)
with col3:
    Score=st.number_input('Score',step='int')
with col4:
    Over=st.number_input('Over Completed',step='int')
with col5:
 Wicket=st.number_input('Wickets Fallen',step='int')         
if st.button('Winning Prediction'):
    Runs_left=Target-Score
    Balls_left=120-Over*6
    CRR=Score/Over
    RRR=(Runs_left*6)/Balls_left
    
    input_df=pd.DataFrame({'Batting_team':[Batting_Team],'Bowling_team':[Bowling_Team],'City':[City],'Runs_left':[Runs_left],'Ball_left':[Balls_left],
                           'Wickets':[Wickets],'Total_runs_x':[Target],'CRR':[CRR],'RRR':[RRR]})
    Result=pipe.predict_proba(input_df)
    Loss=Result[0][0]
    Win=Result[0][1]
    st.header(Batting_Team+"- "+str(round(Win*100,2))+"%")
    st.header(Bowling_Team+"- "+str(round(Loss*100,2))+"%")
    
