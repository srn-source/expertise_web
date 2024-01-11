import streamlit as st
import home
import pyodbc
import matplotlib.pyplot as plt

#cnxn = pyodbc.connect(
#                "DRIVER={ODBC Driver 17 for SQL Server};encrypt=no;SERVER="
#                + st.secrets["server"]
#                + ";DATABASE="
#                + st.secrets["database"]
#                + ";UID="
#                + st.secrets["username"]
#                + ";PWD="
#                + st.secrets["password"]
#            )
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
    return cursor

def app():
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    if st.session_state['loggedIn'] :
        st.subheader("Your progress", divider='rainbow')
        labels = 'Done', 'In progress'

        cursor = reconnect()
        while True:
            if not cnxn:
                cursor = reconnect()
            else:
                break
        df_in_progress = cursor.execute("SELECT * from View_info_insert WHERE actor_master = {} and date_insert IS NULL;".format("'"+st.session_state['userName']+ "'"))
        df_in_progress = df_in_progress.fetchall()
        df_done = cursor.execute("SELECT * from View_info_insert WHERE actor_master = {} and date_insert IS NOT NULL;".format("'"+st.session_state['userName']+ "'"))
        df_done = df_done.fetchall()
        sizes = [len(df_done), len(df_in_progress)]
        #print(sizes)
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
        
    else:
        st.error("Please login")
