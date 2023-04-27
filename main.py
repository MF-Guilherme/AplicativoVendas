from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class HomePage(Screen):
    pass


class AjustesPage(Screen):
    pass


GUI = Builder.load_file("main.kv")
class MainApp(App):

    def build(self):
        return GUI

    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"] #self.root é o main.kv, a minha página de screen manager
        gerenciador_telas.current = id_tela #qual tela atual (current) vc está falando? da que chegar no parametro
MainApp().run()