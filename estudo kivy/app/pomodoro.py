from kivymd.app import MDApp
from kivy.lang import Builder

class PomoDuno(MDApp):
    def build(self):
        return Builder.load_file('app/pomodoro.kv')