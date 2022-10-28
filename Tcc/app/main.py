from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window

Window.size = (470,750)

class home(Screen):
    ...

class Interface(ScreenManager):
    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela

class Myapp(MDApp):
    def build(self):
        Builder.load_file('interface.kv')
        return Interface()
    
Myapp().run()