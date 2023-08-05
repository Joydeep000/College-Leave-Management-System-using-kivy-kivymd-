from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
Window.size = (310,570)
class ProfileCard(MDFloatLayout,FakeRectangularElevationBehavior):
    pass

class MyApp(MDApp):
    def build(self):
        global sm
        sm = MDScreenManager()
        sm.add_widget(Builder.load_file("new_admin_dashboard.kv"))
        return sm
if __name__ == "__main__":
    MyApp().run()
