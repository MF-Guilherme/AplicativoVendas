from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from bannervenda import BannerVenda
import os
from functools import partial
from myfirebase import MyFirebase

GUI = Builder.load_file("main.kv")


class MainApp(App):
    id_usuario = 1

    def build(self):
        self.firebase = MyFirebase()
        return GUI

    def on_start(self):
        # carregar as fotos de perfil
        arquivos = os.listdir('icones/fotos_perfil')
        pagina_fotoperfil = self.root.ids['fotoperfilpage']
        lista_fotos = pagina_fotoperfil.ids['lista_fotos_perfil']
        
        for foto in arquivos:
            imagem = ImageButton(source=f'icones/fotos_perfil/{foto}', on_release=partial(self.mudar_foto_perfil, foto))
            lista_fotos.add_widget(imagem)
        # carrega as infos do usuario
        self.carregar_infos_usuario()

    def carregar_infos_usuario(self):
        # pegar informações do usuario
        requisicao = requests.get(f"https://aplicativovendashash-4e118-default-rtdb.firebaseio.com/{self.id_usuario}.json")
        requisicao_dic = requisicao.json()

        # preencher foto de perfil
        avatar = requisicao_dic['avatar']
        foto_perfil = self.root.ids["foto_perfil"]
        foto_perfil.source = f"icones/fotos_perfil/{avatar}"

        # preencher lista de vendas
        try:
            vendas = requisicao_dic["vendas"][1:]
            pagina_homepage = self.root.ids["homepage"]
            lista_vendas = pagina_homepage.ids['lista_vendas']
            for venda in vendas:
                banner = BannerVenda(cliente=venda['cliente'],
                                     foto_cliente=venda['foto_cliente'],
                                     produto=venda['produto'],
                                     foto_produto=venda['foto_produto'],
                                     data=venda['data'],
                                     preco=venda['preco'],
                                     unidade=venda['unidade'],
                                     quantidade=venda['quantidade'])
                lista_vendas.add_widget(banner)
        except:
            pass

    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"]  # self.root é o main.kv, a minha página de screen manager
        gerenciador_telas.current = id_tela  # qual tela atual (current) vc está falando? da que chegar no parametro

    def mudar_foto_perfil(self, foto, *args):
        foto_perfil = self.root.ids["foto_perfil"]
        foto_perfil.source = f"icones/fotos_perfil/{foto}"
        
        info = f'{{"avatar": "{foto}"}}'
        requisicao = requests.patch(f"https://aplicativovendashash-4e118-default-rtdb.firebaseio.com/{self.id_usuario}.json",
                                    data=info)
        
        self.mudar_tela("ajustespage")


MainApp().run()
