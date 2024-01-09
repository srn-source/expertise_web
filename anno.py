import streamlit as st
# from streamlit_option_menu import option_menu
import home, anno 
from datetime import datetime

PRODUCTS = [
    "Electronics",
    "Apparel",
    "Groceries",
    "Software",
    "Other",
]

TAGS_LEGAL = [
"1.Basic legal knowledge ความรู้พื้นฐานกฏหมาย",
"2.Criminal Law  กฎหมายอาญา",
"3.Civil Law  กฎหมายแพ่ง",
"4.Family Law  กฎหมายครอบครัว",
"5.Corporate Law  กฎหมายนิติบุคคล",
"6.Employment Law  กฎหมายแรงงาน",
"7.Intellectual Property Law  กฎหมายทรัพย์สินทางปัญญา",
"8.Real Estate Law  กฎหมายอสังหาริมทรัพย์",
"9.Environmental Law  กฎหมายสิ่งแวดล้อม",
"10.Tax Law  กฎหมายภาษี",
"11.Immigration Law  กฎหมายคนเข้าเมือง",
"12.Health Law  กฎหมายสุขภาพ",
"13.Constitutional Law  กฎหมายรัฐธรรมนูญ",
"14.International Law  กฎหมายระหว่างประเทศ",
"15.Admiralty (Maritime) Law  กฎหมายการเดินเรือ",
"16.Administrative Law  กฎหมายปกครอง",
"17.Taxation Law  กฎหมายการจัดเก็บภาษี",
"18.Human Rights Law  กฎหมายสิทธิมนุษยชน",
"19.Bankruptcy Law  กฎหมายล้มละลาย",
"20.Securities Law  กฎหมายหลักทรัพย์",
"21.Military Law  กฎหมายทหาร",
"22.Education Law  กฎหมายการศึกษา",
"23.Entertainment Law  กฎหมายบันเทิง",
"24.Aviation Law  กฎหมายการบิน",
"25.Energy Law  กฎหมายพลังงาน",
"26.Animal Law  กฎหมายสัตว์",
"27.Cybersecurity and Privacy Law  กฎหมายความมั่นคงปลอดภัยไซเบอร์และความเป็นส่วนตัว"
]

TAGS_FINANCE = [
"1.สถาบันการเงิน",
"2.ผลิตภัณฑ์และบริการทางการเงิน",
"3.ตลาดการเงิน",
"4.เครื่องมือทางการเงิน",
"5.กลยุทธ์การลงทุน",
"6.การบริหารสินทรัพย์",
"7.การจัดการการเงินส่วนบุคคล",
"8.การวิเคราะห์ทางการเงิน",
"9.เศรษฐศาสตร์การเงิน",
"10.กฎหมายการเงิน",
"11.เทคโนโลยีทางการเงิน",
"12.การเงินดิจิทัล"
]

TAGS_MEDICAL = [
"1.กุมารเวชศาสตร์ (กุมารเวชศาสตร์) - Pediatrics",
"2.จักษุวิทยา (จักษุวิทยา) - Ophthalmology",
"3.จิตเวชศาสตร์ (จิตเวชศาสตร์) - Psychiatry",
"4.นิติเวชศาสตร์ (นิติเวชศาสตร์) - Forensic Medicine",
"5.พยาธิวิทยา (พยาธิวิทยา) - Pathology",
"6.รังสีวิทยา (รังสีวิทยา) - Radiology",
"7.วิสัญญีวิทยา (วิสัญญีวิทยา) - Anesthesiology",
"8.ศัลยศาสตร์ (ศัลยศาสตร์) - Surgery",
"9.สูติศาสตร์ (สูติศาสตร์) - Obstetrics",
"10.นรีเวชวิทยา (นรีเวชวิทยา) - Gynecology",
"11.ออร์โธปิดิกส์ (ออร์โธปิดิกส์) - Orthopedics",
"12.อายุรศาสตร์ (อายุรศาสตร์) - Internal Medicine",
"13.เวชศาสตร์ (เวชศาสตร์) - Medicine",
"14.โสต ศอ นาสิกวิทยา (โสต ศอ นาสิกวิทยา) - Otolaryngology",
"15.ผิวหนัง Dermatology",
"16.ภาควิชาระบาดวิทยา Epidemiology",
"17.ทันตกรรม Dentistry",
"18.เภสัชวิทยา Pharmacology",
"19.สัตวแพทยศาสตร์ Veterinary Medicine",
]

THAICULT = [
     "",
     "NO",
     "YES"
]

REVIEWSTATUS =[
     "",
     "PASS",
     "NOT_PASS"
]

import pyodbc

#cnxn = pyodbc.connect(
#                "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
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

def app():
    #print("====> ",st.session_state)
    if st.session_state['loggedIn'] == False:
        st.error("Please login")
        st.stop()
    with st.form(key="vendor_form" , clear_on_submit=True):
            # conn = st.connection("gsheets", type=GSheetsConnection)
            # data = conn.read(worksheet = "Sheet1", usecols = list(range(4)))
            # sql = '''
            #     SELECT
            #         "Instruction",
            #         "Input",
            #         "Answer",
            #         "DomainTag",
            #         "id",
            #         "actor",
            #         "flag"
            #     FROM 
            #         Sheet1
            #     WHERE 
            #         "actor" = {type1} and "flag" = 0
            #     LIMIT 1
            #     '''
            # #print("user = ",st.session_state['userName'])
            # df_new = conn.query(sql=sql.format(type1 = "'"+ st.session_state['userName'] + "'"))
            # print(df_new)
            

            df_new = cursor.execute("SELECT TOP 1 * from View_info_insert WHERE actor_master = {} and date_insert IS NULL;".format("'"+st.session_state['userName']+ "'"))
            df_new = df_new.fetchall()
            #print(df_new)
            if len(df_new)  == 1:
                #ggg =""
                st.subheader(df_new[0][11], divider='rainbow')
                st.markdown(df_new[0][10])
                st.markdown("Link ref.: "+df_new[0][12])
                st.subheader("Instruction Task Type: "+ df_new[0][3])
                #print(df_new["id"].values[0])
                #ids = df_new["id"].values[0]
                # print(df_new["Instruction"].values[0])
                
                Instruction_name = st.text_area(label="Instruction (Question)*", height= 100, value=df_new[0][4])
                input_name = st.text_area(label="Input", height= 200, value=df_new[0][5])
                
                #years_in_business = st.slider("Years in Business", 0, 50, 5)
                #onboarding_date = st.date_input(label="Onboarding Date" )
                Answer = st.text_area(label="Output*", height= 300, value=df_new[0][6])

                DEF_TAG = PRODUCTS
                if df_new[0][0] == "Finance":
                   DEF_TAG = TAGS_FINANCE
                elif df_new[0][0] == "Medical":
                   DEF_TAG = TAGS_MEDICAL
                elif df_new[0][0] == "Legal":
                   DEF_TAG = TAGS_LEGAL
                   
                #print(DEF_TAG)
                domain_tag = st.multiselect("Domain Tags*", options=DEF_TAG ) #,  default= ["5.กลยุทธ์การลงทุน","6.การบริหารสินทรัพย์"]
                thai_spec = st.selectbox("Thai Culture Specific*", options=THAICULT )
                review_status = st.selectbox("Review Status*", options=REVIEWSTATUS)
                comment_name = st.text_area(label="Comment*", height= 200, value="")

                # Mark mandatory fields
                st.markdown("**required*")

                submit_button = st.form_submit_button(label="Submit Vendor Details")
                

                #If the submit button is pressed
                if submit_button:
                    # Check if all mandatory fields are filled
                    if not Instruction_name  or not Answer or not comment_name or not review_status or not domain_tag or not thai_spec:
                        st.warning("Ensure all mandatory fields are filled.")
                        st.stop()
                    # elif existing_data["CompanyName"].str.contains(company_name).any():
                    #     st.warning("A vendor with this company name already exists.")
                    #     st.stop()
                    else:
                        # Create a new row of vendor data
                        try:
                            domain_tag = ",".join(domain_tag)
                            #cursor.execute('INSERT INTO TD_insert(type_domain, article_id, task_type, Instruction, Input, Output) VALUES (?,?,?,?,?,?)', tuple(row))
                            row = (df_new[0][0],df_new[0][1],df_new[0][2],df_new[0][3],Instruction_name,input_name,Answer,domain_tag,thai_spec,review_status,comment_name,st.session_state['userName'],datetime.now())
                            cursor.execute("INSERT INTO TD_insert(type_domain, article_id, rev, task_type, Instruction, Input, Output, domain_tags, thai_specific, review_status, comment, Actor, Date_actor ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
                            cnxn.commit()
                            st.success("Details successfully submitted!")
                            st.rerun()
                            # from streamlit_js_eval import streamlit_js_eval
                            # streamlit_js_eval(js_expressions="parent.window.location.reload()")
                            #anno.app()
                            #row = (df_new[0][0],df_new[0][1],df_new[0][2],df_new[0][3],Instruction_name,input_name,Answer,domain_tag,thai_spec,review_status,comment_name,st.session_state['userName'],datetime.now())
                        except Exception as e:
                            #print("The error is: ",e)
                            st.error(e)

            else:
                 if st.session_state['loggedIn'] == False:
                      st.subheader("Please login again")
                 else:
                      st.subheader("Data all complete")
                      
