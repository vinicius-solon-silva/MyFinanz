from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
import db_categoria
import gen_charts


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
    def gen_chart(self):
        dict = {"neymar": 250.00, "messi": 300.00}
        gen_charts.generate(dict)

                
class Myapp(MDApp):
    def build(self):
        Builder.load_file('interface.kv')
        return Interface()
    
    # Dialog
    dialog = None
    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(title=message)
        self.dialog.open()

    
    
        
Myapp().run()