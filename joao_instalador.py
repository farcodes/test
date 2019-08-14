#Feito por Thiago Narcizo

from tkinter import *
import urllib.request
import os

def bt_click():
    urllib.request.urlretrieve('https://scontent.fsdu2-2.fna.fbcdn.net/v/t34.0-12/11042244_910849995601826_971067101_n.jpg?_nc_cat=108&_nc_oc=AQnT-CQd1nLqV99AIYuiLcr6djyOEbbphwmrhCjqPNDuSix3IhdwCUHgFpMCqnu3r0A&_nc_ht=scontent.fsdu2-2.fna&oh=81c4c306f2e533d7e7ddaa9d866cfefa&oe=5D535440', os.getcwd() + '\JOAO_FOFO.jpg')

janela = Tk()

textlb1 = 'test'

janela.title('test')
janela.geometry('300x250')
lb1 = Label(janela, text = 'Instalador de fotos do João', font = ('Arial', 12, 'bold')).pack()
Label(janela, text = '').pack()
Button(janela, text = 'Baixar', command = bt_click).pack()
Label(janela, text = '').pack()
Label(janela, text = 'Feito por tEz', font = ('Arial', 12, 'italic')).pack()

janela.mainloop()
