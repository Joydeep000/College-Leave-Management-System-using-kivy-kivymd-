from kivymd.app import MDApp
from kivymd.uix.slider import MDSlider
from kivy.uix.boxlayout import BoxLayout


class SliderApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Creating a horizontal slider
        slider_h = MDSlider(min=0, max=100, value=50)
        slider_h.bind(on_touch_up=self.on_slider_release)
        layout.add_widget(slider_h)
        return layout

    def on_slider_release(self, slider, touch):
        print(f"Slider value: {slider.value}")


SliderApp().run()
