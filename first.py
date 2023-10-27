from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.lang import Builder


KV = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Myapp'
            left_action_items:[['menu', lambda x: x]]
            right_action_items:[['dots-vertical', lambda x: x]]
        FormLogin:

        
<senhacard>:
    
<FormLogin@FloatLayout>:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'language-python'
        icon_size: '75sp'

    MDTextField:
        size_hint_x: .5
        hint_text:'E-mail'
        pos_hint: {'center_x': .5, 'center_y': .6}
    
    MDTextField:
        size_hint_x: .5
        hint_text:'Senha'
        pos_hint: {'center_x': .5, 'center_y': .5}

    MDRaisedButton:
        size_hint_x: .5
        pos_hint: {'center_x': .5, 'center_y': .4}
        text:'Login'

    MDLabel:
        text: 'Esqueceu sua senha?'
        halign: 'center'
        pos_hint: {'center_y': .3}

    MDTextButton:
        text: 'Clique aqui!'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_release: app.abrir_card()
"""
class SenhaCard(MDCard):
    ...


class MainApp(MDApp):
    def abrir_card(self):
        print('abrindo o card')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

MainApp().run()