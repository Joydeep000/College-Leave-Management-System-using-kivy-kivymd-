from kivymd.app import MDApp
from kivy.lang.builder import Builder
import mysql.connector
from kivy.uix.screenmanager import ScreenManager


class LeavesystemApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        mydb = mysql.connector.connect(
            host="sql6.freesqldatabase.com",
            user="sql6632497",
            passwd="EESCstNkZW",
            database="sql6632497"
        )
        # create a cursor
        c = mydb.cursor()

        # create actual db

        # create a secondary table to store employee records
        c.execute("""CREATE TABLE if not exists testing(Employee_ID VARCHAR(50) PRIMARY KEY, Name VARCHAR(100),email_ID VARCHAR(100) ,Phone_Number NUMERIC(14) ,password VARCHAR(20),Joining_Date DATE,Post VARCHAR(30),Gender VARCHAR(10) ,Department VARCHAR(30),Designation VARCHAR(30))""")

        global sm
        sm = ScreenManager()
        return sm
LeavesystemApp().run()