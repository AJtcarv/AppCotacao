from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"] = "Dolar R$ 6"
        self.root.ids["moeda2"] = "Euro R$ 7"
        self.root.ids["moeda3"] = "BitCoin R$ 35k"
        self.root.ids["moeda4"] = "Ethereum R$"

MeuAplicativo().run()