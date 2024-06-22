import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

class Produto:
    def __init__(self, nome, preco, url_imagem):
        self.nome = nome
        self.preco = preco
        self.url_imagem = url_imagem
        self.imagem_local = self.baixar_imagem()

    def baixar_imagem(self):
        response = requests.get(self.url_imagem)
        img_nome = self.url_imagem.split("/")[-1]
        with open(img_nome, 'wb') as file:
            file.write(response.content)
        return img_nome

class LojaApp(App):
    def build(self):
        self.title = "Loja de Eletrônicos"
        
        # Produtos da loja com URLs de imagens da internet
        self.produtos = [
            Produto("Smartphone", 1500.0, "https://example.com/smartphone.jpg"),
            Produto("Notebook", 3500.0, "https://example.com/notebook.jpg"),
            Produto("Tablet", 1200.0, "https://example.com/tablet.jpg"),
            Produto("Fone de Ouvido", 200.0, "https://example.com/fone_de_ouvido.jpg"),
            Produto("Smartwatch", 800.0, "https://example.com/smartwatch.jpg")
        ]
        
        layout = BoxLayout(orientation='vertical')
        
        # Criação de um ScrollView para a lista de produtos
        scroll_view = ScrollView()
        produtos_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        produtos_layout.bind(minimum_height=produtos_layout.setter('height'))
        
        # Adicionando produtos ao layout
        for produto in self.produtos:
            produto_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=120)
            imagem = Image(source=produto.imagem_local, size_hint_x=0.3)
            produto_layout.add_widget(imagem)
            produto_detalhes = BoxLayout(orientation='vertical', size_hint_x=0.5)
            produto_detalhes.add_widget(Label(text=produto.nome))
            produto_detalhes.add_widget(Label(text=f"R$ {produto.preco:.2f}"))
            produto_layout.add_widget(produto_detalhes)
            botao_comprar = Button(text="Comprar", size_hint_x=0.2)
            botao_comprar.bind(on_press=self.comprar_produto)
            produto_layout.add_widget(botao_comprar)
            produtos_layout.add_widget(produto_layout)
        
        scroll_view.add_widget(produtos_layout)
        layout.add_widget(scroll_view)
        
        return layout
    
    def comprar_produto(self, instance):
        produto_nome = instance.parent.children[2].children[1].text
        print(f"Produto {produto_nome} comprado com sucesso!")

if __name__ == '__main__':
    LojaApp().run()
