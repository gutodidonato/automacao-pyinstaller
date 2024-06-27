from tkinter import *

valorSite = ""




def executar_login():
    global valorSite
    campoSite = url.get()
    if (campoSite != ""):
        window.destroy()
        valorSite = campoSite


        

#variaveis-------------------------------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
valor_palavra = ""

    

window = Tk()
window.title("Login")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


nome_url = Label(text="Site Url", highlightthickness=0, background=BACKGROUND_COLOR).grid(row=0, column=0)
url = Entry(highlightthickness=0)
url.grid(row=0, column=1)


Logar = Button(command=executar_login, text="Verificar")
Logar.grid(row=4, column=1)


window.mainloop()