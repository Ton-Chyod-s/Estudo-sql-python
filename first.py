from kivymd.app import MDApp
from kivy.lang import Builder


KV = """

FloatLayout:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        


    MDRaisedButton:
       
    
    
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

MainApp().run()