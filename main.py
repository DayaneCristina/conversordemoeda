from tkinter import Tk
from web_scriping import obter_dados
from funcoes import converter_dolar, converter_real, converter_euro, converter_bitcoin, preencher_campos, limpar
from componentes import criar_componentes
from layout import criar_layout

dolar_hoje, euro_hoje, bitcoin_hoje = obter_dados()

janela_principal = Tk()
janela_principal.title('Conversor de Moedas')
janela_principal.geometry('310x490+400+200')
janela_principal.resizable(False, False)
janela_principal.config(background='#4682B4')

figural, frame_dolar, label_dorlar, text_dolar, frame_real, label_real, text_real, \
frame_euro, label_euro, text_euro, frame_bitcoin, label_bitcoin, text_bitcoin, \
botao_converter, botao_limpar = criar_componentes(
    janela_principal, '#4682B4', '#FFFAFA', '#6495ED', preencher_campos, limpar
)

criar_layout(
    janela_principal, figural, frame_dolar, label_dorlar, text_dolar,
    frame_real, label_real, text_real, frame_euro, label_euro, text_euro,
    frame_bitcoin, label_bitcoin, text_bitcoin, botao_converter, botao_limpar
)

componentes = Componentes(janela_principal)
janela = Janela()

janela_principal.mainloop()
