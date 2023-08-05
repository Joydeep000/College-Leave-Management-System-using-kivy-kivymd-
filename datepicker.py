from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.size = (310,570)


class DatePickerApp(MDApp):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("leave_request.kv"))
        return sm

    def open_date_picker(self, text_input_id):



        # Create an instance of the MDDatePicker widget
        date_dialog = MDDatePicker(orientation="potrait")

        # Add the MDDatePicker widget to the BoxLayout







        # Open the Popup
        date_dialog.open()

    def on_date_save(self, text_input_id, value):
        # Get the current screen from the ScreenManager
        current_screen = sm.current_screen

        # Access the text input widget with the specified id in the current screen
        text_input = current_screen.ids[text_input_id]

        # Format the selected date in the day-month-year format
        formatted_date = value.strftime('%d-%m-%Y')

        # Set the formatted date as the text of the text input widget
        text_input.text = formatted_date




if __name__ == '__main__':
    DatePickerApp().run()
