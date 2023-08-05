from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog


class TestApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        button = MDRaisedButton(text='Click Me!')
        button.bind(on_release=self.change_text)

        layout.add_widget(button)
        return layout

    def change_text(self, instance):
        try:
            if instance.text == 'Click Me!':
                instance.text = 'Clicked!'
            else:
                instance.text = 'Click Me!'
        except Exception as e:
            print(e)
            dialog = MDDialog(
                title='Warning',
                text="Enter the data correctly"
            )
            dialog.open()


if __name__ == '__main__':
    TestApp().run()
