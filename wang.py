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
    #print("====> ",st.session_state)
    if st.session_state['loggedIn'] == False or (st.session_state['userName'].upper() != 'ADMIN18' and st.session_state['userName'].upper() != 'ADMIN19'):
        st.error("Please login")
        st.stop()
    st.session_state['ids'] = []
    
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

    df_count_finish = cursor.execute("SELECT COUNT(*) from TD_vistec_chk WHERE (comment != '' and comment_wang = '' ) or (comment_final_vistec = '');")
    df_count_finish = df_count_finish.fetchall() 

    df_count_cannot = cursor.execute("SELECT COUNT(*) from TD_vistec_chk WHERE (comment_wang != '' ) or (comment_final_vistec != '');")
    df_count_cannot = df_count_cannot.fetchall()

    st.subheader("Summary", divider='rainbow')
    st.subheader("Waiting Jobs: " + str(df_count[0][0]))
    st.subheader("Finished Jobs: " + str(df_count_finish[0][0]))
    st.subheader("Cannot edit: " + str(df_count_cannot[0][0]))
    #st.subheader("", divider='rainbow')
    for i in range(11,21):
        jj = 'admin' + str(i)
        st.subheader(jj, divider='rainbow')
        user = cursor.execute("SELECT jobs from TM_related_job WHERE username = {} ;".format("'"+jj+ "'"))
        user = user.fetchall() 
        #print(len(user))
        if len(user) > 0:
            #print(user[0][0])
            B_list = [ 'article_id like ' +f"'%{item.strip()}'" for item in user[0][0].split(',')]
            #print(B_list)
            y1 = "("
            for hhh in B_list:
                y1 =y1 + hhh + " or "

            y1 = y1[:-3] + ")"
            #print(y1)

            waitt = cursor.execute("SELECT COUNT(*) from TD_vistec_chk WHERE comment != '' and Date_actor_wang IS NULL and {};".format(y1))
            waitt = waitt.fetchall() 
            #print(waitt[0][0])
            st.markdown("waiting " + jj +' ===> '+ str(waitt[0][0]))
            st.markdown("jobs " + jj +' ===> '+ str(user[0][0]))
    
    with st.form(key="vendor_form1" , clear_on_submit=True):
        actor = cursor.execute("SELECT username from TM_related_job ;".format(y1))
        actor = actor.fetchall() 
        all_actor = [""]
        for kkk in actor:
            all_actor.append(kkk[0])
        act1 = st.selectbox("Actors", options=all_actor)
        text1 = st.text_area(label="Update Jobs*", height= 200, value="")

        submit_button = st.form_submit_button(label="Submit Details")
        if submit_button:
            if act1 != '' and text1 != '':
                update_query = """
                                    UPDATE TM_related_job
                                    SET jobs = ?
                                    WHERE username = ?
                                """
                #row2 = (text1.strip())
                cursor.execute(update_query, (text1.strip(), act1))
                cnxn.commit()
                st.success("Details successfully submitted!")
                st.rerun()

