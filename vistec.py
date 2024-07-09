import streamlit as st
from datetime import datetime
import pytz

import pyodbc


cnxn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                + "instructiondata.database.windows.net"
                + ";DATABASE="
                + "db_instruction"
                + ";UID="
                + "adminbeer"
                + ";PWD="
                + "Beer1234"
            )
cursor = cnxn.cursor()

def reconnect():
    cnxn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                + "instructiondata.database.windows.net"
                + ";DATABASE="
                + "db_instruction"
                + ";UID="
                + "adminbeer"
                + ";PWD="
                + "Beer1234"
            )
    cursor = cnxn.cursor()
    return cursor, cnxn

def app():
    if st.session_state['loggedIn'] == False:
        if st.session_state['userName'].upper() != 'admin' or st.session_state['userName'].upper() != 'ADMIN1':
            st.error("Please login")
            st.stop()

    
    cursor, cnxn = reconnect()
    while True:
        if not cnxn:
            cursor, cnxn = reconnect()
            print("ok")
        else:
            break
    

       #st.subheader(df_new1[0][0], divider='rainbow')
    df_count = cursor.execute("SELECT COUNT(*) from TD_vistec_chk WHERE comment != '' and Date_actor_wang IS NULL;")
    df_count = df_count.fetchall() 

    df_count_vistec = cursor.execute("SELECT COUNT(*) FROM TD_insert where review_status = 'PASS'")
    df_count_vistec = df_count_vistec.fetchall() 

    df_count_pass = cursor.execute("SELECT COUNT(*) FROM [dbo].[TD_vistec_chk] where comment = '' or review_wang = 'แก้ไขแล้ว' or review_final_vistec = 'แก้ไขแล้ว'")
    df_count_pass = df_count_pass.fetchall()

    st.subheader("Summary VISTEC", divider='rainbow')
    st.subheader("Waiting Vistec Check: " + str(int(df_count_vistec[0][0]) - int(df_count_pass[0][0]) ))
    st.subheader("Waiting Wang Check: " + str(df_count[0][0]))
    st.subheader("Total Pass: " + str(df_count_pass[0][0]))

    for i in range(0,8):
        jj = 'admin' + str(i)
        if i == 0:
            jj = 'admin' 
        st.subheader(jj, divider='rainbow')
        user = cursor.execute("SELECT * from TD_user WHERE username = {} ;".format("'"+jj+ "'"))
        user = user.fetchall() 
        #print(len(user))
        if len(user) > 0:
            

            waitt = cursor.execute("SELECT COUNT(*) from dbo.View_vistec_check WHERE Actor_vistec = {}  and vistec_chk IS NOT NULL and vistec_chk IS NOT NULL and vistec_chk > DATEADD(DAY, 1, DATEADD(DAY, 1-DATEPART(WEEKDAY, GETDATE()), CAST(GETDATE() AS DATE)))   and  vistec_chk < DATEADD(DAY, 2, DATEADD(DAY, 7-DATEPART(WEEKDAY, GETDATE()), CAST(GETDATE() AS DATE)));".format("'"+jj+ "'"))
            waitt = waitt.fetchall() 
            #print(waitt[0][0])
            st.markdown("This week (Done) ===> " + str(waitt[0][0]))
            #st.markdown("jobs " + jj +' ===> '+ str(user[0][0]))
    
    