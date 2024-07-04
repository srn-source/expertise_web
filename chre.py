import streamlit as st
# from streamlit_option_menu import option_menu
import home, anno 
from datetime import datetime
import pytz

PRODUCTS = [
    "Electronics",
    "Apparel",
    "Groceries",
    "Software",
    "Other",
]

TAGS_LEGAL = [
"1.ความรู้พื้นฐานกฏหมาย",
'2.ประมวลกฎหมายอาญา',
'3.ประมวลกฎหมายแพ่งและพาณิชย์',
'4.ประมวลกฎหมายวิธีพิจารณาความแพ่งฯ(วิแพ่ง)',
'5.ประมวลกฎหมายวิธีพิจาณาความอาญา(วิอาญา)',
'6.กฎหมายปกครอง(วิธีปฏิบัติราชการ-จัดตั้งและพิจารณาคดีของศาลปกครอง)',
'7.กฎหมายยาเสพติดให้โทษ',
'8.กฎหมายคุ้มครองแรงงาน-แรงงานสัมพันธ์-เงินทดแทน',
"9.กฎหมายเยาวชนและครอบครัว พรบ.คุ้มครองผู้ถูกกระทำด้วยความรุนแรงในครอบครัว",
"10.กฎหมายนิติบุคคล",
"11.กฎหมายแรงงาน",
"12.กฎหมายคุ้มครองผู้บริโภค-ราคาสินค้าและบริการ",
"13.ประมวลกฎหมายที่ดิน",
"14.กฎหมายว่าด้วยความผิดเกี่ยวกับคอมพิวเตอร์(พรบ.คอม)",
"15.กฎหมายทรัพย์สินทางปัญญา (ลิขสิทธิ์ สิทธิบัตร เครื่องหมายการค้า)",
"16.กฎหมายอสังหาริมทรัพย์",
"17.กฎหมายสิ่งแวดล้อม กฎหมายป่าไม้และอุทยาน",
"18.กฎหมายภาษี",
"19.กฎหมายคนเข้าเมือง-การทำงานของคนต่างด้าว",
"20.กฎหมายสาธารณสุข การแพทย์ และโรคระบาด",
"21.กฎหมายรัฐธรรมนูญ",
"22.กฎหมายระหว่างประเทศ สนธิสัญญา",
"23.กฎหมายพานิชย์นาวี(ขนส่งทางทะเล-กู้ภัยทางทะเล) พรบ.การขนส่งต่อเนื่องหลายรูปแบบ",
"24.กฎหมายปกครองว่าด้วยความรับผิดทางละเมิดของเจ้าหน้าที่",
"25.กฎหมายประกันภัย",
"26.กฎหมายสิทธิมนุษยชน",
"27.กฎหมายล้มละลาย-ฟื้นฟูกิจการ",
"28.กฎหมายหลักทรัพย์",
"29.กฎหมายทหาร",
"30.กฎหมายการศึกษา-ครูและบุคลากร",
"31.กฎหมายบันเทิง",
"32.กฎหมายการบิน",
"33.กฎหมายพลังงาน",
"34.กฎหมายสัตว์",
"35.กฎหมายไซเบอร์-คุ้มครองข้อมูลส่วนบุคคล(PDPA)",
"36.กฎหมายควบคุมเครื่องดื่มแอลกอฮอล์",
"37.กฎหมายลักษณะหนี้ พรบ.ทวงถามหนี้",
"38.กฎหมายนิติกรรม-สัญญา-ข้อสัญญาไม่เป็นธรรม",
"39.กฎหมายละเมิด",
"40.กฎหมายทรัพย์สิน-กรรมสิทธิ์-ทรัพย์อิงสิทธิ",
"41.กฎหมายมรดก-พินัยกรรม",
"42.กฎหมายซื้อขาย",
"43.กฎหมายเช่าทรัพย์",
"44.กฎหมายเช่าซื้อ",
"45.กฎหมายจ้างแรงงาน",
"46.กฎหมายจ้างทำของ",
"47.กฎหมายกู้ยืม-ยืมใช้คงรูป-ยืมใช้สิ้นเปลือง",
"48.กฎหมายค้ำประกัน",
"48.กฎหมายจำนำ",
"49.กฎหมายจำนอง",
"50.กฎหมายตัวแทน",
"51.กฎหมายนายหน้า",
"52.กฎหมายประนีประนอมยอมความ",
"53.กฎหมายการพนันขันต่อ",
"54.กฎหมายหุ้นส่วน-บริษัท",
"55.กฎหมายอาญาความผิดลหุโทษ",
"56.กฎหมายอาญาความผิดเกี่ยวกับความมั่นคงแห่งราชอาณาจักร-การก่อการร้าย",
"57.กฎหมายอาญาความผิดเกี่ยวกับการปกครอง(ความผิดต่อเจ้าพนักงาน-ตำแหน่งราชการ)",
"58.กฎหมายอาญาความผิดเกี่ยวกับการยุติธรรม",
"59.กฎหมายอาญาความผิดเกี่ยวกับศาสนา",
"60.กฎหมายอาญาความผิดเกี่ยวกับความสงบสุขของประชาชน(อั้งยี่-ซ่องโจร)",
"61.กฎหมายอาญาความผิดเกี่ยวกับการก่อให้เกิดภยันตรายต่อประชาชน(วางเพลิง-อุทกภัยและอื่นๆ)",
"62.กฎหมายอาญาความผิดเกี่ยวกับการปลอมและแปลง",
"63.กฎหมายอาญาความผิดเกี่ยวกับการค้า",
"64.กฎหมายอาญาความผิดเกี่ยวกับเพศ",
"65.กฎหมายอาญาความผิดเกี่ยวกับชีวิตและร่างกาย",
"66.กฎหมายอาญาความผิดเกี่ยวกับเสรีภาพและชื่อเสียง",
"67.กฎหมายอาญาความผิดเกี่ยวกับทรัพย์ (ลักทรัพย์ ยักยอก ฉ้อโกง)",
"68.กฎหมายอาญาความผิดเกี่ยวกับศพ",
"69.กฎหมายตั๋วเงิน-เช็ค",
"70.กฎหมายฝากทรัพย์",
"71.กฎหมายรับขนของ-คนโดยสาร",
"72.คำพิพากษาศาลฎีกา",
"73.กฎหมายการเล่นแชร์",
"74.กฎหมายประกันสังคม",
"75.กฎหมายว่าด้วยธุรกิจนำเที่ยวและมัคคุเทศก์",
"76.กฎหมายว่าด้วยการควบคุมอาคาร อาคารชุด-จัดสรรที่ดินและถมดิน",
"77.พระราชบัญญัติประกอบรัฐธรรมนูญ",
"78.กฎหมายลักษณะพยาน (ทั้งวิแพ่งและวิอาญา)",
"79.พระราชกำหนด",
"80.พระราชกฤษฎีกา ข้อกำหนดประธานศาลฎีกา",
"81.กฎกระทรวง",
"82.กฎหมายและข้อบังคับหรือข้อบัญญัติองค์กรปกครองส่วนท้องถิ่น",
"83.กฎหมายอาวุธปืน เครื่องกระสุนปืน วัตถุระเบิด ดอกไม้เพลิง และสิ่งเทียมอาวุธปืน",
"84.กฎหมายการค้าระหว่างประเทศ",
"85.กฎหมายจราจร และขนส่งทางบก",
"86.กฎหมายพระธรรมนูญศาลยุติธรรม พรบ.ว่าด้วยการวินิจฉัยชี้ขาดอำนาจหน้าที่ระหว่างศาล",
"87.กฎหมายการคลัง",
"88.กฎหมายว่าด้วยคดีอาญาของผู้ดำรงตำแหน่งทางการเมือง",
"89.กฎหมายแลกเปลี่ยน-ให้",
"90.กฎหมายบัญชีเดินสะพัด-เก็บของในคลังสินค้า",
"91.กฎหมายป้องกันและปราบปรามการฟอกเงิน",
"92.ข่าวสารทั่วไป สถิติต่างๆ",
"93.กฎหมายเลือกตั้ง",
"94.กฎหมายโรงงานอุตสาหกรรมและเครื่องจักร-เหมืองแร่",
"95.กฎหมายการแข่งขันทางการค้า-ควบคุมราคา",
"96.กฎหมายอวกาศ",
"97.วิชาว่าความและทนายความ คำฟ้อง คำให้การและคำร้องขอ มรรยาททนายความ",
"98.กฎหมายชุมนุม"
]


# TAGS_FINANCE = [
# "1.สถาบันการเงิน",
# "2.ผลิตภัณฑ์และบริการทางการเงิน",
# "3.ตลาดการเงิน",
# "4.เครื่องมือทางการเงิน",
# "5.กลยุทธ์การลงทุน",
# "6.การบริหารสินทรัพย์",
# "7.การจัดการการเงินส่วนบุคคล",
# "8.การวิเคราะห์ทางการเงิน",
# "9.เศรษฐศาสตร์การเงิน",
# "10.กฎหมายการเงิน",
# "11.เทคโนโลยีทางการเงิน",
# "12.การเงินดิจิทัล",
# ]
TAGS_FINANCE = [
 "1.เทคโนโลยีทางการเงิน & การเงินดิจิทัล",
 "2.การวิเคราะห์ทางการเงิน & เศรษฐศาสตร์การเงิน",
 "3.ตลาดการเงิน & ผลิตภัณฑ์และบริการทางการเงิน",
 "4.ข่าวเศรษฐกิจและการเงิน",
 "5.ความรู้ทางการเงิน",
 "6.ข้อมูลการเงินรายบริษัท"
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
"13.โสต ศอ นาสิกวิทยา (โสต ศอ นาสิกวิทยา) - Otolaryngology",
"14.ผิวหนัง Dermatology",
"15.ภาควิชาระบาดวิทยา Epidemiology",
"16.ทันตกรรม Dentistry",
"17.เภสัชวิทยา Pharmacology",
"18.งานการพยาบาล",
"19.สาธารณสุข (public health)",
"20.การแพทย์ทางเลือก (alternative medicine)",
"21.เวชศาสตร์ฉุกเฉิน (emergency)",
"22.Physiology",
"23.Anatomy",
"24.เวชศาสตร์ฟื้นฟู",
"25.โภชนวิทยา",
"26.เวชศาสตร์การบริการโลหิต",

]

THAICULT = [
     "",
     "NO",
     "YES"
]

REVIEWSTATUS =[
     "",
     "SKIP"
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
    if st.session_state['loggedIn'] == False:
        st.error("Please login")
        st.stop()
    if len(st.session_state['ids']) > 2:
        st.session_state['ids'] = []
        # st.error("Please logout and login again")
        # st.stop()

    cursor, cnxn = reconnect()
    while True:
            if not cnxn:
                cursor, cnxn = reconnect()
            else:
                break
    
    with st.form(key="vendor_form1" , clear_on_submit=True):
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
            
            
            print("=======================================") #ORDER BY NEWID()
            #df_new = cursor.execute("SELECT TOP 1 *  from View_insert_chosen_reject WHERE actor = {} and (id_keys like 'Finance%' or id_keys like 'Legal%' or id_keys like 'Medical%') and date_actor IS NULL  and id_keys in (SELECT article_id FROM [dbo].[TD_vistec_chk] where comment = '' or ( review_wang = 'แก้ไขแล้ว' and ( Actor_wang = 'admin2' or Actor_wang = 'admin6')) or review_final_vistec = 'แก้ไขแล้ว') ;".format("'"+st.session_state['userName']+ "'"))
            df_new = cursor.execute("SELECT TOP 1 *  from View_insert_chosen_reject WHERE actor = {} and (id_keys like 'Finance%' or id_keys like 'Legal%' or id_keys like 'Medical%') and date_actor IS NULL ;".format("'"+st.session_state['userName']+ "'"))
            df_new = df_new.fetchall()
            print(len(df_new))

            if len(df_new) == 0:
                df_new = cursor.execute("SELECT TOP 1 *  from View_insert_chosen_reject WHERE actor = {} and date_actor IS NULL ;".format("'"+st.session_state['userName']+ "'"))
                df_new = df_new.fetchall()

            if len(df_new)  == 1 :
                
                df_count = cursor.execute("SELECT COUNT(*) from View_insert_chosen_reject WHERE actor = {} and status_review = '' and date_actor IS NOT NULL;".format("'"+st.session_state['userName']+ "'"))
                df_count = df_count.fetchall()

                df_count_week = cursor.execute("SELECT COUNT(*) from View_insert_chosen_reject WHERE actor = {} and status_review = '' and date_actor IS NOT NULL and date_actor > DATEADD(DAY, 1, DATEADD(DAY, 1-DATEPART(WEEKDAY, GETDATE()), CAST(GETDATE() AS DATE)))   and  date_actor < DATEADD(DAY, 2, DATEADD(DAY, 7-DATEPART(WEEKDAY, GETDATE()), CAST(GETDATE() AS DATE))) ;".format("'"+st.session_state['userName']+ "'"))
                df_count_week = df_count_week.fetchall()
                #print("df_count_week ", df_count_week)
                if df_count_week[0][0] > 140:
                    st.error("Over limit of This week")
                    st.stop()


                st.subheader( "ID: " + df_new[0][0] + " (Done: " + str(df_count[0][0]) + " Week: " + str(df_count_week[0][0]) +")", divider='rainbow')

                #st.subheader( "ID: " + df_new[0][0], divider='rainbow')

                
                if df_new[0][1] == '':
                    if "Medical" in df_new[0][0] and ("Open" in df_new[0][7] or "Classification" in df_new[0][7] or "Creative" in df_new[0][7] or "choice" in df_new[0][7] or "Brainstorming" in df_new[0][7]):
                        st.markdown(df_new[0][5])
                    if "Open" in df_new[0][7] or "Classification" in df_new[0][7] or "Creative" in df_new[0][7] or "choice" in df_new[0][7] or "Brainstorming" in df_new[0][7]:
                        st.markdown("Hint: "+df_new[0][6])
                    
                    print("df_new[0][13]", df_new[0][13])
                    if df_new[0][13] != None:
                        st.subheader("Type: "+ df_new[0][7])
                        st.subheader("Instruction:")
                        st.markdown(df_new[0][13])
                        st.subheader("Context or Article:")
                        st.markdown(df_new[0][14])
                        st.subheader("Answer:")
                        st.markdown(df_new[0][15])
                    else:
                        st.subheader("Type: "+ df_new[0][7])
                        st.subheader("Instruction:")
                        st.markdown(df_new[0][9])
                        st.subheader("Context or Article:")
                        st.markdown(df_new[0][10])
                        st.subheader("Answer:")
                        st.markdown(df_new[0][11])
                else:
                    st.subheader("Instruction:")
                    st.markdown(df_new[0][2])
                    st.subheader("Context or Article:")
                    st.markdown(df_new[0][1])
                    st.subheader("Answer:")
                    st.markdown(df_new[0][3])
                #st.subheader( "", divider='rainbow')
                    # st.subheader("Instruction: "+df_new[0][2])
                    # st.subheader("Context: "+df_new[0][1])
                    # st.subheader("Answer: "+df_new[0][3])

                #idk = st.text_input(label= "ID:", value=df_new[0][0] )
                reject1 = st.text_area(label="Reject 1*", height= 200, value="")
                reject2 = st.text_area(label="Reject 2*", height= 200, value="")

                

                
                #years_in_business = st.slider("Years in Business", 0, 50, 5)
                #onboarding_date = st.date_input(label="Onboarding Date" )
                review_status = st.selectbox("Review Status", options=REVIEWSTATUS)
                multi = '''Importance\n1. บางข้อที่มีคำถาม refer ถึงบทความ แต่ไม่มี บทความอยู่ในช่อง Context or Article ให้สามารถ skip และใส่เหตุผล\n2. กรุณาจัด format ให้อ่านง่ายๆ เพื่อคนตรวจจะได้เช็ค Quality ได้ ถ้าหาก format อ่ายยากหรือไม่ consistency เราจะ Reject ข้อความนั้น ถือว่า quality ไม่ผ่าน
                '''
                st.markdown(multi)
            
                comment_name = st.text_area(label="Comment", height= 200, value="")

                # Mark mandatory fields
                st.markdown("**required*")
                submit_button = st.form_submit_button(label="Submit Details")
                

                #If the submit button is pressed
                print("df_new[0][0] =" , df_new[0][0])
                ids = df_new[0][0]
                print("ids =" , ids)
                st.session_state['ids'].append(ids)
                print("st.session_state['ids'] =" , st.session_state['ids'])
                if submit_button:
                    if review_status != "" :
                        if  comment_name == "":
                            st.warning("please fill a reason why skip.")
                            st.session_state['ids'] = []
                            st.stop()
                        else:
                            try: 
                                # if len(st.session_state['ids']) == 2:
                                #     row1 = (st.session_state['ids'][0],reject1,reject2,review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                #     print("row1 ==>", row1)
                                #     cursor.execute("INSERT INTO TD_insert_chosen_reject(id_keys, reject_text1, reject_text2, status_review, comment, actor, date_actor ) VALUES (?,?,?,?,?,?,?)", row1)
                                #     cnxn.commit()
                                #     st.success("You skip!!")
                                #     st.session_state['ids'] = []
                                #     st.rerun()
                                # else:
                                #     st.session_state['ids'] = []
                                #     st.rerun()
                                    row1 = (df_new[0][0],reject1,reject2,review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                    print("row1 ==>", row1)
                                    cursor.execute("INSERT INTO TD_insert_chosen_reject(id_keys, reject_text1, reject_text2, status_review, comment, actor, date_actor ) VALUES (?,?,?,?,?,?,?)", row1)
                                    cnxn.commit()
                                    st.success("You skip!!")
                                    st.session_state['ids'] = []
                                    st.rerun()
                            except Exception as e:
                                st.session_state['ids'] = []
                                st.error(e)
                    elif reject1 =="" or reject2 == "":
                        st.warning("Ensure all mandatory fields are filled.")
                        st.session_state['ids'] = []
                        st.stop()
                    else:
                        try:    
                            #  if len(st.session_state['ids']) == 2:
                            #     # row2 = (st.session_state['ids'][0],reject1,reject2,review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                            #     # print("row2 ==>", row2)
                            #     # cursor.execute("INSERT INTO TD_insert_chosen_reject(id_keys, reject_text1, reject_text2, status_review, comment, actor, date_actor ) VALUES (?,?,?,?,?,?,?)", row2)
                            #     # cnxn.commit()
                            #     # st.success("Details successfully submitted!")
                            #     # st.session_state['ids'] = []
                            #     # st.rerun()
                            #  else:
                            #     st.session_state['ids'] = []
                            #     st.rerun()
                                row2 = (df_new[0][0],reject1,reject2,review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                print("row2 ==>", row2)
                                cursor.execute("INSERT INTO TD_insert_chosen_reject(id_keys, reject_text1, reject_text2, status_review, comment, actor, date_actor ) VALUES (?,?,?,?,?,?,?)", row2)
                                cnxn.commit()
                                st.success("Details successfully submitted!")
                                st.session_state['ids'] = []
                                st.rerun()
                        except Exception as e:
                                st.session_state['ids'] = []
                                st.error(e)

            else:
                 st.session_state['ids'] = []
                 if st.session_state['loggedIn'] == False or "USER" not in st.session_state['userName']:
                      st.subheader("Please login again")
                 else:
                      st.subheader("Data all complete")
                      
