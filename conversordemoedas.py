from tkinter import *
from tkinter import messagebox
from requests import *

############# WEB SCRAPING ################

url = get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
url_format= url.json()

dolar_hoje = url_format['USDBRL']['bid']
dolar_hoje = float(dolar_hoje)
dolar_hoje = round(dolar_hoje,2)

euro_hoje = url_format['EURBRL']['bid']
euro_hoje = float(euro_hoje)
euro_hoje = round(euro_hoje, 2)

bitcoin_hoje = url_format['BTCBRL']['bid']
bitcoin_hoje = float(bitcoin_hoje)
bitcoin_hoje = round(bitcoin_hoje,2)

########## INTERFACE GRAFICA ##########
janela_principal = Tk()
janela_principal.title('Conversor de Moedas')
janela_principal.geometry('310x490+400+200')
janela_principal.resizable(False, False)
janela_principal.config(background='#FFD700')

########## FUNCOES ##########
def converter():
    try:
        if text_real.get() == '' and text_euro.get() == '' and text_bitcoin.get() == '':
            dolar = float(text_dolar.get())

            real = dolar * dolar_hoje
            text_real.insert(0,round(real,3))

            euro = real / euro_hoje
            text_euro.insert(0,round(euro,3))

            bitcoin = real / bitcoin_hoje
            text_bitcoin.insert(0,round(bitcoin,3))

        elif text_dolar.get() == '' and text_euro.get() == '' and text_bitcoin.get() == '':
            real = float(text_real.get())

            dolar = real / dolar_hoje
            text_dolar.insert(0,round(dolar,2))

            euro = real / euro_hoje
            text_euro.insert(0,round(euro,3))

            bitcoin = real / bitcoin_hoje
            text_bitcoin.insert(0,round(bitcoin,3))

        elif text_real.get() == '' and text_euro.get() == '':
            euro = float(text_euro.get())

            real = euro * euro_hoje
            text_real.insert(0,round(real,3))
    
            euro = real / euro_hoje
            text_euro.insert(0,round(euro,2))

        elif text_real.get() == '' and text_bitcoin.get() == '':
            bitcoin = float(text_bitcoin.get())
            real = bitcoin * bitcoin_hoje
            text_real.insert(0,round(real,3))
    
            bitcoin = real / bitcoin_hoje
            text_bitcoin.insert(0,round(bitcoin,2))

    except ValueError:
        messagebox.showerror('Atenção', 'Por favor, colocar um valor númerico ')

def limpar():
    text_dolar.delete(0,END)
    text_real.delete(0,END)
    text_euro.delete(0,END)
    text_bitcoin.delete(0,END)

########## COMPONENTES ##########
logo = PhotoImage(file='css/imagem/conversormoedas.png')
logo = logo.subsample(4,4)
figural = Label(image=logo, bg ='#FFD700')

lixeira = PhotoImage(file='css/imagem/lixeira.png')
lixeira = lixeira.subsample(30,30)
figura2 = Label(image=lixeira, bg='#FFD700')

frame_dolar = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#FFD700')
label_dorlar = Label(janela_principal, text='Dolar', bg='#FFD700')
text_dolar = Entry(frame_dolar, width=46, bg ='#FFFAFA')

frame_real = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#FFD700')
label_real = Label(janela_principal, text='Real', bg='#FFD700')
text_real = Entry(frame_real, width=46, bg ='#FFFAFA')

frame_euro = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#FFD700')
label_euro = Label(janela_principal, text='Euro', bg='#FFD700')
text_euro = Entry(frame_euro, width=46, bg ='#FFFAFA')

frame_bitcoin = Frame(janela_principal, borderwidth=1.5, relief='solid', bg='#FFD700')
label_bitcoin = Label(janela_principal, text='Bitcoin', bg='#FFD700')
text_bitcoin = Entry(frame_bitcoin, width=46, bg ='#FFFAFA')

botao_converter = Button(janela_principal, text='Converta', font=('Georgia', 15), 
                    highlightthickness=0, bg ='#FFA500', command=converter)

botao_limpar = Button(janela_principal, image=lixeira, 
                highlightthickness=0, bg ='#FFA500', command=limpar)

########## LAYOUT ##########
figural.place(x=86, y=15)

frame_dolar.place(x=5, y=165, width=295, height=48)
label_dorlar.place(x=8, y=155)
text_dolar.place(x=5, y=15)

frame_real.place(x=5, y=235, width=295, height=48)
label_real.place(x=8, y=225)
text_real.place(x=5, y=15)

frame_euro.place(x=5, y=306, width=295, height=48)
label_euro.place(x=8, y=296)
text_euro.place(x=5, y=15)

frame_bitcoin.place(x=5, y=377, width=295, height=48)
label_bitcoin.place(x=8, y=367)
text_bitcoin.place(x=5, y=15)

botao_converter.place(x=86, y=440)
botao_limpar.place(x=270, y=440)

janela_principal.mainloop()