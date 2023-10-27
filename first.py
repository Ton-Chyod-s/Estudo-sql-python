import kivy
from kivy.app import App


layout = """Button:
    text: 'Hello from test.kv'"""


class TestApp(App):
    def build(self):
        return layout

if __name__ == '__main__':
    TestApp().run()