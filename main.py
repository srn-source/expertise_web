
import streamlit as st
import home
import pyodbc
import pandas as pd
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
    return cursor, cnxn

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
            cursor, cnxn = reconnect()
            while True:
                if not cnxn:
                    cursor, cnxn = reconnect()
                    print("ok")
                else:
                    break
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
    
    def save_info_chosen_reject(df , n , dom):
        try:
            print("df : " ,len(df))
            for index, row in df.iterrows():
                actor = dom + str((index % n)+1)

                row1 = (row["id_key"],row["context"].strip(),row["question"].strip(),row["answers"].strip() , actor)
                cursor.execute('INSERT INTO TD_info_chosen_reject(id_keys, context, question, answer,  actor) VALUES (?,?,?,?,?)', row1)
            cnxn.commit()
            print("finish ==> " + dom )

        except Exception as e:
            print("The error is: ",e)
    def save_info_chosen_reject_only_id(df , n , dom):
        try:
            import numpy as np
            print("df : " ,len(df))
            article_csv = pd.read_csv(r'D:\data_instruction_backup\Master table.csv')
            print("original : " ,len(df))
            merge_table = pd.merge(df, article_csv,  left_on=['article_id'], right_on=['keys'] , how="left" ,  indicator = True) 
            print("merge_table : " ,len(merge_table))
            print(merge_table.columns)
            print(len(merge_table[merge_table['_merge'] == 'both']) , len(df))
            print(merge_table.head())
            # merge_table = merge_table.replace('', np.nan)                   # to get rid of empty values
            # nan_values = merge_table[merge_table.isna().any(axis=1)]  
            # print(nan_values)  

            for index, row in merge_table.iterrows():
                actor = dom + str((index % n)+1)

                df_new = cursor.execute("SELECT TOP 1 * from TM_articles WHERE article_id = {}".format("'"+row["article_id"]+"'"))
                df_new = df_new.fetchall()

                if len(df_new)  == 0:
                    if row["type_new"] == '' or pd.isna(row["type_new"]):
                       row["type_new"] = row["type_old"]
                       print(row["type_new"])
                    row1 = (row["keys"],row["Topic"],row["title"],row["texts"],row["url"],row["type_new"])
                    cursor.execute('INSERT INTO TM_articles(article_id ,type_domain,  title_name, contents, url , task_type) VALUES (?,?,?,?,?,?)', row1)
                
                row1 = (row["article_id"],"","","" , actor)
                cursor.execute('INSERT INTO TD_info_chosen_reject(id_keys, context, question, answer,  actor) VALUES (?,?,?,?,?)', row1)

            if len(merge_table[merge_table['_merge'] == 'both']) == len(df):
                cnxn.commit()
                print("finish ==> " + dom )

        except Exception as e:
            print("The error is: ",e)
    def save_info(df , n , dom):
        try:
            article_csv = pd.read_csv(r'D:\data_instruction_backup\Master table.csv')
            print("original : " ,len(df))
            merge_table = pd.merge(df, article_csv,  left_on=['keys'], right_on=['keys'] , how="left" ,  indicator = True) 
            print("merge_table : " ,len(merge_table))
            print(merge_table.columns)
            print(len(merge_table[merge_table['_merge'] == 'both']) , len(df))
            for index, row in merge_table.iterrows():
                task_type_id = 0
                if row["Instruction task type"] == "Closed QA":
                    task_type_id = 2
                elif row["Instruction task type"] == "Open QA":
                    task_type_id = 1
                elif row["Instruction task type"] == "Summarization":
                    task_type_id = 4
                elif row["Instruction task type"] == "Classification":
                    task_type_id = 6
                elif row["Instruction task type"] == "Multiple choice":
                    task_type_id = 3

                actor = 'no'
                if dom != "Medical":
                    if index % n == 0:
                        actor = dom + str(1)
                    elif index % n == 1:
                        actor = dom + str(2)
                    elif index % n == 2:
                        actor = dom + str(3)
                    elif index % n == 3:
                        actor = dom + str(4)
                    elif index % n == 4:
                        actor = dom + str(5)
                else:
                    if index % n == 0:
                        actor = dom + str(1)
                    elif index % n == 1:
                        actor = dom + str(2)
                    elif index % n == 2:
                        actor = dom + str(3)
                    elif index % n == 3:
                        actor = dom + str(4)
                    elif index % n == 4:
                        actor = dom + str(5)
                    elif index % n == 5:
                        actor = dom + str(6)
                

                #q= ""
                q = "_fix1"

                row1 = (row["keys"] + q,row["type"],row["title"],row["texts"],row["url"],row["type_new"])
                cursor.execute('INSERT INTO TM_articles(article_id ,type_domain,  title_name, contents, url , task_type) VALUES (?,?,?,?,?,?)', row1)

                row1 = (row["type"],row["keys"] + q,0,row["Instruction task type"], task_type_id  ,row["Instruction"].strip(),row["Input"].strip(),row["Output"].strip() , actor)
                cursor.execute('INSERT INTO TD_info(type_domain, article_id, rev, task_type,  task_type_id, Instruction, Input, Output, Actor) VALUES (?,?,?,?,?,?,?,?,?)', row1)
            
            if len(merge_table[merge_table['_merge'] == 'both']) == len(df):
                cnxn.commit()
                print("finish ==> " + dom )
        except Exception as e:
            print("The error is: ",e)

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

                    import pandas as pd

                    # df1 = pd.read_csv(r'C:\Users\BeEr\Downloads\iapp_tydi_4000.csv')
                    # df1 = df1.fillna('')
                    # print(df1.head(3))
                    # save_info_chosen_reject(df1, 11, 'USER')

                    # df1 = pd.read_csv(r'C:\Users\BeEr\Downloads\legal_sample_2000.csv')
                    # df1 = df1.fillna('')
                    # print(df1.head(3))
                    # save_info_chosen_reject_only_id(df1, 11, 'USER')
                    
                    # df1 = pd.read_csv(r'C:\Users\BeEr\Downloads\finance_sample_2000.csv')
                    # df1 = df1.fillna('')
                    # print(df1.head(3))
                    # save_info_chosen_reject_only_id(df1, 11, 'USER')
                    
                    # df1 = pd.read_csv(r'C:\Users\BeEr\Downloads\medical_sample_2000.csv')
                    # df1 = df1.fillna('')
                    # print(df1.head(3))
                    # save_info_chosen_reject_only_id(df1, 11, 'USER')
                    

                    # df1 = pd.read_csv(r'C:\Users\BeEr\Downloads\Retail_b4.csv')
                    # df1 = df1.fillna('')
                    # print(df1.head(3))
                    # save_info(df1, 5, 'Retail')

                    # df2 = pd.read_csv(r'D:\expertise_web\data_original\Medical1_fix.csv')
                    # df2 = df2.fillna('')
                    # print(df2.head(3))
                    # save_info(df2, 6, 'Medical')

                    # df3 = pd.read_csv(r'D:\expertise_web\data_original\Legal1_fix.csv')
                    # df3 = df3.fillna('')
                    # print(df3.head(2))
                    # save_info(df3, 5, 'Legal')

                    # df4 = pd.read_csv(r'D:\expertise_web\data_original\Finance1_fix.csv') #read_excel
                    # df4 = df4.fillna('')
                    # print(df4.head(2))
                    # save_info(df4, 5, 'Finance')

                    # try:
                    #     for index, row in df1.iterrows():
                    #         row1 = (row["keys"],row["Topic"],row["title"],row["texts"],row["url"],row["type1"])
                    #         cursor.execute('INSERT INTO TM_articles(article_id, type_domain, title_name, contents, url, task_type) VALUES (?,?,?,?,?,?)', row1)
                    #     #cnxn.commit()
                    #     for index, row in df2.iterrows():
                    #         row1 = (row["keys"],row["Topic"],row["title"],row["texts"],row["url"],row["type1"])
                    #         cursor.execute('INSERT INTO TM_articles(article_id, type_domain, title_name, contents, url, task_type) VALUES (?,?,?,?,?,?)', row1)
                    #     #cnxn.commit()
                    #     for index, row in df3.iterrows():
                    #         row1 = (row["keys"],row["Topic"],row["title"],row["texts"],row["url"],row["type1"])
                    #         cursor.execute('INSERT INTO TM_articles(article_id, type_domain, title_name, contents, url, task_type) VALUES (?,?,?,?,?,?)', row1)
                    #     cnxn.commit()
                    # except Exception as e:
                    #     print("The error is: ",e)

                    # j = cursor.execute("SELECT type_domain,article_id ,review_status ,Actor from TD_insert")
                    # df_new = j.fetchall()
                    # print(len(df_new))
                    # print(type(df_new))
                    # fff = [d[0] for d in df_new]
                    # fff1 = [d[1] for d in df_new]
                    # fff2 = [d[2] for d in df_new]
                    # fff3 = [d[3] for d in df_new]
                    # import pandas as pd
                    # df_all_insert_v1 = pd.DataFrame(list(zip(fff , fff1 , fff2, fff3)) ,columns=['type_domain_insert' ,'article_id_insert', 'review_status_insert', 'Actor_insert' ])


                    # j = cursor.execute("SELECT type_domain,article_id,Actor  from TD_info")
                    # df_new = j.fetchall()
                    # print(len(df_new))
                    # print(type(df_new))
                    # fff = [d[0] for d in df_new]
                    # fff1 = [d[1] for d in df_new]
                    # fff2 = [d[2] for d in df_new]
                    # import pandas as pd
                    # df_all_info_v1 = pd.DataFrame(list(zip(fff, fff1 , fff2)) ,columns=['type_domain_info' ,'article_id_info', 'Actor_info'])


                    # df2 = pd.DataFrame({'keys': ['test'],
                    #                    'batch': ['0']})
                    # for i in range(1,10):
                    #     f = f'D:\expertise_web\data_original\Finance{i}.csv'
                    #     df = pd.read_csv(f)
                    #     df = df[['keys']]
                    #     df['type_domain'] = "Finance"
                    #     df['batch'] = str(i)
                    #     df2 = pd.concat([df2, df])

                    # for i in range(1,10):
                    #     f = f'D:\expertise_web\data_original\Legal{i}.csv'
                    #     df = pd.read_csv(f)
                    #     df = df[['keys']]
                    #     df['type_domain'] = "Legal"
                    #     df['batch'] = str(i)
                    #     df2 = pd.concat([df2, df])

                    # for i in range(1,10):
                    #     f = f'D:\expertise_web\data_original\Medical{i}.csv'
                    #     df = pd.read_csv(f)
                    #     df = df[['keys']]
                    #     df['type_domain'] = "Medical"
                    #     df['batch'] = str(i)
                    #     df2 = pd.concat([df2, df])
                        
                    # for i in range(1,10):
                    #     f = f'D:\expertise_web\data_original\Retail{i}.csv'
                    #     df = pd.read_csv(f)
                    #     df = df[['keys']]
                    #     df['type_domain'] = "Retail"
                    #     df['batch'] = str(i)
                    #     df2 = pd.concat([df2, df])
                        

                    # print("TD_insert : " ,len(df_all_insert_v1))
                    # print("TD_info : " ,len(df_all_info_v1))
                    # print("All : " ,len(df2))
                    # merge_table1 = pd.merge(df2, df_all_insert_v1,  left_on=['keys'], right_on=['article_id_insert'] , how="left" ,  indicator = True)
                    # print(merge_table1.head())
                    # merge_table = pd.merge(merge_table1, df_all_info_v1,  left_on=['keys'], right_on=['article_id_info'] , how="left" )
                    # print("merge_table : " ,len(merge_table))
                    # merge_table.to_csv(f"D:\expertise_web\data_original\merge_table_v1.csv" , encoding="utf-8")











                    # import pandas as pd
                    # df = pd.read_csv(r'D:\expertise_web\backup_db_10_March_2024\TM_articles.csv')
                    # df['len_a'] = df['contents'].apply(lambda x: len(x))
                    # print(len(df))
                    # print(df[df['len_a'] >33000])
                    # df_TD_insert = cursor.execute("SELECT * from TD_insert")
                    # df_TD_insert = df_TD_insert.fetchall()

                    # type_domain = []
                    # article_id = []
                    # rev = []
                    # task_type_id = []
                    # task_type = []
                    # Instruction = []
                    # Input = []
                    # Output = []
                    # Actor = []

                    # type_domain= []
                    # article_id= []
                    # rev= []
                    # task_type_id= []
                    # task_type= []
                    # Instruction= []
                    # Input= []
                    # Output= []
                    # domain_tags= []
                    # thai_specific= []
                    # review_status= []
                    # comment= []
                    # Actor= []
                    # Date_actor= []

                    # print("df_TD_insert = ",len(df_TD_insert))
                    # for rows in df_TD_insert:
                    #     type_domain.append(rows[0])
                    #     article_id.append(rows[1])
                    #     rev.append(rows[2])
                    #     task_type_id.append(rows[3])
                    #     task_type.append(rows[4])
                    #     Instruction.append(rows[5])
                    #     Input.append(rows[6])
                    #     Output.append(rows[7])
                    #     domain_tags.append(rows[8])
                    #     thai_specific.append(rows[9])
                    #     review_status.append(rows[10])
                    #     comment.append(rows[11])
                    #     Actor.append(rows[12])
                    #     Date_actor.append(rows[13])
                    
                    # df = pd.DataFrame(list(zip(type_domain , article_id , rev, task_type_id,task_type ,Instruction,Input ,Output,domain_tags,thai_specific, review_status ,comment,Actor, Date_actor )) ,columns=['type_domain' , 'article_id' , 'rev', 'task_type_id','task_type' ,'Instruction','Input' ,'Output','domain_tags','thai_specific', 'review_status' ,'comment','Actor', 'Date_actor' ])
                    
                    # df.to_json('D:\expertise_web\df_TD_insert_all.json', orient = 'records', compression = 'infer', index = 'true' , force_ascii = False)
                    # df.to_csv("D:\expertise_web\df_TD_insert_all.csv" , encoding="utf-8")

                else:
                    show_login_page()
                    #print("3")
