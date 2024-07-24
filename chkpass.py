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

TAGS_reason = [
 "จัด format ไม่ดี อ่านยาก",
 "ไม่มีการแนบ บทความหรือข้อมูล ที่กล่าวถึง",
 "มีการเกริ่นนําหรือมี เนื้อหาที่เหมือน Copy มาจาก บทความ",
 "มีภาษาอื่นแทรกมา, เขียนไม่ถูกต้อง หรือ มีลิ้งปนมา",
 "รายละเอียดเยอะไป โจทย์ถามอะไร ให้ตอบแค่นั้น",
 "ขึ้นบรรทัดใหม่ เยอะเกินไป พารากราฟเดียวกันห้ามขึ้นบรรทัดใหม่ หรือ ควรแบ่งเป็นข้อๆให้ชัดเจน ใส่ขีด หรือ ตัวเลข",
 "งง คำถาม คำตอบว่า ถามอะไร ตอบอะไร",
 "ข้อความมันติดกันยาว ไม่มีย่อหน้าเว้นวรรคให้หายเหนื่อยบ้างเลย ตอนอ่าน",
 "ควร ขึ้นบรรทัดใหม่ แยกสัดส่วนกันในแต่หัวข้อ ตอนนี้มันไปติดข้อก่อนหน้า"
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

 
REVIEWSTATUS_WANG =[
     "",
     "แก้ไขแล้ว",
     "แก้ไขไม่ได้"
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
    if st.session_state['loggedIn'] == False or "ADMIN" not in st.session_state['userName'].upper() :
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
    
    df_new = []
    #df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE (url like '%www.longtunman.com%' or url like '%www.finnomena.com%' or url like '%khemmapat.org%' or url like '%www.lawsiam.com%' or url like '%srisunglaw.com%' or url like '%www.thanulegal.com%' or url like '%www.nstda.or.th%' or url like '%www.petcharavejhospital.com%') and review_status = 'PASS' and vistec_chk IS NULL ")
    #and article_id like '%9'
    if "ADMIN3" in st.session_state['userName'].upper(): 
        df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  review_status = 'PASS' and vistec_chk IS NULL and (article_id like '%7' or article_id like '%4') ")
        df_new = df_new.fetchall()
    elif "ADMIN4" in st.session_state['userName'].upper(): 
        df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  review_status = 'PASS' and vistec_chk IS NULL and (article_id like '%3' or article_id like '%8' )")
        df_new = df_new.fetchall()
    elif "ADMIN9" in st.session_state['userName'].upper(): 
        df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE   review_status = 'PASS' and vistec_chk IS NULL and  ( article_id like '%5') ")
        df_new = df_new.fetchall()
    elif "ADMIN8" in st.session_state['userName'].upper(): 
        df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  review_status = 'PASS' and vistec_chk IS NULL and (article_id like '%0' or article_id like '%9' )")
        df_new = df_new.fetchall()
    elif "ADMIN1" in st.session_state['userName'].upper(): 
        df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE   review_status = 'PASS' and vistec_chk IS NULL and (article_id like '%6' or article_id like '%1'  )")
        df_new = df_new.fetchall()
    elif "ADMIN5" in st.session_state['userName'].upper(): 
        df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE   review_status = 'PASS' and vistec_chk IS NULL and (article_id like '%2' )")
        df_new = df_new.fetchall()
    # elif "ADMIN" == st.session_state['userName'].upper(): 
    #     df_new = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE   review_status = 'PASS' and vistec_chk IS NULL and (article_id like '%9' )")
    #     df_new = df_new.fetchall()
    


    REVIEWSTATUS =[
        "",
     "PASS",
     "NOT PASS"
    ]
    # df_count = cursor.execute("SELECT COUNT(*) from View_vistec_check WHERE Actor_vistec = {}  and vistec_chk IS NOT NULL;".format("'"+st.session_state['userName']+ "'"))
    # df_count = df_count.fetchall() 
    #print(st.session_state['userName'].upper())


    if "ADMIN6" in st.session_state['userName'].upper():
       df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  review_status = 'PASS' and vistec_chk IS NOT NULL and status_vistec = 'PASS' and vistec_chk > DATEADD(DAY, 1, DATEADD(DAY, 1-DATEPART(WEEKDAY, GETDATE()), CAST(GETDATE() AS DATE)))   and  vistec_chk < DATEADD(DAY, 2, DATEADD(DAY, 7-DATEPART(WEEKDAY, GETDATE()), CAST(GETDATE() AS DATE))) ORDER BY NEWID()")
       df_new1 = df_new1.fetchall()

       st.subheader(df_new1[0][1] + "  (Actor: " +  df_new1[0][16] + " )", divider='rainbow')
       st.subheader("Instruction:")
       st.markdown(df_new1[0][4].replace('\n', '<br>'), unsafe_allow_html=True)
       st.subheader("Input:")
       st.markdown(df_new1[0][5].replace('\n', '<br>'), unsafe_allow_html=True)
       st.subheader("Output:")
       st.markdown(df_new1[0][6].replace('\n', '<br>'), unsafe_allow_html=True )
       st.subheader("Comment:")
       st.markdown(df_new1[0][18])

    if "ADMIN2" in st.session_state['userName'].upper():
       #print("erererrrrrrrrrr")
       #df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE status_vistec IS NOT NULL and  comment_vistec != '' ORDER BY NEWID()")
       if "ADMIN2" in st.session_state['userName'].upper():
            df_new1 = cursor.execute("SELECT TOP 1 * from TD_vistec_chk WHERE Actor_wang  IS NOT NULL and review_wang = 'แก้ไขแล้ว' and (article_id like '%0' or article_id like '%1' or article_id like '%2' or article_id like '%3' or article_id like '%4' ) and Actor_wang != 'admin2' and Actor_wang != 'admin6' and Actor_final_vistec IS NULL ") 
            df_new1 = df_new1.fetchall()

            # df_new1 = cursor.execute("SELECT TOP 1 * from TD_vistec_chk WHERE article_id in (SELECT id_keys FROM View_insert_chosen_reject where actor = 'USER9') and Actor_wang  IS NOT NULL and review_wang = 'แก้ไขแล้ว' and Actor_wang != 'admin2' and Actor_wang != 'admin6' and Actor_final_vistec IS NULL  ") 
            # df_new1 = df_new1.fetchall()

            # df_new1 = cursor.execute("SELECT TOP 1 * from TD_vistec_chk WHERE article_id  = 'Finance_40743'  ") 
            # df_new1 = df_new1.fetchall()

       else:
           df_new1 = cursor.execute("SELECT TOP 1 * from TD_vistec_chk WHERE Actor_wang  IS NOT NULL and review_wang = 'แก้ไขแล้ว' and (article_id like '%5' or article_id like '%6' or article_id like '%7' or article_id like '%8' or article_id like '%9' ) and Actor_wang != 'admin2' and Actor_wang != 'admin6' and Actor_final_vistec IS NULL ")
           df_new1 = df_new1.fetchall()

       #st.subheader(df_new1[0][0], divider='rainbow')
       df_count = cursor.execute("SELECT COUNT(*) from TD_vistec_chk WHERE Actor_final_vistec = {} and Date_actor_wang IS NOT NULL;".format("'"+st.session_state['userName']+ "'"))
       df_count = df_count.fetchall() 
       st.subheader(df_new1[0][0]  + " ( Done: " + str(df_count[0][0]) + " )", divider='rainbow')
    #    st.subheader("Type:")
    #    st.markdown(df_new1[0][3])
       st.subheader("Instruction:")
       st.markdown(df_new1[0][5].replace('\n', '<br>'), unsafe_allow_html=True)
       st.subheader("Input:")
       st.markdown(df_new1[0][6].replace('\n', '<br>'), unsafe_allow_html=True)
       st.subheader("Output:")
       st.markdown(df_new1[0][7].replace('\n', '<br>'), unsafe_allow_html=True )
       st.subheader("Comment:")
       st.markdown(df_new1[0][2])

       with st.form(key="vendor_form1" , clear_on_submit=True):
                inst1 = st.text_area(label="Instruction:", height= 50, value=df_new1[0][5])
                input1 = st.text_area(label="Input:", height= 400, value=df_new1[0][6])
                outpu = st.text_area(label="Output:", height= 600, value=df_new1[0][7])

                review_status = st.selectbox("Review Status", options=REVIEWSTATUS_WANG)
                comment_name = st.text_area(label="Comment", height= 200, value="")
                submit_button = st.form_submit_button(label="Submit Details")

                can_save = 1
                if submit_button:
                        if review_status == "" :
                            can_save == 0
                            st.warning("please choose Review Status.")
                            st.stop()
                        elif review_status == "แก้ไขไม่ได้" :
                            if  comment_name == "":
                                can_save == 0
                                st.warning("please fill a reason why NOT PASS.")
                                st.stop()
                            
                        if can_save == 1:
                            try:
                                # row2 = (df_new[0][1],review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                # print("row2 ==>", row2)

                                # cursor.execute("INSERT INTO TD_vistec_chk(article_id, review_status, comment, Actor, Date_actor ) VALUES (?,?,?,?,?)", row2)
                                # cnxn.commit()
                                article_id = df_new1[0][0]
                                row2 = (inst1, input1, outpu,review_status, comment_name ,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                print("row2 ==>", row2)
                                print("article_id ==>", article_id)

                                # Construct the SQL UPDATE statement
                                update_query = """
                                    UPDATE TD_vistec_chk
                                    SET instruction_wang = ?, input_wang = ?, output_wang = ?, review_final_vistec = ?, comment_final_vistec = ?, Actor_final_vistec = ?, Date_actor_final_vistec = ?
                                    WHERE article_id = ?
                                """

                                # Execute the UPDATE statement
                                cursor.execute(update_query, (*row2, article_id))
                                cnxn.commit()
                                st.success("Details successfully submitted!")
                                st.rerun()

                            except Exception as e:
                                st.error(e)
    #    comment_name1 = st.text_area(label="Instruction:", height= 50, value=df_new1[0][5])
    #    comment_name2 = st.text_area(label="Input:", height= 200, value=df_new1[0][6])
    #    comment_name3 = st.text_area(label="Output:", height= 400, value=df_new1[0][7])

    if "ADMIN11" in st.session_state['userName'].upper() or "ADMIN12" in st.session_state['userName'].upper() or "ADMIN13" in st.session_state['userName'].upper() or "ADMIN14" in st.session_state['userName'].upper() or "ADMIN15" in st.session_state['userName'].upper() or "ADMIN16" in st.session_state['userName'].upper() or "ADMIN17" in st.session_state['userName'].upper() or "ADMIN18" in st.session_state['userName'].upper() or "ADMIN19" in st.session_state['userName'].upper():
            
        df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%3') ")
        df_new1 = df_new1.fetchall()
        user = cursor.execute("SELECT jobs from TM_related_job WHERE username = {} ;".format("'"+st.session_state['userName']+ "'"))
        user = user.fetchall() 
        print(user)
        if len(user) > 0:
                #B_list = [ 'article_id like ' +f"'%{item.strip()}'" for item in user[0][0].split(',')]
                B_list = [ 'article_id like ' + (f"'%{item.strip()}%'" if item.strip() == "fix" else f"'%{item.strip()}'") for item in user[0][0].split(',') ]
                y1 = "("
                for hhh in B_list:
                    y1 =y1 + hhh + " or "

                y1 = y1[:-3] + ")"
                #print(y1)
                df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and {} ".format(y1))
                df_new1 = df_new1.fetchall() 
    #    if "ADMIN11" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%3') ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN12" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%5' or article_id like '%70' or article_id like '%80' or article_id like '%90') ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN13" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%00' or article_id like '%10' or article_id like '%20'  ) ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN14" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%9') ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN15" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%01' or article_id like '%11' or article_id like '%21' or article_id like '%31' or article_id like '%41') ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN16" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%51' or article_id like '%61' ) ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN17" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%2') ")
    #         df_new1 = df_new1.fetchall()
    #    elif "ADMIN18" in st.session_state['userName'].upper():
    #         df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE  comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%8' or article_id like '%54' or article_id like '%64' or article_id like '%74' or article_id like '%84' or article_id like '%94' or article_id like '%71' or article_id like '%81' or article_id like '%91' or article_id like '%30' or article_id like '%40')  ")
    #         df_new1 = df_new1.fetchall()
    #    else:
    #        df_new1 = cursor.execute("SELECT TOP 1 * from View_vistec_check WHERE   comment_vistec != '' and Date_actor_wang IS NULL and (article_id like '%50' or article_id like '%60' or article_id like '%04' or article_id like '%14' or article_id like '%24' or article_id like '%34' or article_id like '%44' or article_id like '%6' or article_id like '%7') ")
    #        df_new1 = df_new1.fetchall()

        df_count = cursor.execute("SELECT COUNT(*) from View_vistec_check WHERE Actor_wang = {} and Date_actor_wang IS NOT NULL;".format("'"+st.session_state['userName']+ "'"))
        df_count = df_count.fetchall() 

        if len(df_new1)  == 1:
            st.subheader(df_new1[0][1]  + " ( Done: " + str(df_count[0][0]) + " )", divider='rainbow')
            st.subheader("Type:")
            st.markdown(df_new1[0][3])
            st.subheader("Instruction:")
            st.markdown(df_new1[0][4].replace('\n', '<br>'), unsafe_allow_html=True)
            st.subheader("Input:")
            st.markdown(df_new1[0][5].replace('\n', '<br>'), unsafe_allow_html=True)
            st.subheader("Output:")
            st.markdown(df_new1[0][6].replace('\n', '<br>'), unsafe_allow_html=True)

            st.subheader("Comment:")
            st.markdown(df_new1[0][18])


            with st.form(key="vendor_form1" , clear_on_submit=True):
                inst1 = st.text_area(label="Instruction:", height= 50, value=df_new1[0][4])
                input1 = st.text_area(label="Input:", height= 200, value=df_new1[0][5])
                outpu = st.text_area(label="Output:", height= 400, value=df_new1[0][6])

                review_status = st.selectbox("Review Status", options=REVIEWSTATUS_WANG)
                comment_name = st.text_area(label="Comment", height= 200, value="")
                submit_button = st.form_submit_button(label="Submit Details")

                can_save = 1
                if submit_button:
                        if review_status == "" :
                            can_save == 0
                            st.warning("please choose Review Status.")
                            st.stop()
                        elif review_status == "แก้ไขไม่ได้" :
                            if  comment_name == "":
                                can_save == 0
                                st.warning("please fill a reason why NOT PASS.")
                                st.stop()
                            
                        if can_save == 1:
                            try:
                                # row2 = (df_new[0][1],review_status,comment_name,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                # print("row2 ==>", row2)

                                # cursor.execute("INSERT INTO TD_vistec_chk(article_id, review_status, comment, Actor, Date_actor ) VALUES (?,?,?,?,?)", row2)
                                # cnxn.commit()
                                article_id = df_new1[0][1]
                                row2 = (inst1, input1, outpu,review_status, comment_name ,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                                print("row2 ==>", row2)
                                print("article_id ==>", article_id)

                                # Construct the SQL UPDATE statement
                                update_query = """
                                    UPDATE TD_vistec_chk
                                    SET instruction_wang = ?, input_wang = ?, output_wang = ?, review_wang = ?, comment_wang = ?, Actor_wang = ?, Date_actor_wang = ?
                                    WHERE article_id = ?
                                """

                                # Execute the UPDATE statement
                                cursor.execute(update_query, (*row2, article_id))
                                cnxn.commit()
                                st.success("Details successfully submitted!")
                                st.rerun()

                            except Exception as e:
                                st.error(e)


    
    if len(df_new)  == 1 and ( "ADMIN2" not in st.session_state['userName'].upper() and "ADMIN6" not in st.session_state['userName'].upper() and "ADMIN10" not in st.session_state['userName'].upper() and "ADMIN11" not in st.session_state['userName'].upper() and "ADMIN12" not in st.session_state['userName'].upper() and "ADMIN13" not in st.session_state['userName'].upper() and "ADMIN14" not in st.session_state['userName'].upper() and "ADMIN15" not in st.session_state['userName'].upper() and "ADMIN16" not in st.session_state['userName'].upper() and "ADMIN17" not in st.session_state['userName'].upper() and "ADMIN18" not in st.session_state['userName'].upper() and "ADMIN19" not in st.session_state['userName'].upper()):

       df_count = cursor.execute("SELECT COUNT(*) from View_vistec_check WHERE Actor_vistec = {}  and vistec_chk IS NOT NULL;".format("'"+st.session_state['userName']+ "'"))
       df_count = df_count.fetchall() 
       
       st.subheader(df_new[0][1]  + " ( Done: " + str(df_count[0][0]) + " )", divider='rainbow')
       st.subheader("Type:")
       st.markdown(df_new[0][3])
       st.subheader("Instruction:")
       st.markdown(df_new[0][4].replace('\n', '<br>'), unsafe_allow_html=True)
       st.subheader("Input:")
       st.markdown(df_new[0][5].replace('\n', '<br>'), unsafe_allow_html=True)
       st.subheader("Output:")
       st.markdown(df_new[0][6].replace('\n', '<br>'), unsafe_allow_html=True)



       with st.form(key="vendor_form1" , clear_on_submit=True):
           review_status = st.selectbox("Review Status", options=REVIEWSTATUS)
           comment_tag = st.multiselect("Reason If NOT PASS", options=TAGS_reason ) 
           comment_name = st.text_area(label="Comment", height= 200, value="")
           submit_button = st.form_submit_button(label="Submit Details")
           


           can_save = 1
           if submit_button:
                

                if review_status == "" :
                    can_save == 0
                    st.warning("please choose Review Status.")
                    st.stop()
                elif review_status == "NOT PASS" :
                    if  comment_name == "" and len(comment_tag) == 0:
                        can_save == 0
                        st.warning("please fill a reason why NOT PASS.")
                        st.stop()
                    
                if can_save == 1:
                    try:
                        comment_tag = ", ".join(comment_tag)
                        new_ment = comment_tag +  ", " +comment_name
                        if new_ment == ", ":
                            new_ment = ""

                        row2 = (df_new[0][1],review_status,new_ment,st.session_state['userName'],datetime.now(pytz.timezone('Asia/Bangkok')))
                        print("row2 ==>", row2)

                        cursor.execute("INSERT INTO TD_vistec_chk(article_id, review_status, comment, Actor, Date_actor ) VALUES (?,?,?,?,?)", row2)
                        cnxn.commit()
                        st.success("Details successfully submitted!")
                        st.rerun()
                    except Exception as e:
                        st.error(e)
               
           
                      
