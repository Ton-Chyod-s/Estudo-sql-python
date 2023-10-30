from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder

from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout


class HotReload(MDApp):
    KV_FILES = ['app/pomodoro.kv']
    DEBUG = True

    def build_app(self):
        #self.theme_cls.theme_style = "Dark"
        return Builder.load_file('app/pomodoro.kv')

HotReload().run()