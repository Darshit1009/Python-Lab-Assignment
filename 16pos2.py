from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TextInputApp(App):
    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Text Input
        self.text_input = TextInput(hint_text='Type something...', font_size=24, multiline=False)
        layout.add_widget(self.text_input)

        # Display Label
        self.display_label = Label(text='', font_size=32)
        layout.add_widget(self.display_label)

        # Show Button
        button = Button(text='Show Text', font_size=28, size_hint=(1, 0.4))
        button.bind(on_press=self.display_text)
        layout.add_widget(button)

        return layout

    def display_text(self, instance):
        self.display_label.text = self.text_input.text

if __name__ == '__main__':
    TextInputApp().run()
