#-------------------------------------------------------------------------------
# Name:        Valentine_Gift
# Purpose:
#
# Author:      Sundus Yawar
#
# Created:     12-02-2022
# Copyright:   (c) Sundus Yawar 2022
# Licence:     <MIT>
#-------------------------------------------------------------------------------
import mariadb
import sys
import pandas as pd
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASS')

#=================================

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=os.getenv('USER'),
        password=os.getenv('PASS'),
        host="127.0.0.1",
        port=3306,
        database="valentine"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

#=== example of how you can populate tables via mariadb connector for python
place="Mississauga Celebration Square"
image="shorturl.at/hEKMP"
act_desc="Goose Chase Contest"
mapLink_ ="shorturl.at/ouwE1"
free_event ="YES"
na = "N/A"
ev_dur ="till March 20, 2022"
cur.execute("INSERT IGNORE INTO recreation (id,place,image,activity_description,map,free_event,price,link_to_booking,event_duration) VALUES (?,?,?,?,?,?,?,?,?)",
(1,place,image,act_desc,mapLink_,free_event,na,na,ev_dur))
conn.commit() #must commit for changes to show up in the db

#=====streamlit
st.title("💖 Valentine Gift 💝")
page = st.selectbox('Page',('Recreation/Entertainment','Romantic Meals','Romantic Desserts'))
if page == 'Recreation/Entertainment':
    st.write("Hey! Did you know there are 12,418,440 single people in Canada? (stats canada)")
    st.write("Yet many feel like they are the only one single on Valentines Day.")
    st.write("Well who says Valentines day is for couples only? Valentines Day is about LOVE! 🌹")
    st.write("So, show yourself some love and take yourself on a date! 😉")
    SQL_Query = pd.read_sql_query('''SELECT * FROM recreation ORDER BY price ASC''',conn)
    df = pd.DataFrame(SQL_Query, columns=['id','place','image','activity_description','map','free_event','price','link_to_booking','event_duration'])
    
    left_aligned_df = df.style.set_properties(**{'background-color':'pink','color':'black','border-color':'red','text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'centre')])])
    st.table(left_aligned_df)
    
elif page == 'Romantic Meals':
    st.write("Treat yourself with these romantic dishes.")
    st.write("If people can make extravagant meals for a loved one.")
    st.write("Why not make it for yourself? You deserve some love too!💖")
    SQL_Query = pd.read_sql_query('''SELECT * FROM rom_cooking ORDER BY cookTimeInMins ASC''',conn)
    df = pd.DataFrame(SQL_Query, columns=['id','nameOfDish','description','recipeLink','cookTimeInMins'])
    
    left_aligned_df = df.style.set_properties(**{'background-color':'pink','color':'black','border-color':'red','text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'centre')])])
    st.table(left_aligned_df)

elif page == 'Romantic Desserts':
    st.write("Treat yourself with these romantic desserts.")
    st.write("Mmmmm.... so mouthwatering! 💖")
    SQL_Query = pd.read_sql_query('''SELECT * FROM desserts ORDER BY totalTimeInMins ASC''',conn)
    df = pd.DataFrame(SQL_Query, columns=['id','name','recipeLink','totalTimeInMins'])
    
    left_aligned_df = df.style.set_properties(**{'background-color':'pink','color':'black','border-color':'red','text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'centre')])])
    st.table(left_aligned_df)

