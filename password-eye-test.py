from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        global sm
        sm = ScreenManager()

        sm.add_widget(Builder.load_file("password.kv"))
        return sm

    def toggle_password_visibility(self, password_field):
        print("helo")
        if password_field.password:
            password_field.password = False
            password_field.icon_right = "eye"

        else:
            password_field.password = True
            password_field.icon_right = "eye-off"
LoginApp().run()
