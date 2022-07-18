from unittest.util import _MAX_LENGTH
import requests
import json
from tkinter import *

def metar():
    API_KEY = "1KZCif5lwt6IbJOWuKZJ1rkh4eVvLp1nJMFDoSfP"
    LOCALIDADE = premetar.get()
    requisicao = requests.get(f'https://api-redemet.decea.mil.br/mensagens/metar/{LOCALIDADE}?api_key={API_KEY}&data_')
    requisicao_dic = requisicao.json()
        
    
    weather = requisicao_dic['data']['data'][0]['mens']
    
    texto_metar["text"] = weather
    texto_metar.grid(row=2, column=3)


janela = Tk()
janela.title('METAR')
janela.geometry("800x200")


texto_orientacao = Label(janela, text="Insira o metar: ", font=("Calibri", 15), justify=CENTER)
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='BUSCAR', command=metar, font=("Calibri", 15), justify=CENTER)
botao.grid(column=0, row=3, padx=10, pady=10)


texto_metar = Label(janela, text="", font=("Calibri", 15), justify=CENTER)
texto_metar.grid(column=0, row=6, padx=10, pady=10)


premetar = Entry(janela, bd=2, width=8, font=("Calibri", 15))
premetar.grid(column=0, row=2)





janela.mainloop()