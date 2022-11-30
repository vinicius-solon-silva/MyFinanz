from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import db_categoria


Window.size = (470,750)

class home(Screen):
    ...

class categorias(Screen):
    ...

class Interface(ScreenManager):
    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela
    def add_categoria(self, nome, valor):
        msg = db_categoria.gera_categoria(nome, valor)
        return msg
                
class Myapp(MDApp):
    dialog = None
    def build(self):
        Builder.load_file('interface.kv')
        return Interface()
    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(title=message)
        self.dialog.open()
        
Myapp().run()