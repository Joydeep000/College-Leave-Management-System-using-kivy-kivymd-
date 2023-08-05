from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import mysql.connector
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget
import random
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from datetime import datetime
from kivymd.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import re
from kivymd.uix.filemanager import MDFileManager
from io import BytesIO
from PIL import Image
from kivymd.uix.textfield import MDTextField
import smtplib
from kivymd.uix.dialog import MDDialog
import os
from kivymd.uix.button import MDFlatButton
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior



class ProfileCard(MDFloatLayout,FakeRectangularElevationBehavior):
    pass

Window.size = (310,570)







""",red,pink, 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 
'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']"""

class LeavesystemApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
        )
        self.file_mana = MDFileManager(
            exit_manager=self.exit_file_mana,
            select_path=self.select_pa,
        )
        self.file_manae = MDFileManager(
            exit_manager=self.exit_file_manae,
            select_path=self.select_pae,
        )



    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Cyan"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()

        # create actual db

        # create a secondary table to store employee records
        c.execute("""CREATE TABLE if not exists secondary_table(Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) UNIQUE,Phone_Number NUMERIC(14) UNIQUE,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists teaching_records (Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) UNIQUE,Phone_Number NUMERIC(14) UNIQUE,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists non_teaching_records (Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) UNIQUE,Phone_Number NUMERIC(14) UNIQUE,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists admin_records (Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) UNIQUE,Phone_Number NUMERIC(14) UNIQUE,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")
        c.execute("INSERT IGNORE INTO admin_records VALUES('E0001A', 'ABC', 'abc@gmail.com', 1234567890, 'hello@123', '2023-07-04', 'Admin', 'Male', 'NONE', 'NONE')")

        #Leave tables
        c.execute("""CREATE TABLE if not exists teaching_leave_record(Employee_ID VARCHAR(50) UNIQUE,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(40),From_Date DATE,To_Date DATE,reason VARCHAR(30))""")
        c.execute("""CREATE TABLE if not exists non_teaching_leave_record(Employee_ID VARCHAR(50) UNIQUE,Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(100),From_Date DATE,To_Date DATE,reason VARCHAR(100))""")

        #Leave Balance
        c.execute("""CREATE TABLE if not exists leave_balance(Employee_ID VARCHAR(50) PRIMARY KEY,Casual_Leave INT,Earned_Leave INT,last_updated DATE)""")

        #notice
        c.execute("CREATE TABLE if not exists notice(Employee_ID VARCHAR(50) ,Sentence VARCHAR(100))")
        #employee photo table
        c.execute("CREATE TABLE if not exists dp(Employee_ID VARCHAR(50) ,pic LONGBLOB)")
        # employee birth certificate photo table
        c.execute("CREATE TABLE if not exists the_captured_image(Employee_ID VARCHAR(50) ,the_image LONGBLOB)")

        #leave history table
        c.execute("""CREATE TABLE if not exists leave_history(Employee_ID VARCHAR(50),Name VARCHAR(50),Leave_type VARCHAR(100),emp_type VARCHAR(40),From_Date DATE,To_Date DATE,reason VARCHAR(30),eventtime DATETIME,status VARCHAR(15))""")
        mydb.commit()

        global sm
        sm = ScreenManager()

        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("new_log3.kv"))
        sm.add_widget(Builder.load_file("new_signup2.kv"))
        sm.add_widget(Builder.load_file("new_teaching_dashboard.kv"))
        sm.add_widget(Builder.load_file("new_non_teaching_dashboard.kv"))
        sm.add_widget(Builder.load_file("new_admin_dashboard.kv"))
        sm.add_widget(Builder.load_file("employees_list.kv"))
        sm.add_widget(Builder.load_file("add_employee_details.kv"))
        sm.add_widget(Builder.load_file("Leave_request.kv"))
        sm.add_widget(Builder.load_file("leave_list.kv"))
        sm.add_widget(Builder.load_file("employee_leave_details.kv"))
        sm.add_widget(Builder.load_file("check_balance.kv"))
        sm.add_widget(Builder.load_file("check_balance_empid.kv"))
        sm.add_widget(Builder.load_file("check_balance_empid1.kv"))
        sm.add_widget(Builder.load_file("update_profile.kv"))
        sm.add_widget(Builder.load_file("notice.kv"))
        sm.add_widget(Builder.load_file("notice2.kv"))
        sm.add_widget(Builder.load_file("Leave_request_edit.kv"))
        sm.add_widget(Builder.load_file("upload_certificate.kv"))
        sm.add_widget(Builder.load_file("noticelist.kv"))
        sm.add_widget(Builder.load_file("leave_con_report.kv"))
        sm.add_widget(Builder.load_file("details_of_employee.kv"))
        sm.add_widget(Builder.load_file("show_document.kv"))
        sm.add_widget(Builder.load_file("show_edit_doc.kv"))
        sm.add_widget(Builder.load_file("test_appdrawer.kv"))
        sm.add_widget(Builder.load_file("leave_history_list.kv"))
        sm.add_widget(Builder.load_file("forgot_password.kv"))

        return sm





    def on_start(self):
        # Schedule a function to be called after 3 seconds
        Clock.schedule_once(self.next_screen, 5)
        self.increment()
    def next_screen(self,dt):

        MDApp.get_running_app().root.current = 'login'
    def increment(self):
        print("Hello")
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            tup = (0,)
            tap =0
            # create a cursor
            c = mydb.cursor()
            current_date = datetime.now().date()

            c.execute("SELECT Employee_ID FROM leave_balance")
            row = c.fetchall()
            print(row)
            for i in row:
                c.execute("SELECT last_updated from leave_Balance WHERE Employee_ID = %s ", i)
                last_updated_date = c.fetchone()

                if (current_date - last_updated_date[0]).days >= 365:
                    c.execute("UPDATE leave_Balance SET Earned_Leave = Earned_Leave + 10 WHERE Employee_ID = %s", i)
                    c.execute("UPDATE leave_Balance SET Casual_Leave = 12 WHERE Employee_ID = %s", i)
                    tup = i
                    tap = str(tup[0])
                    last_updated_date = current_date
                    c.execute("UPDATE leave_Balance SET last_updated = %s WHERE Employee_ID = %s",(last_updated_date,tap))
                    mydb.commit()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()




    def forgot_password(self, email_ph,etype):
        print(email_ph)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        global t
        if etype == "Admin":
            t = 'admin_records'
        elif etype == "Teaching Employee":
            t = 'teaching_records'
        elif etype == "Non-Teaching Employee":
            t = 'non_teaching_records'

        c.execute("SELECT password from {} WHERE email_ID = %s".format(t),(email_ph,))
        row = c.fetchone()
        if row is None:
            dialog = MDDialog(
                title='Notice',
                text="Your email is not registered in our database"
            )
            dialog.open()
        else:
            self.verify_pass_otp(email_ph,t)


    def verify_pass_otp(self,email_id,etype):
        try:
            rand = str(random.randint(100000, 999999))

            # Get the email details from the text fields
            email = "jr1954674@gmail.com"
            password = "yzofpmcpumpyddmg"
            recipient = email_id
            subject =" OTP"
            message = rand

            # Connect to the email server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.ehlo()
            server.login(email, password)

            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail(email, recipient, email_message)
            server.quit()

            dialo = MDDialog(
                title="Enter the OTP sent to you",
                type="custom",
                auto_dismiss=False,
                content_cls=MDTextField(hint_text="Enter OTP", size_hint=(None, None), width=280),
                buttons=[
                    MDFlatButton(text="Cancel", on_release=lambda *args: dialo.dismiss()),
                    MDFlatButton(text="OK",
                                 on_release=lambda *args: self.process_pass_input(rand, dialo.content_cls.text,email_id,etype,dialo)),
                ],
            )

            dialo.open()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text="Enter the data correctly"
            )
            dialog.open()

    def process_pass_input(self, rand, otp,email_id,etype,dialo):
        print(rand, otp)
        try:
            if otp == rand:
                print("continue")
                dialog = MDDialog(
                    title="Enter your new password",
                    type="custom",
                    auto_dismiss=False,
                    content_cls=MDTextField(hint_text="New Password", size_hint=(None, None), width=280),
                    buttons=[
                        MDFlatButton(text="Cancel", on_release=lambda *args: dialog.dismiss()),
                        MDFlatButton(text="OK",
                                     on_release=lambda *args: self.update_password(dialog.content_cls.text,email_id,etype, dialog)),
                    ],
                )

                dialog.open()
                # close another dialog from here
                dialo.dismiss()

            else:
                dialog = MDDialog(
                    title='Warning',
                    text="Wrong OTP"
                )
            dialog.open()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def update_password(self,passwrd,email_id,etype,dialog):
        print(passwrd,email_id,etype)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()
        c.execute("UPDATE {} SET password = %s WHERE email_ID = %s".format(etype),(passwrd,email_id,))
        dialoge = MDDialog(
            title='Notice',
            text="Your Password is changed"
        )
        dialoge.open()
        dialog.dismiss(())
        sm.current='login'
        mydb.commit()
        mydb.close()







    def toggle_password_visibility(self, password_field):
        print("helo")
        if password_field.password:
            password_field.password = False
            password_field.icon_right = "eye"

        else:
            password_field.password = True
            password_field.icon_right = "eye-off"

    """def open_date_picker(self, text_input_id):
        # Create an instance of the MDDatePicker widget
        date_dialog = MDDatePicker(size_hint=(None, None), size=(50,60))

        date_dialog.bind(on_save=lambda instance, value, date_range: self.on_date_save(text_input_id, value))


        # Adjust the size_hint_min and size_hint_max if necessary
        #date_dialog.size_hint_min = (0.5, 0.5)  # Set a minimum size (90% width, 60% height)


        # Open the date picker dialog
        date_dialog.open()

    def on_date_save(self, text_input_id, value):
        # Get the current screen from the ScreenManager
        current_screen = sm.current_screen

        # Access the text input widget with the specified id in the current screen
        text_input = current_screen.ids[text_input_id]

        # Format the selected date in the day-month-year format
        formatted_date = value.strftime('%d-%m-%Y')

        # Set the formatted date as the text of the text input widget
        text_input.text = formatted_date"""


    '''def send_email(self, *args):
        
        
        
        
        try:
            # Get the email details from the text fields
            email = "jr1954674@gmail.com"
            password = "eysdmzhuxvuenezz"
            recipient = .text
            subject =" OTP"
            message = rand

            # Connect to the email server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.ehlo()
            server.login(email, password)

            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail(email, recipient, email_message)
            server.quit()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text=f"{e}"
            )
            dialog.open()'''








    def verify_otp(self,):

        try:
            rand = str(random.randint(100000, 999999))
            det= sm.get_screen('signup')
            # Get the email details from the text fields
            email = "jr1954674@gmail.com"
            password = "yzofpmcpumpyddmg"
            recipient = det.ids.email_id.text
            subject =" OTP"
            message = rand

            # Connect to the email server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.ehlo()
            server.login(email, password)

            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            server.sendmail(email, recipient, email_message)
            server.quit()

            dialo = MDDialog(
                title="Enter the OTP sent to you",
                type="custom",
                auto_dismiss=False,
                content_cls=MDTextField(hint_text="Enter OTP", size_hint=(None, None), width=280),
                buttons=[
                    MDFlatButton(text="Cancel", on_release=lambda *args: dialo.dismiss()),
                    MDFlatButton(text="OK",
                                 on_release=lambda *args: self.process_input(rand, dialo.content_cls.text, dialo)),
                ],
            )

            dialo.open()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text="Enter the data correctly"
            )
            dialog.open()





    '''def send_by_thread(self):
        
        det = sm.get_screen('signup')

        recipient = det.ids.email_id.text

        # Start a new thread to send the email
        t1 = th.Thread(
            target=self.verify_otp,
            args=(recipient,),
        )
        t1.start()'''


    def process_input(self, rand, otp, dialo):
        print(rand, otp)
        try:
            if otp == rand:
                print("continue")
                dialog = MDDialog(
                    title='Notice',
                    text="Your emeail is verified"
                )
                dialog.open()
                # close another dialog from here
                dialo.dismiss()

            else:
                dialog = MDDialog(
                    title='Warning',
                    text="Wrong OTP"
                )
            dialog.open()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def leave_history_list(self):
        print("running")
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()
            global u, empid
            c = mydb.cursor()
            det = sm.get_screen('login')
            t = det.ids.login_as.text
            if t == "Teaching Employee":
                u = sm.get_screen('teaching_dashboard')
                empid = u.ids.tea.text

            if t == "Non-Teaching Employee":
                u = sm.get_screen('non_teaching_dashboard')
                empid = u.ids.non_tea.text


            # Retrieve the employee data
            c.execute("SELECT Name, Employee_ID,eventtime FROM leave_history WHERE Employee_ID =%s",(empid,))
            row = c.fetchone()

            current_date = row[2]
            formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            sm.current = 'leave_history_list'


            # Create the teaching employee leave list
            leave_list = self.root.get_screen('leave_history_list').ids.container
            leave_list.clear_widgets()  # Clear existing widgets before populating the list
            for ro in row:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = ThreeLineListItem(text=ro[0],secondary_text=str(ro[1]),tertiary_text=str(formatted_date))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.leave_history_details)
                # Add the TwoLineListItem to the employee list
                leave_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()


    def leave_history_details(self, item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            # Retrieve the employee details
            c.execute("SELECT * FROM leave_history WHERE Employee_ID = %s AND eventtime=%s", (item.secondary_text,item.tertiary_text))
            row = c.fetchone()

            sm.current = 'emp_leave_details'

            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('emp_leave_details')

            employee_details_screen.ids.ltype.text = str(row[2])
            employee_details_screen.ids.emp_type.text = str(row[3])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.fdate.text = str(row[4])
            employee_details_screen.ids.tdate.text = str(row[5])
            employee_details_screen.ids.reason.text = str(row[6])
            employee_details_screen.ids.empid.text = item.secondary_text
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def dashboard_details(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            # create a cursor
            c = mydb.cursor()

            global u, empid
            c = mydb.cursor()
            det = sm.get_screen('login')
            t = det.ids.login_as.text
            if t == "Teaching Employee":
                u = sm.get_screen('teaching_dashboard')
                empid = u.ids.tea.text

            if t == "Non-Teaching Employee":
                u = sm.get_screen('non_teaching_dashboard')
                empid = u.ids.non_tea.text

            if t == "Admin":
                u = sm.get_screen('admin_dashboard')
                empid = u.ids.admin.text
            c.execute("SELECT the_image FROM the_captured_image WHERE Employee_ID = %s",(empid,))
            row = c.fetchone()
            if row is None:
                print("none")
            else:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))
                image.save("temp_image.jpg")
                det = sm.get_screen('admin_dashboard')

                det.ids.name.text = "hey"
                det.ids.empid.text = "hey"
                det.ids.email.text = "hey"
                det.ids.phone.text = "hey"
                det.ids.jdate.text = "hey"
                det.ids.my_image.source = 'temp_image.jpg'
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()


    def open_file_manager(self):
        try:
            self.file_manager.show('/')  # Show the file manager starting from the root directory
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def select_path(self, path):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            dete=sm.get_screen('Leave_Request_Form')
            emp = dete.ids.empid.text
            self.cursor = self.mydb.cursor()
            # Handle the selected image file path here
            self.file_manager.close()
            print("Selected File:", path)
            det = sm.get_screen('certificate')
            det.ids.my_image.source = path
            with open(path, 'rb') as image_file:
                img = image_file.read()
                self.cursor.execute("SELECT * FROM the_captured_image WHERE Employee_ID=%s",(emp,))
                row = self.cursor.fetchone()
                if row is None:
                    self.cursor.execute("INSERT INTO the_captured_image VALUES(%s,%s)", (emp,img))
                else:
                    sql = "UPDATE the_captured_image SET the_image = %s WHERE Employee_ID = %s"
                    self.cursor.execute(sql, (img,emp))
                self.mydb.commit()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def exit_file_manager(self, *args):
        try:
            self.file_manager.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()




    def open_file_mana(self):
        try:
            self.file_mana.show('/')  # Show the file manager starting from the root directory
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def select_pa(self, path):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global det,emp
            self.cursor = self.mydb.cursor()
            # Handle the selected image file path here
            self.file_mana.close()
            print("Selected File:", path)
            if sm.current=='admin_dashboard':
                det = sm.get_screen('admin_dashboard')
                emp = det.ids.admin.text
            if sm.current =='teaching_dashboard':
                det = sm.get_screen('teaching_dashboard')
                emp = det.ids.tea.text
            if sm.current =='non_teaching_dashboard':
                det = sm.get_screen('non_teaching_dashboard')
                emp = det.ids.non_tea.text

            det.ids.my_image.source = path
            with open(path, 'rb') as image_file:
                img = image_file.read()
                self.cursor.execute("SELECT Employee_ID FROM dp WHERE Employee_ID=%s", (emp,))
                row = self.cursor.fetchone()
                if row is None:
                    self.cursor.execute("INSERT INTO dp VALUES(%s,%s)", (emp, img))
                else:
                    sql = "UPDATE dp SET pic = %s WHERE Employee_ID = %s"
                    self.cursor.execute(sql, (img, emp))
                self.mydb.commit()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()
    def exit_file_mana(self, *args):
        try:
            self.file_mana.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def open_file_manae(self):
        try:
            self.file_manae.show('/')  # Show the file manager starting from the root directory
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def select_pae(self, path):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global det,emp
            self.cursor = self.mydb.cursor()
            # Handle the selected image file path here
            self.file_manae.close()
            print("Selected File:", path)
            if sm.current=='admin_dashboard':
                det = sm.get_screen('admin_dashboard')
                emp = det.ids.admin.text
            if sm.current =='teaching_dashboard':
                det = sm.get_screen('teaching_dashboard')
                emp = det.ids.tea.text
            if sm.current =='non_teaching_dashboard':
                det = sm.get_screen('non_teaching_dashboard')
                emp = det.ids.non_tea.text

            det.ids.my_image.source = path
            with open(path, 'rb') as image_file:
                img = image_file.read()
                self.cursor.execute("SELECT Employee_ID FROM the_captured_image WHERE Employee_ID=%s", (emp,))
                row = self.cursor.fetchone()
                if row is None:
                    self.cursor.execute("INSERT INTO the_captured_image VALUES(%s,%s)", (emp, img))
                else:
                    sql = "UPDATE the_captured_image SET the_image = %s WHERE Employee_ID = %s"
                    self.cursor.execute(sql, (img, emp))
                self.mydb.commit()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()
    def exit_file_manae(self, *args):
        try:
            self.file_manae.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()




    def show_dp(self):
        print("running")
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global det,emp,t
            self.cursor = self.mydb.cursor()
            # Handle the selected image file path here


            if sm.current =='admin_dashboard':
                det = sm.get_screen('admin_dashboard')
                emp = det.ids.admin.text
                t = "admin_records"

                self.cursor.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (emp,))
                ray = self.cursor.fetchone()
                det.ids.name.text = str(ray[1])
                det.ids.empid.text = str(ray[0])
                det.ids.email.text = str(ray[2])
                det.ids.phone.text = str(ray[3])
                det.ids.jdate.text = str(ray[5])
                self.cursor.execute("SELECT pic FROM dp WHERE Employee_ID = %s", (emp,))
                row = self.cursor.fetchone()
                if row is None:
                    pass

                else:
                    image_data = row[0]
                    image = Image.open(BytesIO(image_data))
                    image.save("temp_image.jpg")
                    det.ids.my_image.source = 'temp_image.jpg'

            if sm.current =='teaching_dashboard':
                det = sm.get_screen('teaching_dashboard')
                emp = det.ids.tea.text
                t = "teaching_records"

                self.cursor.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (emp,))
                ray = self.cursor.fetchone()
                det.ids.name.text=str(ray[1])
                det.ids.empid.text=str(ray[0])
                det.ids.email.text=str(ray[2])
                det.ids.phone.text=str(ray[3])
                det.ids.jdate.text=str(ray[5])
                det.ids.dept.text=str(ray[9])
                det.ids.desig.text=str(ray[8])
                self.cursor.execute("SELECT pic FROM dp WHERE Employee_ID = %s", (emp,))
                row = self.cursor.fetchone()
                if row is None:
                    pass

                else:
                    image_data = row[0]
                    image = Image.open(BytesIO(image_data))
                    image.save("temp_image.jpg")
                    det.ids.my_image.source = 'temp_image.jpg'

            if sm.current =='non_teaching_dashboard':
                det = sm.get_screen('non_teaching_dashboard')
                emp = det.ids.non_tea.text
                t = "non_teaching_records"
                self.cursor.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (emp,))
                ray = self.cursor.fetchone()
                det.ids.name.text=str(ray[1])
                det.ids.empid.text=str(ray[0])
                det.ids.email.text=str(ray[2])
                det.ids.phone.text=str(ray[3])
                det.ids.jdate.text=str(ray[5])
                det.ids.dept.text=str(ray[9])
                det.ids.desig.text=str(ray[8])


                self.cursor.execute("SELECT pic FROM dp WHERE Employee_ID = %s",(emp,))
                row = self.cursor.fetchone()
                if row is None:
                    pass

                else:
                    image_data = row[0]
                    image = Image.open(BytesIO(image_data))
                    image.save("temp_image.jpg")
                    det.ids.my_image.source = 'temp_image.jpg'
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()




    def show_document(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            dete = sm.get_screen('emp_leave_details')
            emp = dete.ids.empid.text
            # create a cursor
            c = mydb.cursor()
            c.execute("SELECT the_image FROM the_captured_image WHERE Employee_ID = %s",(emp,))
            row = c.fetchone()
            if row is None:
                dialog = MDDialog(
                    title='Notice',
                    text="No attached document"
                )
                dialog.open()

            else:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))
                image.save("temp_image_doc.jpg")
                sm.current = 'show_doc'
                det = sm.get_screen('show_doc')
                det.ids.my_image.source = 'temp_image_doc.jpg'


        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def show_edit_document(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global u, empid

            det = sm.get_screen('login')
            t = det.ids.login_as.text
            if t == "Teaching Employee":
                u = sm.get_screen('teaching_dashboard')
                empid = u.ids.tea.text

            if t == "Non-Teaching Employee":
                u = sm.get_screen('non_teaching_dashboard')
                empid = u.ids.non_tea.text
            # create a cursor
            c = mydb.cursor()
            c.execute("SELECT the_image FROM the_captured_image WHERE Employee_ID = %s",(empid,))
            row = c.fetchone()
            if row is None:
                dialog = MDDialog(
                    title='Notice',
                    text="No attached document"
                )
                dialog.open()

            else:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))
                image.save("temp_image_edit_doc.jpg")
                sm.current = 'edit_show_doc'
                det = sm.get_screen('edit_show_doc')
                det.ids.my_image.source = 'temp_image_edit_doc.jpg'
                image_data = None

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()







    #function for employee list
    def notice_list(self,):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global u,empid
            c = mydb.cursor()
            det = sm.get_screen('login')
            t = det.ids.login_as.text
            if t == "Teaching Employee":
                u = sm.get_screen('teaching_dashboard')
                empid=u.ids.tea.text

            if t == "Non-Teaching Employee":
                u = sm.get_screen('non_teaching_dashboard')
                empid=u.ids.non_tea.text




            # Retrieve the employee data
            c.execute("SELECT Employee_ID, Name, eventtime FROM leave_history WHERE Employee_ID = %s ORDER BY eventtime DESC", (empid,))

            rows = c.fetchall()

            sm.current='noticelist'
            # Create the employee list
            employee_list = self.root.get_screen('noticelist').ids.container
            employee_list.clear_widgets()  # Clear existing widgets before populating the list

            for row in rows:
                item = ThreeLineListItem(text=row[1],secondary_text=str(empid),tertiary_text=str(row[2]))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.notice_details)
                # Add the TwoLineListItem to the employee list
                employee_list.add_widget(item)




                """vhvjh
    
                    # Retrieve the employee data
                    c.execute("SELECT Name, Employee_ID FROM secondary_table")
                    rows = c.fetchall()
    
                    # Create the employee list
                    employee_list = self.root.get_screen('emp_list').ids.container
                    employee_list.clear_widgets()  # Clear existing widgets before populating the list
                    for row in rows:
                        # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                        item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
                        # Bind the on_release event to the show_employee_details function
                        item.bind(on_release=self.show_employee_details)
                        # Add the TwoLineListItem to the employee list
                        employee_list.add_widget(item)
                    jkbk,b"""
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()











    #function to show employee list on click
    def notice_details(self,item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )


            c = mydb.cursor()
            # Retrieve the employee details

            c.execute("SELECT * FROM leave_history WHERE Employee_ID=%s AND eventtime = %s",(item.secondary_text,item.tertiary_text,))
            row = c.fetchone()
            print(row)


            sm.current = 'leave_con_report'

            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('leave_con_report')
            if employee_details_screen:

                employee_details_screen.ids.sen.text = str(row[8])
                employee_details_screen.ids.empid.text = str(row[0])
                employee_details_screen.ids.name.text = str(row[1])
                employee_details_screen.ids.ltype.text = str(row[2])
                employee_details_screen.ids.emp_type.text = str(row[3])
                employee_details_screen.ids.fdate.text = str(row[4])
                employee_details_screen.ids.tdate.text = str(row[5])
                employee_details_screen.ids.reason.text = str(row[6])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    #function for employee list
    def history_list(self,):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global u,empid
            c = mydb.cursor()
            det = sm.get_screen('login')
            t = det.ids.login_as.text
            if t == "Teaching Employee":
                u = sm.get_screen('teaching_dashboard')
                empid=u.ids.tea.text

            if t == "Non-Teaching Employee":
                u = sm.get_screen('non_teaching_dashboard')
                empid=u.ids.non_tea.text




            # Retrieve the employee data
            c.execute("SELECT Employee_ID,Name,eventtime FROM leave_history WHERE Employee_ID = %s",(empid,))
            print("li",empid)
            row = c.fetchone()
            if row is None:
                dialog = MDDialog(
                    title='Notice',
                    text="You don't have any leaves"
                )
                dialog.open()
            else:
                sm.current='leave_history_list'

                # Create the employee list
                employee_list = self.root.get_screen('leave_history_list').ids.container
                employee_list.clear_widgets()  # Clear existing widgets before populating the list
                item = ThreeLineListItem(text=row[1],secondary_text=str(empid),tertiary_text=str(row[2]))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.history_details)
                # Add the TwoLineListItem to the employee list
                employee_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()


    #function to show employee list on click
    def history_details(self,item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )


            global u, empid,row,term,ta
            det = sm.get_screen('login')
            t = det.ids.login_as.text
            if t == "Teaching Employee":
                u = sm.get_screen('teaching_dashboard')
                ta = "teaching_leave_record"
                empid = u.ids.tea.text

            if t == "Non-Teaching Employee":
                u = sm.get_screen('non_teaching_dashboard')
                ta = "non_teaching_leave_record"
                empid = u.ids.tea.text
            c = mydb.cursor()
            # Retrieve the employee details
            c.execute("SELECT sentence FROM notice WHERE Employee_ID=%s ", (item.secondary_text,))
            rat = c.fetchone()
            if rat[0]=="Accepted":
                term = "Your leave is sanctioned"
            else:
                term = "Your leave is rejected"

            c.execute("SELECT * FROM leave_history WHERE Employee_ID=%s AND eventtime = %s",(item.secondary_text,item.tertiary_text,))
            row = c.fetchone()
            print(row)
            print(empid)
            print(item.secondary_text)


            sm.current = 'leave_con_report'

            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('leave_con_report')
            if employee_details_screen:

                employee_details_screen.ids.sen.text = term
                employee_details_screen.ids.empid.text = str(row[0])
                employee_details_screen.ids.name.text = str(row[1])
                employee_details_screen.ids.ltype.text = str(row[2])
                employee_details_screen.ids.emp_type.text = str(row[3])
                employee_details_screen.ids.fdate.text = str(row[4])
                employee_details_screen.ids.tdate.text = str(row[5])
                employee_details_screen.ids.reason.text = str(row[6])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()










    def selected(self, filename):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            det = sm.get_screen('Leave_Request_Form')
            emp = det.ids.empid.text
            print(emp)
            # create a cursor
            c = mydb.cursor()
            image_path = filename[0]
            try:
                with open(image_path, "rb") as image_file:
                    image_blob = image_file.read()
                    c.execute("SELECT * FROM the_captured_image WHERE Employee_ID = %s ",(emp,))
                    row = c.fetchone()
                    if row is None:
                        c.execute("INSERT INTO the_captured_image VALUES(%s,%s) ", (emp,image_blob,))
                    else:
                        c.execute("UPDATE the_captured_image SET the_image= %s WHERE Employee_ID = 123", (image_blob,))
                    mydb.commit()

            except FileNotFoundError:
                print("Image not found!")
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def show_apply_request(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()
            det = sm.get_screen('login')
            global s, empid, t
            e = det.ids.login_as.text

            if e == "Teaching Employee":
                details = sm.get_screen('teaching_dashboard')
                empid = details.ids.tea.text
                t = 'teaching_records'
            elif e == "Non-Teaching Employee":
                details = sm.get_screen('non_teaching_dashboard')
                empid = details.ids.non_tea.text
                t = 'non_teaching_records'

            c.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (empid,))
            row = c.fetchone()


            sm.current='Leave_Request_Form'
            det = sm.get_screen('Leave_Request_Form')
            print(row)

            det.ids.emp_type.text=str(row[6])
            det.ids.name.text=str(row[1])
            det.ids.empid.text=str(row[0])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()





    def show_edit_request(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()
            det = sm.get_screen('login')
            global s, empid, t
            e = det.ids.login_as.text

            if e == "Teaching Employee":
                details = sm.get_screen('teaching_dashboard')
                empid = details.ids.tea.text
                t = 'teaching_leave_record'
            elif e == "Non-Teaching Employee":
                details = sm.get_screen('non_teaching_dashboard')
                empid = details.ids.non_tea.text
                t = 'non_teaching_leave_record'

            c.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t), (empid,))
            row = c.fetchone()
            if row is None:
                dialog = MDDialog(
                    title='Notice',
                    text="Yoy didn't applied for any leave")
                dialog.open()


            else:
                sm.current='Leave_Request_edit'
                det = sm.get_screen('Leave_Request_edit')

                print(row)
                det.ids.leave_types.text=str(row[2])
                det.ids.emp_type.text=str(row[3])
                det.ids.name.text=str(row[1])
                det.ids.empid.text=str(row[0])
                print(row[4])
                print(row[5])
                sdate=str(row[4])
                edate=str(row[5])

                date_obj = datetime.strptime(sdate, '%Y-%m-%d')
                # Convert the datetime object back to a string in the year-month-day format
                sdate = date_obj.strftime('%d-%m-%Y')

                date_obj2 = datetime.strptime(edate, '%Y-%m-%d')
                # Convert the datetime object back to a string in the year-month-day format
                edate = date_obj2.strftime('%d-%m-%Y')
                print(sdate,edate)



                det.ids.fdate.text=sdate
                det.ids.tdate.text=edate
                det.ids.reason.text=str(row[6])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()


    def leave_req_update(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()

        try:

            det = sm.get_screen('Leave_Request_edit')
            lt = det.ids.leave_types.text
            et =  det.ids.emp_type.text
            na = det.ids.name.text
            ei = det.ids.empid.text
            fd = det.ids.fdate.text
            td = det.ids.tdate.text

            date_obj = datetime.strptime(fd, '%d-%m-%Y')
            # Convert the datetime object back to a string in the year-month-day format
            fd = date_obj.strftime('%Y-%m-%d')

            date_obj = datetime.strptime(td, '%d-%m-%Y')
            # Convert the datetime object back to a string in the year-month-day format
            td = date_obj.strftime('%Y-%m-%d')



            r = det.ids.reason.text
            print(lt,et,na,ei,fd,td,r)
            if et == "Teaching Employee":
                c.execute("UPDATE teaching_leave_record SET Leave_type = %s,From_Date = %s,To_Date = %s,reason = %s WHERE Employee_ID = %s",(lt,fd,td,r,ei))
                mydb.commit()
                mydb.close()

            else:
                c.execute("UPDATE non_teaching_leave_record SET Leave_type = %s,From_Date = %s,To_Date = %s,reason = %s WHERE Employee_ID = %s",(lt,fd,td,r,ei))
                mydb.commit()
                mydb.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()



    def dialog1(self):
        try:
            dialog = MDDialog(
                  title='Notice',
                  text='You Can login after the admin accepts your request')
            dialog.open()
        except Exception as e:

            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()



    def show_update_profile(self,):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()
            det = sm.get_screen('login')
            global s,empid,t
            e = det.ids.login_as.text

            if e == "Admin":
                details = sm.get_screen('admin_dashboard')
                empid = details.ids.admin.text
                t = 'admin_records'
            elif e == "Teaching Employee":
                details = sm.get_screen('teaching_dashboard')
                empid = details.ids.tea.text
                t ='teaching_records'
            elif e == "Non-Teaching Employee":
                details = sm.get_screen('non_teaching_dashboard')
                empid = details.ids.non_tea.text
                t = 'non_teaching_records'

            c.execute("SELECT * FROM {} WHERE Employee_ID = %s".format(t),(empid,))
            row = c.fetchone()
            sm.current = 'update'
            details_screen = sm.get_screen('update')
            if details_screen:
                details_screen.ids.empid.text = str(row[0])
                details_screen.ids.empid.disabled = True
                details_screen.ids.full_name.text = str(row[1])
                details_screen.ids.email_id.text = str(row[2])
                details_screen.ids.phone_no.text =str(row[3])
                details_screen.ids.password.text =str(row[4])
                details_screen.ids.jdate.text =str(row[5])
                details_screen.ids.jdate.disabled = True
                details_screen.ids.desig.text = str(row[9])
                details_screen.ids.dept.text = str(row[8])
                details_screen.ids.gender.text = str(row[7])
                details_screen.ids.etype.text = str(row[6])


            mydb.commit()
            mydb.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def update1(self,):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )

            c = mydb.cursor()
            details_screen = sm.get_screen('update')
            empid1 = details_screen.ids.empid.text
            full_name1 = details_screen.ids.full_name.text
            email_id1 = details_screen.ids.email_id.text
            phone_no1 = details_screen.ids.phone_no.text
            password1 = details_screen.ids.password.text
            jdate1 = details_screen.ids.jdate.text
            dept1 = details_screen.ids.dept.text
            desig1 = details_screen.ids.desig.text
            spinner_id11 = details_screen.ids.etype.text
            spinner_id21 = details_screen.ids.gender.text


            if spinner_id11 == "Admin":
                c.execute("UPDATE admin_records SET Name=%s,email_ID=%s,Phone_Number=%s,password=%s,Joining_Date=%s,Post=%s,Gender=%s,Department=%s,Designation=%s WHERE Employee_ID=%s",(full_name1,email_id1,phone_no1,password1,jdate1,spinner_id11,spinner_id21,dept1,desig1,empid1,))
                sm.current = 'login'
            elif spinner_id11 == "Teaching Employee":
                c.execute("UPDATE teaching_records SET Name=%s,email_ID=%s,Phone_Number=%s,password=%s,Joining_Date=%s,Post=%s,Gender=%s,Department=%s,Designation=%s WHERE Employee_ID=%s",(full_name1,email_id1,phone_no1,password1,jdate1,spinner_id11,spinner_id21,dept1,desig1,empid1,))
                sm.current = 'login'
            elif spinner_id11 == "Non-Teaching Employee":
                c.execute("UPDATE non_teaching_records SET Name=%s,email_ID=%s,Phone_Number=%s,password=%s,Joining_Date=%s,Post=%s,Gender=%s,Department=%s,Designation=%s WHERE Employee_ID=%s",(full_name1,email_id1,phone_no1,password1,jdate1,spinner_id11,spinner_id21,dept1,desig1,empid1,))
                sm.current = 'login'
            mydb.commit()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()




    def send_message_verification(self,email_id,sts):

        try:
            # Get the email details from the text fields
            email = "jr1954674@gmail.com"
            password = "yzofpmcpumpyddmg"
            recipient = email_id
            subject ="Your Leave Status"
            message = sts
            # Connect to the email server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.ehlo()
            server.login(email, password)
            # Compose the email
            email_message = f"Subject: {subject}\n\n{message}"
            # Send the email
            server.sendmail(email, recipient, email_message)
            server.quit()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()












    def acreq(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        #ltype,name,fdate,tdate,reason,empid
        try:
            c = mydb.cursor()
            det = sm.get_screen('emp_leave_details')
            lt = det.ids.ltype.text
            emp=det.ids.empid.text
            nam=det.ids.name.text
            f=det.ids.fdate.text
            t=det.ids.tdate.text
            id=det.ids.empid.text
            r=det.ids.reason.text
            empt=det.ids.emp_type.text
            current_date = datetime.now()
            formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            nf =f
            nt =t
            from_date_object = datetime.strptime(nf, "%Y-%m-%d")
            to_date_object = datetime.strptime(nt, "%Y-%m-%d")
            global l, n,email_id,sts
            if empt == "Teaching Employee":
                l = "teaching_leave_record"
                lr = "teaching_records"
            elif empt == "Non-Teaching Employee":
                l = "non_teaching_leave_record"
                lr = "non_teaching_records"
            else:
                dialog = MDDialog(
                    title='Warning',
                    text=f"Select Employee type"
                )
                dialog.open()
            c.execute("SELECT email_ID FROM {} WHERE Employee_ID = %s".format(lr),(emp,))
            raw = c.fetchone()
            email_id = str(raw[0])
            sts = f"Your leave for {lt} from {f} to {t} is santioned"
            if lt == "Casual Leave":
                c.execute("SELECT Casual_Leave FROM leave_balance WHERE Employee_ID=%s", (emp,))
                row = c.fetchone()
                nv = row[0] - (to_date_object - from_date_object).days
                c.execute("UPDATE leave_balance SET Casual_Leave = %s WHERE Employee_ID=%s", (nv, emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                self.send_message_verification(email_id, sts)
                mydb.commit()
                mydb.close()
            elif lt == "Earned Leave":
                c.execute("SELECT Earned_Leave FROM leave_balance WHERE Employee_ID=%s", (emp,))
                row = c.fetchone()
                nv = row[0] - (to_date_object - from_date_object).days
                c.execute("UPDATE leave_balance SET Earned_Leave = %s WHERE Employee_ID=%s", (nv, emp,))
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                self.send_message_verification(email_id, sts)
                mydb.commit()
                mydb.close()
            elif lt == "Child Care Leave":
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date,"Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                c.execute("DELETE FROM the_captured_image WHERE Employee_ID=%s", (emp,))
                self.send_message_verification(email_id, sts)
                mydb.commit()
                mydb.close()
            elif lt == "Maternity Leave":
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                self.send_message_verification(email_id, sts)
                mydb.commit()
                mydb.close()
            elif lt == "Duty Leave":
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                self.send_message_verification(email_id,sts)
                mydb.commit()
                mydb.close()
            elif lt == "Special Leave":
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                self.send_message_verification(email_id, sts)
                mydb.commit()
                mydb.close()
            elif lt == "Medical Leave":
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                c.execute("DELETE FROM the_captured_image WHERE Employee_ID=%s",(emp,))
                self.send_message_verification(email_id, sts)
                print("did")
                mydb.commit()
                mydb.close()
            elif lt == "Others":
                query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
                c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Sanctioned"))
                c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
                self.send_message_verification(email_id, "Contact College authority regarding your leave")
                mydb.commit()
                mydb.close()
            self.on_click_teaching_leave_list()
            self.on_click_non_teaching_leave_list()
            sm.current = 'leave_list'

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()















    def rejreq(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )

            # create a cursor
            # ltype,name,fdate,tdate,reason,empid
            c = mydb.cursor()
            det = sm.get_screen('emp_leave_details')
            lt = det.ids.ltype.text
            emp = det.ids.empid.text
            nam = det.ids.name.text
            f = det.ids.fdate.text
            t = det.ids.tdate.text
            id = det.ids.empid.text
            r = det.ids.reason.text

            empt = det.ids.emp_type.text

            current_date = datetime.now()
            formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

            nf = f
            nt = t

            from_date_object = datetime.strptime(nf, "%Y-%m-%d")
            to_date_object = datetime.strptime(nt, "%Y-%m-%d")

            global l, n, email_id, sts,lr
            if empt == "Teaching Employee":
                l = "teaching_leave_record"
                lr = "teaching_records"

            elif empt == "Non-Teaching Employee":
                l = "non_teaching_leave_record"
                lr ="non_teaching_records"

            else:
                dialog = MDDialog(
                    title='Warning',
                    text=f"Select Employee type"
                )
                dialog.open()

            c.execute("SELECT email_ID FROM {} WHERE Employee_ID = %s".format(lr), (emp,))
            raw = c.fetchone()
            email_id = str(raw[0])
            sts = f"Your leave for {lt} from {f} to {t} is Rejected"

            query = "INSERT INTO leave_history VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s)"
            c.execute(query, (id, nam, lt, empt, f, t, r, formatted_date, "Rejected"))
            c.execute("DELETE FROM {} WHERE Employee_ID=%s".format(l), (emp,))
            c.execute("SELECT * FROM the_captured_image WHERE Employee_ID=%s", (emp,))
            row = c.fetchone()
            if row is not None:
                c.execute("DELETE FROM the_captured_image WHERE Employee_ID=%s", (emp,))
            mydb.commit()
            mydb.close()
            self.send_message_verification(email_id,sts)
            self.on_click_teaching_leave_list()
            self.on_click_non_teaching_leave_list()
            sm.current = 'leave_list'

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()









    def save_report(self,):
        layout = BoxLayout(orientation='vertical')

        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Set canvas color
            self.rect = Rectangle(size=Window.size, pos=layout.pos)
        layout.bind(size=lambda *args: setattr(self.rect, 'size', args[1]))

        layout = self.root  # Assuming self.root is the root container for the layout hierarchy

        # Capture the layout as an image
        try:
            Window.screenshot(name='rep9.png')
            print("Screenshot saved successfully as 'rep9.png'.")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

    def shownotice(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()
            details_screen = sm.get_screen('teaching_dashboard')
            empid = details_screen.ids.tea.text
            c.execute(f"select Sentence from notice where Employee_ID = %s",(empid,))
            row = c.fetchone()
            sm.current = 'notice'
            details_screen2 = sm.get_screen('notice')
            details_screen2.ids.noti.text=row[0]
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry an unknown error occured"
            )
            dialog.open()

    def check_login(self,email_phn,login_as,password):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        pas = password

        print(email_phn)
        email_phn=str(email_phn)


        dialog = MDDialog(
            title='Invalid',
            text='Wrong Login Details'
        )
        # create a cursor
        c = mydb.cursor()
        try:
            if login_as =="Admin":
                c.execute("SELECT * FROM admin_records WHERE email_ID = %s OR Phone_Number = %s",(email_phn,email_phn,))
                row = c.fetchone()
                print(row)
                if row[4] == pas:
                    MDApp.get_running_app().root.current = 'admin_dashboard'
                    sm.current = 'admin_dashboard'
                    details_screen = sm.get_screen('admin_dashboard')
                    if details_screen:
                        details_screen.ids.admin.title = str(row[1])
                        details_screen.ids.admin.text = str(row[0])
                        self.show_dp()
                else:
                    dialog.open()

            if login_as =="Teaching Employee":
                c.execute("SELECT * FROM teaching_records WHERE email_ID = %s OR Phone_Number = %s",(email_phn,email_phn,))
                row = c.fetchone()
                print(row)
                if row[4] == pas:
                    MDApp.get_running_app().root.current = 'teaching_dashboard'
                    sm.current = 'teaching_dashboard'
                    details_screen = sm.get_screen('teaching_dashboard')
                    if details_screen:
                        details_screen.ids.tea.title = str(row[1])
                        details_screen.ids.tea.text = str(row[0])
                        self.show_dp()
                else:
                    dialog.open()



            if login_as =="Non-Teaching Employee":
                c.execute("SELECT * FROM non_teaching_records WHERE email_ID = %s OR Phone_Number = %s",(email_phn,email_phn,))
                row = c.fetchone()
                if row[4] == pas:
                    MDApp.get_running_app().root.current = 'non_teaching_dashboard'
                    sm.current = 'non_teaching_dashboard'
                    details_screen = sm.get_screen('non_teaching_dashboard')
                    if details_screen:
                        details_screen.ids.non_tea.title = str(row[1])
                        details_screen.ids.non_tea.text = str(row[0])
                        self.show_dp()
                else:
                    dialog.open()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Invalid login details "
            )
            dialog.open()
















    def signup(self,full_name,email_id,phone_no,password,jdate,spinner_id1,spinner_id2,spinner_id3,spinner_id4):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        global rand_num,formatted_date
        formatted_date = jdate.text
        print(formatted_date)

        # Convert the formatted_date string to a datetime object
        date_obj = datetime.strptime(formatted_date, '%d-%m-%Y')

        # Convert the datetime object back to a string in the MySQL date format
        mysql_date = date_obj.strftime('%Y-%m-%d')
        print(mysql_date)

        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            # create a cursor
            c = mydb.cursor()
            if (re.fullmatch(regex, email_id.text)):
                #insert_record
                #secondary table
                if spinner_id1.text=="Admin":
                    rand_n = random.randint(1, 100000)
                    rand_num = 'E' + str(rand_n) + 'A'

                elif spinner_id1.text=="Teaching Employee":
                    rand_n = random.randint(1, 100000)
                    rand_num = 'E' + str(rand_n) + 'T'
                elif spinner_id1.text=="Non-Teaching Employee":
                    rand_n = random.randint(1, 100000)
                    rand_num = 'E' + str(rand_n) + 'NT'
                else:
                    dialog = MDDialog(
                        title='Notice',
                        text="Select Employee Type "
                    )
                    dialog.open()


                c.execute(f"insert into secondary_table values('{rand_num}','{full_name.text}','{email_id.text}','{phone_no.text}','{password.text}','{mysql_date}','{spinner_id1.text}','{spinner_id2.text}','{spinner_id3.text}','{spinner_id4.text}')")
                dialog = MDDialog(
                    title='Notice',
                    text="You can login after the admin accepts "
                )
                dialog.open()

            else:
                dialog = MDDialog(
                    title='Notice',
                    text="Invalid Email "
                )
                dialog.open()

            mydb.commit()
            mydb.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text="Fill the form correctly "
            )
            dialog.open()


    #function for employee list
    def on_click_show_list(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            # Retrieve the employee data
            c.execute("SELECT Name, Employee_ID FROM secondary_table")
            rows = c.fetchall()

            # Create the employee list
            employee_list = self.root.get_screen('emp_list').ids.container
            employee_list.clear_widgets()  # Clear existing widgets before populating the list
            for row in rows:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.show_employee_details)
                # Add the TwoLineListItem to the employee list
                employee_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()

    #function to show employee list on click
    def show_employee_details(self, item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            # Retrieve the employee details
            c.execute("SELECT * FROM secondary_table WHERE Employee_ID=%s", (item.secondary_text,))
            row = c.fetchone()
            sm.current = 'emp_detail'

            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('emp_detail')
            if employee_details_screen:

                employee_details_screen.ids.empid.text = str(row[0])
                employee_details_screen.ids.name.text = str(row[1])
                employee_details_screen.ids.email.text = str(row[2])
                employee_details_screen.ids.phone.text = str(row[3])
                employee_details_screen.ids.gender.text = str(row[7])
                employee_details_screen.ids.emp_type.text = str(row[6])
                employee_details_screen.ids.dept.text = str(row[8])
                employee_details_screen.ids.desig.text = str(row[9])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()

    ##function for employee list
    def on_click_show_list_of_all_employees(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            # Retrieve the employee data
            c.execute("SELECT Name, Employee_ID FROM teaching_records UNION SELECT Name, Employee_ID FROM non_teaching_records ORDER BY Name")
            rows = c.fetchall()

            # Create the employee list
            employee_list = self.root.get_screen('emp_list').ids.container
            employee_list.clear_widgets()  # Clear existing widgets before populating the list
            for row in rows:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = TwoLineAvatarIconListItem(text=row[0], secondary_text=str(row[1]))
                item.add_widget(IconLeftWidget(icon="account"))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.show_employee_details_of_employees)
                # Add the TwoLineListItem to the employee list
                employee_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()




    ##function to show employee list on click
    def show_employee_details_of_employees(self, item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()
            global row

            # Retrieve the employee details
            c.execute("SELECT * FROM teaching_records WHERE Employee_ID=%s", (item.secondary_text,))
            row = c.fetchone()
            if row is None:
                c.execute("SELECT * FROM non_teaching_records WHERE Employee_ID=%s", (item.secondary_text,))
                row = c.fetchone()


            sm.current = 'detail_employee'

            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('detail_employee')
            if employee_details_screen:

                employee_details_screen.ids.empid.text = str(row[0])
                employee_details_screen.ids.name.text = str(row[1])
                employee_details_screen.ids.email.text = str(row[2])
                employee_details_screen.ids.phone.text = str(row[3])
                employee_details_screen.ids.emp_type.text = str(row[6])
                employee_details_screen.ids.gender.text = str(row[7])
                employee_details_screen.ids.dept.text = str(row[8])
                employee_details_screen.ids.desig.text = str(row[9])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()




    #function to add employee(for admin section)
    def add_emp(self,empid,emp_type):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            print(emp_type)
            c = mydb.cursor()
            c.execute("SELECT * FROM secondary_table WHERE Employee_ID =%s ", (empid.text,))
            row = c.fetchone()
            if emp_type =="Teaching Employee":

                c.execute("INSERT INTO teaching_records VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],))
                c.execute("INSERT INTO leave_balance VALUES(%s,0,0,%s)", (row[0], row[5],))
                c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s",(empid.text,))
                mydb.commit()
                mydb.close()


                MDApp.get_running_app().root.current = 'emp_list'

            elif emp_type =="Admin":
                print("a")
                c.execute("INSERT INTO admin_records VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],))
                c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s",(empid.text,))
                mydb.commit()
                mydb.close()



                MDApp.get_running_app().root.current = 'emp_list'

            elif emp_type =="Non-Teaching Employee":

                c.execute("INSERT INTO non_teaching_records VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],))

                c.execute("INSERT INTO leave_balance VALUES(%s,0,0,%s)", (row[0], row[5],))
                c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s", (empid.text,))
                mydb.commit()
                mydb.close()
                MDApp.get_running_app().root.current = 'emp_list'
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()





    #function to remove employee(for admin section)
    def rem_emp(self,empid):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            c.execute("DELETE FROM secondary_table WHERE Employee_ID=%s",(empid.text,))

            MDApp.get_running_app().root.current = 'emp_list'

            mydb.commit()
            mydb.close()
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()



    #function for employee list
    def on_click_teaching_leave_list(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()


            # Retrieve the employee data
            c.execute("SELECT Name, Empployee_ID FROM teaching_leave_record")

            rows = c.fetchall()


            # Create the teaching employee leave list
            leave_list = self.root.get_screen('leave_list').ids.container
            leave_list.clear_widgets()  # Clear existing widgets before populating the list
            for row in rows:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.show_employee_details)
                # Add the TwoLineListItem to the employee list
                leave_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()

    #function for employee list
    def on_click_non_teaching_leave_list(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()


            # Retrieve the employee data
            c.execute("SELECT Name, Employee_ID FROM non_teaching_leave_record")

            rows = c.fetchall()


            # Create the teaching employee leave list
            leave_list = self.root.get_screen('leave_list').ids.container1
            leave_list.clear_widgets()  # Clear existing widgets before populating the list
            for row in rows:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = TwoLineListItem(text=row[0], secondary_text=str(row[1]))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.show_employee_details)
                # Add the TwoLineListItem to the employee list
                leave_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()

    def send_request(self, empid, name, leave_types, emp_type, fdate, tdate, reason):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        # create a cursor
        c = mydb.cursor()
        try:
            date_obj = datetime.strptime(fdate, '%d-%m-%Y')
            # Convert the datetime object back to a string in the year-month-day format
            fdate = date_obj.strftime('%Y-%m-%d')
            print(fdate)
            date_obj2 = datetime.strptime(tdate, '%d-%m-%Y')
            # Convert the datetime object back to a string in the year-month-day format
            tdate = date_obj2.strftime('%Y-%m-%d')
            print(tdate)


            from_date = fdate
            to_date = tdate
            from_date_object = datetime.strptime(from_date, "%Y-%m-%d")
            to_date_object = datetime.strptime(to_date, "%Y-%m-%d")
            global l, n

            if emp_type == "Teaching Employee":
                l = 'teaching_leave_record'
                n = 'teaching_records'
            elif emp_type == "Non-Teaching Employee":
                l = 'non_teaching_leave_record'
                n = 'non_teaching_records'
            else:
                dialog = MDDialog(
                    title='Warning',
                    text=f"Select Employee type"
                )
                dialog.open()

            if leave_types == "Casual Leave":
                c.execute("SELECT Casual_Leave FROM leave_balance WHERE Employee_ID=%s", (empid,))
                row = c.fetchone()
                if (to_date_object - from_date_object).days > row[0]:
                    dialog = MDDialog(
                        title='Warning',
                        text=f"You have {row[0]} Casual Leaves"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    self.goback()



            elif leave_types == "Earned Leave":
                c.execute("SELECT Earned_Leave FROM leave_balance WHERE Employee_ID=%s", (empid,))
                row = c.fetchone()
                if (to_date_object - from_date_object).days > row[0]:
                    dialog = MDDialog(
                        title='Warning',
                        text=f"You have {row[0]} Earned Leaves only"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    self.goback()

            elif leave_types == "Child Care Leave":
                print(n)
                c.execute("SELECT Gender FROM {} WHERE Employee_ID = %s".format(n), (empid,))
                row = c.fetchone()
                if row[0] == "Male":
                    dialog = MDDialog(
                        title='Warning',
                        text=f"Only female employees can apply for CCL"
                    )
                    dialog.open()

                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                    sm.current = 'certificate'





            elif leave_types == "Medical Leave":

                if emp_type == "Teaching Employee":
                    dialog = MDDialog(
                        title='Warning',
                        text=f"Only non-teaching employees can apply for Medical Leave"
                    )
                    dialog.open()

                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                    sm.current = 'certificate'

            elif leave_types == "Maternity Leave":
                c.execute("SELECT Gender FROM {} WHERE Employee_ID = %s".format(n), (empid,))
                row = c.fetchone()
                if row[0] == "Male":
                    dialog = MDDialog(
                        title='Warning',
                        text=f"Only female employees can apply for Maternity Leave"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                    sm.current = 'certificate'



            elif leave_types == "Duty Leave":
                query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                self.goback()

            elif leave_types == "Others":
                query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))
                dialog = MDDialog(
                    title='Notice',
                    text=f"Contact with the College"
                )
                dialog.open()

                self.goback()

            elif leave_types == "Special Leave":

                if (to_date_object - from_date_object).days > 547:
                    dialog = MDDialog(
                        title='Warning',
                        text=f"You can't take Special Leave more than 547 days or 18 months"
                    )
                    dialog.open()
                else:
                    query = "INSERT INTO {} VALUES (%s,%s, %s, %s, %s, %s, %s)".format(l)
                    c.execute(query, (empid, name, leave_types, emp_type, fdate, tdate, reason))

                    self.goback()

            mydb.commit()
            mydb.close()

        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text=f"Either you have a pending request or didn't fill the form correctly"
            )
            dialog.open()



    def callback_func(self):
        print("juj")






    def callback_for_menu_items(self,):
        print("ok")


    def no_function(self, instance):
        dialog = MDDialog(
            title='Warning',
            text=f"To apply for CCL, your child's age must be below 18 years old"
        )
        dialog.open()

    def goback(self):
        det = sm.get_screen('login')
        e = det.ids.login_as.text
        if e == "Teaching Employee":
            sm.current = 'teaching_dashboard'
        elif e == "Non-Teaching Employee":
            sm.current = 'non_teaching_dashboard'


    def goback2(self):
        det = sm.get_screen('login')
        e = det.ids.login_as.text
        if e == "Teaching Employee":
            sm.current = 'teaching_dashboard'
        elif e == "Non-Teaching Employee":
            sm.current = 'non_teaching_dashboard'
        elif e == "Admin":
            sm.current = 'admin_dashboard'




    #function for employee list
    def on_click_teaching_leave_list(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()


            # Retrieve the employee data
            c.execute("SELECT Employee_ID, Name FROM teaching_leave_record")

            rows = c.fetchall()


            # Create the teaching employee leave list
            leave_list = self.root.get_screen('leave_list').ids.container
            leave_list.clear_widgets()  # Clear existing widgets before populating the list
            for row in rows:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = TwoLineListItem(text=str(row[1]), secondary_text=str(row[0]))
                # Bind the on_release event to the show_employee_details function

                item.bind(on_release=self.show_temployee_leave_details)
                # Add the TwoLineListItem to the employee list
                leave_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()

    #function for employee list
    def on_click_non_teaching_leave_list(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()


            # Retrieve the employee data
            c.execute("SELECT Employee_ID, Name FROM non_teaching_leave_record")

            rows = c.fetchall()


            # Create the teaching employee leave list
            leave_list = self.root.get_screen('leave_list').ids.container1
            leave_list.clear_widgets()  # Clear existing widgets before populating the list
            for row in rows:
                # Create a TwoLineListItem with the employee name as text and phone number as secondary text
                item = TwoLineListItem(text=str(row[1]), secondary_text=str(row[0]))
                # Bind the on_release event to the show_employee_details function
                item.bind(on_release=self.show_nemployee_leave_details)
                # Add the TwoLineListItem to the employee list
                leave_list.add_widget(item)
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()


    def show_nemployee_leave_details(self, item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            # Retrieve the employee details
            c.execute("SELECT * FROM non_teaching_leave_record WHERE Employee_ID = %s", (item.secondary_text,))
            row = c.fetchone()

            sm.current = 'emp_leave_details'

            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('emp_leave_details')


            employee_details_screen.ids.ltype.text = str(row[2])
            employee_details_screen.ids.emp_type.text = str(row[3])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.fdate.text = str(row[4])
            employee_details_screen.ids.tdate.text = str(row[5])
            employee_details_screen.ids.reason.text = str(row[6])
            employee_details_screen.ids.empid.text = item.secondary_text
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()



    def show_temployee_leave_details(self, item):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            c = mydb.cursor()

            # Retrieve the employee details
            c.execute("SELECT * FROM teaching_leave_record WHERE Employee_ID = %s", (item.secondary_text,))
            row = c.fetchone()

            sm.current = 'emp_leave_details'


            # Update the employee details screen with the retrieved data
            employee_details_screen = sm.get_screen('emp_leave_details')


            employee_details_screen.ids.ltype.text = str(row[2])
            employee_details_screen.ids.emp_type.text = str(row[3])
            employee_details_screen.ids.name.text = str(row[1])
            employee_details_screen.ids.fdate.text = str(row[4])
            employee_details_screen.ids.tdate.text = str(row[5])
            employee_details_screen.ids.reason.text = str(row[6])
            employee_details_screen.ids.empid.text = item.secondary_text
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()

    def employee_check_balance(self,):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="test_db"
            )
            global detail,empid
            c = mydb.cursor()
            det = sm.get_screen('login')
            e = det.ids.login_as.text
            if e == "Teaching Employee":
                detail = sm.get_screen('teaching_dashboard')
                empid = detail.ids.tea.text

            elif e == "Non-Teaching Employee":
                detail = sm.get_screen('non_teaching_dashboard')
                empid = detail.ids.non_tea.text

            # Retrieve the employee details
            c.execute("SELECT Casual_Leave,Earned_Leave from leave_balance WHERE Employee_ID= %s", (empid,))
            row = c.fetchone()

            sm.current = 'check_balance'
            # Update the employee details screen with the retrieved data
            details_screen = sm.get_screen('check_balance')
            if details_screen:
                details_screen.ids.CL.text = str(row[0])
                details_screen.ids.EL.text = str(row[1])
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Notice',
                text="Sorry! An error occured "
            )
            dialog.open()


    def update(self,empid,full_name,email_id,phone_no,password,jdate,spinner_id1,spinner_id2,spinner_id3,spinner_id4):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="test_db"
        )
        c = mydb.cursor()





LeavesystemApp().run()