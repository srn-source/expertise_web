import streamlit as st
import pyodbc
# cnxn = pyodbc.connect(
#                 "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
#                 + st.secrets["server"]
#                 + ";DATABASE="
#                 + st.secrets["database"]
#                 + ";UID="
#                 + st.secrets["username"]
#                 + ";PWD="
#                 + st.secrets["password"]
#             )

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

def signup(userName, password):
    user_add = False
    try:
        cursor, cnxn = reconnect()
        while True:
            if not cnxn:
                cursor, cnxn = reconnect()
                print("ok")
            else:
                break
        j = cursor.execute("SELECT * from TD_user WHERE username = {} and password = {};".format("'"+userName+"'", "'"+password+"'")) 
        count = 0
        
        for row in j:
            count = 1
            #print(row)
        if count == 0:
            row = (userName, password)
            #print(row)
            cursor.execute("INSERT INTO TD_user(username, password) VALUES ({},{})".format("'"+userName+"'", "'"+password+"'"))
            cnxn.commit()
            user_add = True
    except Exception as e:
        #print("The error is: ",e)
        st.error(e)

    return user_add

     
def SignUp_Clicked(userName, password):
    if userName == ""  or password == "":
        st.warning("Ensure all mandatory fields are filled.")
    else:
        if signup(userName, password):
            st.session_state['loggedIn'] = True
            st.session_state['userName'] = userName
            st.success("you already signed up")
        else:
            st.session_state['loggedIn'] = False
            st.error("Invalid user name or password")

def app():
    st.title("Sign Up")
    st.session_state['ids'] = []
    if not st.session_state['loggedIn'] :
        username = st.text_input(label="Username*")
        password = st.text_input(label="Password*" , type="password")
        st.button ("Sign Up", on_click=SignUp_Clicked, args= (username, password))
    else:
        st.markdown("Welcome K'" + st.session_state['userName'])
    
