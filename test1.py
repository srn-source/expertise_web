import streamlit as st
from streamlit_option_menu import option_menu
import home , main , anno ,yoursuccess , chre, chkpass, wang,vistec #, trending, test, your, about
st.set_page_config(
        page_title="Instruction Dataset",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Instruction ',
                options=['Home','Main', 'Chosen & Reject','Annotation','Your success' , 'Check Pass', 'Wang' , 'Vistec'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill','info-circle-fill','chat-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
           
        #import pyodbc

        # Initialize connection.
        # Uses st.cache_resource to only run once.
        # @st.cache_resource
        # def init_connection():
        #     return pyodbc.connect(
        #         "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        #         + st.secrets["server"]
        #         + ";DATABASE="
        #         + st.secrets["database"]
        #         + ";UID="
        #         + st.secrets["username"]
        #         + ";PWD="
        #         + st.secrets["password"]
        #     )

        # conn = init_connection()

        # # @st.cache_data(ttl=600)
        # def run_query(query):
        #     with conn.cursor() as cur:
        #         cur.execute(query)
        #         return cur.fetchall()

        # rows = run_query("SELECT * from TD_name;")
        

        # # Print results.
        # for row in rows:
        #     #print("==> ",row)
        #     #print(row[0])
        #     print(row[1].strip())
        #     st.write(f"{row[1]} has a :{row[1]}:")
        
        # #rows = run_query("UPDATE TD_name SET name = 'Alfred Schmidt' WHERE ids = 1;")
        
        # sql = "update TD_name set name ='Alfred Schmidt' where ids = 1"
        # conn.cursor().execute(sql)
        # conn.commit()

        # rows = run_query("SELECT * from TD_name;")


        # # Print results.
        # for row in rows:
        #     #print("==> ",row)
        #     #print(row[0])
        #     print(row[1].strip())
        #     st.write(f"{row[1]} has a :{row[1]}:")


        #print("================== ok2")
        # Print results.
        

        
        if app == "Home":
            st.session_state['ids'] = []
            home.app()
        if app == "Main":
            st.session_state['ids'] = []
            main.app()
        if app == 'Chosen & Reject':
            chre.app()
        if app == "Annotation":
            st.session_state['ids'] = []
            anno.app()        
        if app == 'Your success':
            st.session_state['ids'] = []
            yoursuccess.app()
        if app == 'Check Pass':
            chkpass.app()
        if app == 'Wang':
            wang.app()
        if app == 'Vistec':
            vistec.app()
            
             
          
             
    run()            
         