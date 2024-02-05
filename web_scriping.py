from tkinter import messagebox
from requests import get

def obter_dados():
    try:
        url = get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
        url.raise_for_status()

        dados = url.json()
        return (
            float(dados['USDBRL']['bid']),
            float(dados['EURBRL']['bid']),
            float(dados['BTCBRL']['bid'])
        )
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao obter dados: {str(e)}')
        return None
