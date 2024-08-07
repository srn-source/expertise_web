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
"98.กฎหมายชุมนุม",
"99.คำพิพากษาศาลปกครอง"
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
    st.session_state['ids'] = []
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
            cursor, cnxn = reconnect()
            while True:
                if not cnxn:
                    cursor, cnxn = reconnect()
                    print("ok")
                else:
                    break

            if "FINANCE" in st.session_state['userName'].upper() or "LEGAL" in st.session_state['userName'].upper(): 
                df_new = cursor.execute("SELECT TOP 1 * from View_info_insert WHERE actor_master = {} and date_insert IS NULL and (url like '%www.longtunman.com%' or url like '%www.finnomena.com%' or url like '%khemmapat.org%' or url like '%www.lawsiam.com%' or url like '%srisunglaw.com%' or url like '%www.thanulegal.com%' or url like '%www.nstda.or.th%' or url like '%www.petcharavejhospital.com%');".format("'"+st.session_state['userName']+ "'"))
            else:
                df_new = cursor.execute("SELECT TOP 1 * from View_info_insert WHERE actor_master = {} and date_insert IS NULL;".format("'"+st.session_state['userName']+ "'"))
            df_new = df_new.fetchall()

            if len(df_new)  == 0: #กรณีดาต้าหมด
                df_new = cursor.execute("SELECT TOP 1 * from View_info_insert WHERE actor_master = {} and date_insert IS NULL;".format("'"+st.session_state['userName']+ "'"))
                df_new = df_new.fetchall()
            #print(df_new)
            if len(df_new)  == 1:
                
                st.subheader(df_new[0][11], divider='rainbow')
                if "Medical" in df_new[0][0] and ("Open" in df_new[0][3] or "Classification" in df_new[0][3] or "Creative" in df_new[0][3] or "choice" in df_new[0][3] or "Brainstorming" in df_new[0][3]):
                    st.markdown(df_new[0][10])

                if "Open" in df_new[0][3] or "Classification" in df_new[0][3] or "Creative" in df_new[0][3] or "choice" in df_new[0][3] or "Brainstorming" in df_new[0][3]:
                    st.markdown("Link ref.: "+df_new[0][12])

                st.subheader("Instruction Task Type: "+ df_new[0][3])
                
                
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
                review_status = st.selectbox("Review Status* (หาก Criteria แม้ 1 ข้อไม่ผ่าน จะต้องใส่ NOT_PASS เพื่อตีกลับไปแก้ไข)", options=REVIEWSTATUS)

                multi = '''Criteria\n1. Output is reasonable\n2. Correct information?*\n3. Makesene question\n4. Knowledge or Culture specific questions (Optional)
                '''
                st.markdown(multi)
            
                comment_name = st.text_area(label="Comment*", height= 200, value="")

                # Mark mandatory fields
                st.markdown("**required*")

                submit_button = st.form_submit_button(label="Submit Details")
                

                #If the submit button is pressed
                if submit_button:
                    # Check if all mandatory fields are filled
                    if not Instruction_name  or not Answer or not comment_name or not review_status or not domain_tag or not thai_spec:
                        st.warning("Ensure all mandatory fields are filled.")
                        st.stop()
                    else:
                        domain_tag = ",".join(domain_tag)
                        row = (df_new[0][0],df_new[0][1],df_new[0][2],df_new[0][3],df_new[0][13],Instruction_name,input_name,Answer,domain_tag,thai_spec,review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                        cursor.execute("INSERT INTO TD_insert(type_domain, article_id, rev, task_type, task_type_id, Instruction, Input, Output, domain_tags, thai_specific, review_status, comment, Actor, Date_actor ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
                        cnxn.commit()
                        st.success("Details successfully submitted!")
                        st.rerun()
                        # try:
                        #     domain_tag = ",".join(domain_tag)
                        #     #cursor.execute('INSERT INTO TD_insert(type_domain, article_id, task_type, Instruction, Input, Output) VALUES (?,?,?,?,?,?)', tuple(row))
                        #     row = (df_new[0][0],df_new[0][1],df_new[0][2],df_new[0][3],df_new[0][13],Instruction_name,input_name,Answer,domain_tag,thai_spec,review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                        #     cursor.execute("INSERT INTO TD_insert(type_domain, article_id, rev, task_type, task_type_id, Instruction, Input, Output, domain_tags, thai_specific, review_status, comment, Actor, Date_actor ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
                        #     cnxn.commit()
                        #     st.success("Details successfully submitted!")
                        #     st.rerun()
                        # except Exception as e:
                        #     st.error(e)

            else:
                 if st.session_state['loggedIn'] == False or "USER" in st.session_state['userName'] :
                      st.subheader("Please login again")
                 else:
                      st.subheader("Data all complete")
                      
