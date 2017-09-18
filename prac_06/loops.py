from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class NameWidgetApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Mardy", "Molly", "Penny", "Akela", "Bunny", "Turtle"]

    def build(self):
        self.title = "Names"
        self.root = Builder.load_file("loops.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.nameBox.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = name

    def clear_all(self):
        self.root.ids.nameBox.clear_widgets()

NameWidgetApp().run()
