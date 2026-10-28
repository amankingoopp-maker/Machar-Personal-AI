
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.06, 0.07, 0.10, 1)

class MacharAI(App):
    def build(self):
        self.root = BoxLayout(
            orientation="vertical",
            padding=12,
            spacing=10
        )

        self.root.add_widget(Label(
            text="[b]Machar Personal AI[/b]\nOffline AI Assistant",
            markup=True,
            font_size="24sp",
            size_hint_y=None,
            height=75
        ))

        self.chat = Label(
            text="Namaste! Main Machar AI hoon.\nAap kya poochna chahte hain?",
            halign="left",
            valign="top",
            size_hint_y=1
        )
        self.chat.bind(size=self.update_text_size)
        self.root.add_widget(self.chat)

        self.input = TextInput(
            hint_text="Yahan message likhein...",
            multiline=False,
            size_hint_y=None,
            height=52
        )
        self.root.add_widget(self.input)

        self.root.add_widget(Button(
            text="Send",
            size_hint_y=None,
            height=48,
            on_press=self.send_message
        ))

        return self.root

    def update_text_size(self, instance, size):
        instance.text_size = (size[0], None)

    def send_message(self, instance):
        message = self.input.text.strip()
        if not message:
            return

        self.chat.text += f"\n\nAap: {message}\nMachar AI: Abhi AI model connect karna baaki hai."
        self.input.text = ""

MacharAI().run()
