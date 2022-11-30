from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
import db_categoria


Window.size = (470,750)

class home(Screen):
    ...

class SuccesCard():
    def __init__(self,message='',**kwargs):
       super().__init__(**kwargs)
       self.ids.message.text = message

class Interface(ScreenManager):
    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela
    def add_categoria(self, nome, valor):
        db_categoria.gera_categoria(nome, valor)

        # self.ids.results_box.add_widget(ResultadosCard(Message=message)

class Myapp(MDApp):
    def build(self):
        Builder.load_file('interface.kv')
        return Interface()
    
Myapp().run()