
import streamlit as st
import home
import pyodbc

cnxn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};encrypt=no;SERVER="
                + st.secrets["server"]
                + ";DATABASE="
                + st.secrets["database"]
                + ";UID="
                + st.secrets["username"]
                + ";PWD="
                + st.secrets["password"]
            )

cursor = cnxn.cursor()
def app():

    headerSection = st.container()
    mainSection = st.container()
    loginSection = st.container()
    logOutSection = st.container()
    
    # def show_main_page():
    #     # with mainSection:
    #     #     dataFile = st.text_input("Enter your Test file name: ")
    #     #     Topics = st.text_input("Enter your Model Name: ")
    #     #     ModelVersion = st.text_input("Enter your Model Version: ")
    #     #     processingClicked = st.button ("Start Processing", key="processing")
    #     #     if processingClicked:
    #     #            st.balloons() 
    #     with st.form(key="vendor_form"):
    #         company_name = st.text_input(label="Company Name*")
    #         #products = st.multiselect("Products Offered", options=PRODUCTS)
    #         years_in_business = st.slider("Years in Business", 0, 50, 5)
    #         onboarding_date = st.date_input(label="Onboarding Date")
    #         additional_info = st.text_area(label="Additional Notes")

    #         # Mark mandatory fields
    #         st.markdown("**required*")

    #         submit_button = st.form_submit_button(label="Submit Vendor Details")
                
    # @st.cache_resource
    # def init_connection():
    #         return pyodbc.connect(
    #             "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
    #             + st.secrets["server"]
    #             + ";DATABASE="
    #             + st.secrets["database"]
    #             + ";UID="
    #             + st.secrets["username"]
    #             + ";PWD="
    #             + st.secrets["password"]
    #         )

    # conn1 = init_connection()
    # def run_query(query):
    #         with conn1.cursor() as cur1:
    #             print("query=====", query)
    #             cur1.execute(query)
    #             #print(cur.execute(query))
    #         return cur1.fetchall()
    @st.cache_data
    def login(userName: str, password: str) -> bool:
        
        # Initialize connection.
        # Uses st.cache_resource to only run once.
        

        
        try:
        

            userName = "'" + userName + "'"
            password = "'" + password + "'"
            # sql = '''
            #         SELECT
            #             "username",
            #             "password"
            #         FROM 
            #             TD_user
            #         WHERE 
            #             username = {userName} and password = {password};
            #         '''
            #rows = run_query(sql.format(userName = userName , password = password))
            # print(rows)
            # df_new = conn.query(sql=sql.format(userName = userName , password = password))
        
            # conn1.cursor().execute(sql.format(userName = userName , password = password))
            # row = conn1.cursor().fetchone()
            # if row > 0:
            #     print("There are no results for this query")
            # else:
            #     print("ok")
            count = 0
            
            j = cursor.execute("SELECT * from TD_user WHERE username = {} and password = {};".format(userName,password))
            for row in j:
                count = 1
                #print(row)
            if count == 0:
                #print("No Result")
                st.error("No Result")

            #result = conn1.cursor().fetchall()
            # for row in result:
            #     st.write(row)
        except Exception as e:
            #print("The error is: ",e)
            st.error(e)
        # print("rows == ",rows)
        # print("hhhhh == ",len(rows))


        return True if count == 1 else False

    def LoggedOut_Clicked():
        st.session_state['loggedIn'] = False
        st.session_state['userName'] = ''
        
    def show_logout_page():
        loginSection.empty()
        with logOutSection:
            st.markdown("Welcome K'" + st.session_state['userName'])
            st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
    def LoggedIn_Clicked(userName, password):
        if login(userName, password):
            st.session_state['loggedIn'] = True
            st.session_state['userName'] = userName
            
        else:
            st.session_state['loggedIn'] = False
            st.error("Invalid user name or password")
        
    def show_login_page():
        with loginSection:
            if st.session_state['loggedIn'] == False:
                userName = st.text_input (label="", value="", placeholder="Enter your user name")
                password = st.text_input (label="", value="",placeholder="Enter password", type="password")
                st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))
                

    with headerSection:
            st.title("Login")
            #first run will have nothing in session_state
            
            if 'loggedIn' not in st.session_state:
                st.session_state['loggedIn'] = False
                show_login_page() 
                #print("1")
            else:
                if st.session_state['loggedIn']:
                    show_logout_page() 
                    #print("You already logged in")   
                    #show_main_page()  
                    #print("2")

                    # import pandas as pd
                    # df = pd.read_csv(r'C:\Users\BeEr\Downloads\Finance_topic.csv')
                    # df = df.fillna('')
                    # print(df.head(2))
                    # try:

                    #     for index, row in df.iterrows():
                    #         row1 = (row["keys"],row["Topic"],row["title"],row["texts"],row["url"],row["type1"])
                    #         cursor.execute('INSERT INTO TM_articles(article_id, type_domain, title_name, contents, url, task_type) VALUES (?,?,?,?,?,?)', row1)
                    #     cnxn.commit()
                    # except Exception as e:
                    #     print("The error is: ",e)
            
                else:
                    show_login_page()
                    #print("3")
