from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from PIL import Image as PILImage


class ImageFilterApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        # Load the original image
        original_image = PILImage.open("image.jpg")

        # Create Kivy image widget and set the original image as source
        kivy_image = Image(source="image.jpg")
        layout.add_widget(kivy_image)

        # Create sliders for adjusting filter intensity
        slider_layout = BoxLayout(orientation="vertical", size_hint=(1, 0.1))
        layout.add_widget(slider_layout)

        # Create a slider for intensity adjustment
        intensity_slider = Slider(min=0, max=1, value=1, step=0.01)
        intensity_slider.bind(value=lambda x, value: self.apply_filter(kivy_image, original_image, value))
        slider_layout.add_widget(intensity_slider)

        return layout

    def apply_filter(self, kivy_image, original_image, intensity):
        # Apply the black and white filter with the adjusted intensity
        filtered_image = original_image.convert("L")
        filtered_image = filtered_image.point(lambda x: x * intensity)

        # Save the filtered image
        filtered_image.save("filtered_image.jpg")

        # Set the filtered image as the source of the Kivy image widget
        kivy_image.source = "filtered_image.jpg"
if __name__ == "__main__":
    ImageFilterApp().run()
