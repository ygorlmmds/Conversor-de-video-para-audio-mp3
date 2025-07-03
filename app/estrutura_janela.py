import tkinter as tk
from app.conversor import converter

def iniciar_janela():
    janela = tk.Tk()
    janela.title("Conversor de video mp3")
    janela.geometry('300x150')

    label = tk.Label(janela, text = "Clique para escolher um video:")
    label.pack(pady=10)

    botao = tk.Button(janela, text="Selecione o video para converter:", bg='green',  command=converter)
    botao.pack(pady=10)

    janela.mainloop()