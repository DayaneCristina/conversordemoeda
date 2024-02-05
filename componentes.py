from tkinter import END, Tk, Label, Frame, Entry, Button, PhotoImage, messagebox
import requests

class ConversorMoeda:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.bg_color = '#FFFFFF'
        self.entry_bg_color = '#EDEDED'
        self.button_bg_color = '#4CAF50'

        self.text_dolar = Entry()
        self.text_real = Entry()
        self.text_euro = Entry()
        self.text_bitcoin = Entry()

        self.criar_componentes()

    def criar_componentes(self):
        logo = PhotoImage(file='css/imagem/conversormoedas.png')
        logo = logo.subsample(4, 4)
        figural = Label(image=logo, bg='#FFD700')
        figural.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        lixeira = PhotoImage(file='css/imagem/lixeira.png')
        lixeira = lixeira.subsample(30, 30)
        figura2 = Label(image=lixeira,bg='#FFD700')
        figura2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.frame_dolar = Frame(self.janela_principal, borderwidth=1.5, relief='solid', bg='#FFD700')
        self.frame_dolar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        label_dorlar = Label(self.frame_dolar, text='Dolar', bg='#FFD700')
        label_dorlar.grid(row=0, column=0, pady=5, padx=10)

        self.text_dolar = Entry(self.frame_dolar, width=46, bg='#FFD700')
        self.text_dolar.grid(row=0, column=1, pady=5, padx=10)

        botao_converter = Button(self.janela_principal, text='Converta', font=('Georgia', 15),
                                highlightthickness=0, bg=self.button_bg_color, command=self.converter)
        botao_converter.grid(row=6, column=0, columnspan=2, pady=10)

        botao_limpar = Button(self.janela_principal, image=lixeira,
                                highlightthickness=0, bg=self.button_bg_color, command=self.limpar)
        botao_limpar.grid(row=7, column=0, columnspan=2, pady=10)

    def calcular_conversao(self, valor, taxa):
        return valor * taxa

    def obter_taxas_cambio(self):
        try:
            url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
            resposta = requests.get(url)
            dados = resposta.json()

            if 'USDBRL' in dados and 'EURBRL' in dados and 'BTCBRL' in dados:
                usd_bid = float(dados['USDBRL'][0]['bid'])
                eur_bid = float(dados['EURBRL'][0]['bid'])
                btc_bid = float(dados['BTCBRL'][0]['bid'])

                return {
                    'USDBRL': {'bid': usd_bid},
                    'EURBRL': {'bid': eur_bid},
                    'BTCBRL': {'bid': btc_bid}
                }
            else:
                raise ValueError('Dados da API incompletos ou indisponíveis.')

        except Exception as e:
            raise ValueError(f'Erro ao obter taxas de câmbio: {str(e)}')

    def converter(self):
        try:
            url_format = self.obter_taxas_cambio()

            dolar_hoje = url_format['USDBRL']['bid']
            dolar_hoje = float(dolar_hoje)
            dolar_hoje = round(dolar_hoje, 2)

            if self.text_real.get() == '':
                dolar = float(self.text_dolar.get())
                real = self.calcular_conversao(dolar, dolar_hoje)
                self.text_real.delete(0, END)  # Removido para evitar duplicação
                self.text_real.insert(0, round(real, 2))

        except Exception as e:
            messagebox.showerror('Erro', f'Erro na conversão: {str(e)}')

    def limpar(self):
        self.text_dolar.delete(0, END)
        self.text_real.delete(0, END)
        self.text_euro.delete(0, END)
        self.text_bitcoin.delete(0, END)
