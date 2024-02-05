from tkinter import Tk, Frame, Label, Entry, Button, messagebox

class ConversorMoeda(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.frame_dolar = Frame(self)
        self.label_dorlar = Label(self.frame_dolar, text="Dólar:")
        self.text_dolar = Entry(self.frame_dolar)

        self.frame_real = Frame(self)
        self.label_real = Label(self.frame_real, text="Real:")
        self.text_real = Entry(self.frame_real)

        self.frame_euro = Frame(self)
        self.label_euro = Label(self.frame_euro, text="Euro:")
        self.text_euro = Entry(self.frame_euro)

        self.frame_bitcoin = Frame(self)
        self.label_bitcoin = Label(self.frame_bitcoin, text="Bitcoin:")
        self.text_bitcoin = Entry(self.frame_bitcoin)

        self.botao_converter = Button(self, text="Converter", command=self.converter)
        self.botao_limpar = Button(self, text="Limpar", command=self.limpar)

        self.frame_dolar.grid(row=0, column=0, padx=5, pady=10)
        self.label_dorlar.grid(row=0, column=0, pady=5)
        self.text_dolar.grid(row=0, column=1, pady=5)

        self.frame_real.grid(row=1, column=0, padx=5, pady=10)
        self.label_real.grid(row=0, column=0, pady=5)
        self.text_real.grid(row=0, column=1, pady=5)

        self.frame_euro.grid(row=2, column=0, padx=5, pady=10)
        self.label_euro.grid(row=0, column=0, pady=5)
        self.text_euro.grid(row=0, column=1, pady=5)

        self.frame_bitcoin.grid(row=3, column=0, padx=5, pady=10)
        self.label_bitcoin.grid(row=0, column=0, pady=5)
        self.text_bitcoin.grid(row=0, column=1, pady=5)

        self.botao_converter.grid(row=4, column=0, pady=10)
        self.botao_limpar.grid(row=5, column=0, pady=10)

    def converter(self):
        try:
            dolar_hoje = float(dolar_hoje)
            euro_hoje = float(euro_hoje)
            bitcoin_hoje = float(bitcoin_hoje)

            if self.text_real.get() == '' and self.text_euro.get() == '' and self.text_bitcoin.get() == '':
                dolar = float(self.text_dolar.get())

                real = dolar * dolar_hoje
                self.text_real.insert(0, round(real, 3))

                euro = real / euro_hoje
                self.text_euro.insert(0, round(euro, 3))

                bitcoin = real / bitcoin_hoje
                self.text_bitcoin.insert(0, round(bitcoin, 3))

            elif self.text_dolar.get() == '' and self.text_euro.get() == '' and self.text_bitcoin.get() == '':
                real = float(self.text_real.get())

                dolar = real / dolar_hoje
                self.text_dolar.insert(0, round(dolar, 2))

                euro = real / euro_hoje
                self.text_euro.insert(0, round(euro, 3))

                bitcoin = real / bitcoin_hoje
                self.text_bitcoin.insert(0, round(bitcoin, 3))

            elif self.text_real.get() == '' and self.text_euro.get() == '':
                euro = float(self.text_euro.get())

                real = euro * euro_hoje
                self.text_real.insert(0, round(real, 3))

                euro = real / euro_hoje
                self.text_euro.insert(0, round(euro, 2))

            elif self.text_real.get() == '' and self.text_bitcoin.get() == '':
                bitcoin = float(self.text_bitcoin.get())
                real = bitcoin * bitcoin_hoje
                self.text_real.insert(0, round(real, 3))

                bitcoin = real / bitcoin_hoje
                self.text_bitcoin.insert(0, round(bitcoin, 2))

        except ValueError:
            messagebox.showerror('Atenção', 'Por favor, coloque um valor numérico')
            pass

    def limpar(self):
        self.text_dolar.delete(0, 'end')
        self.text_real.delete(0, 'end')
        self.text_euro.delete(0, 'end')
        self.text_bitcoin.delete(0, 'end')
        pass

if __name__ == "__main__":
    root = Tk()
    app = ConversorMoeda(master=root)
    app.mainloop()