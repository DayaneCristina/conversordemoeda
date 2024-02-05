from tkinter import END, Entry, messagebox
import requests

class ConversorMoeda:
    def __init__(self, text_dolar, text_real, text_euro, text_bitcoin):
        self.text_dolar = text_dolar
        self.text_real = text_real
        self.text_euro = text_euro
        self.text_bitcoin = text_bitcoin
        self.dolar_hoje, self.euro_hoje, self.bitcoin_hoje = self.obter_taxas_cambio()

    def obter_taxas_cambio(self):
        try:
            url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
            resposta = requests.get(url)
            dados = resposta.json()

            dolar_hoje = float(dados['USDBRL']['bid'])
            euro_hoje = float(dados['EURBRL']['bid'])
            bitcoin_hoje = float(dados['BTCBRL']['bid'])

            return dolar_hoje, euro_hoje, bitcoin_hoje

        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao obter taxas de câmbio: {str(e)}')
            return 1.0, 1.0, 1.0

    def converter(self):
        try:
            if self.text_real.get() == '' and self.text_euro.get() == '' and self.text_bitcoin.get() == '':
                dolar = float(self.text_dolar.get())

                real = dolar * self.dolar_hoje
                self.text_real.insert(0, round(real, 3))

                euro = real / self.euro_hoje
                self.text_euro.insert(0, round(euro, 3))

                bitcoin = real / self.bitcoin_hoje
                self.text_bitcoin.insert(0, round(bitcoin, 3))

            elif self.text_dolar.get() == '' and self.text_euro.get() == '' and self.text_bitcoin.get() == '':
                real = float(self.text_real.get())
                dolar = real / self.dolar_hoje
                self.text_dolar.insert(0, round(dolar, 2))

                euro = real / self.euro_hoje
                self.text_euro.insert(0, round(euro, 3))

                bitcoin = real / self.bitcoin_hoje
                self.text_bitcoin.insert(0, round(bitcoin, 3))

            elif self.text_real.get() == '' and self.text_euro.get() == '':
                euro = float(self.text_euro.get())
                real = euro * self.euro_hoje
                self.text_real.insert(0, round(real, 3))

                euro = real / self.euro_hoje
                self.text_euro.insert(0, round(euro, 2))

            elif self.text_real.get() == '' and self.text_bitcoin.get() == '':
                bitcoin = float(self.text_bitcoin.get())
                real = bitcoin * self.bitcoin_hoje
                self.text_real.insert(0, round(real, 3))

                bitcoin = real / self.bitcoin_hoje
                self.text_bitcoin.insert(0, round(bitcoin, 2))

        except ValueError:
            messagebox.showerror('Atenção', 'Por favor, coloque um valor numérico ')

    def limpar(self):
        self.text_dolar.delete(0, END)
        self.text_real.delete(0, END)
        self.text_euro.delete(0, END)
        self.text_bitcoin.delete(0, END)

if __name__ == "__main__":
    text_dolar = Entry()
    text_real = Entry()
    text_euro = Entry()
    text_bitcoin = Entry()

    conversor = ConversorMoeda(text_dolar, text_real, text_euro, text_bitcoin)
    conversor.converter()  # Chame a função converter
    conversor.limpar()  # Chame a função limpar
    