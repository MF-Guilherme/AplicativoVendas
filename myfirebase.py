from kivy.app import App
import requests


class MyFirebase():
    API_KEY = 'AIzaSyC3JI4r2C-MmVnw53jBcCuIH7Uck5lm4WA'

    def criar_conta(self, email, senha):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"
        print(email, senha)
        info = {"email": email,
                "password": senha,
                "returnSecureToken": True}
        
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()
        
        if requisicao.ok:
            print("Usuário criado")
        else:
            mensagem_erro = requisicao_dic["error"]["message"]
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids['loginpage']
            pagina_login.ids["mensagem_login"].text = mensagem_erro
            pagina_login.ids["mensagem_login"].color = (1, 0, 0, 1)
        print(requisicao_dic)
        


    def fazer_login(self, email, senha):
        pass