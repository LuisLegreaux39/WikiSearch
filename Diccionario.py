# Este programa debe buscar el significado de una palabra en wikipedia con la api de python
# e ir haciendo una base de datos en un excel de todas las palabras buscadas con su significado
import tkinter as TK
from partials import *
from wikipediaapi import Wikipedia
import os

###  Variables ####
padx = 10
pady = 10
bg = 'royal blue'
win = TK.Tk()
win.title("Traductor")
win.geometry('300x100')
win.config(bg='royal blue')
labelTitular = TK.Label(
win, text="¿Qué palabra quieres buscar?", font=5, padx=padx, bg=bg)
labelTitular.pack()
entryPalabra = TK.Entry(win, width=32)
entryPalabra.pack(pady=pady)
btnTraducir = TK.Button(win, text="Traduce", width=15,command=print("Hello"))
btnTraducir.pack()


# main()
def DefinitionWin(titutlo,resultado):
    titulo = str(titutlo)
    resultado = str(resultado)
    Definition = TK.Tk()
    Definition.geometry("200 x 400")
    Definition.title('Definicion')
    Definition.config(bg=bg)
    Titulo = TK.Label(Definition,text =titulo,font=15)
    Titulo.pack(justify='center',pady=pady)
    
    

############# Funciones #########################
def wikipedia_word_search(palabra):
    palabra = str(palabra)
    resultado = str()
    try:
        wiki = Wikipedia('es')
        busqueda = wiki.page(palabra)
        resultado = str(wiki.extracts(busqueda,exsentences=1))
    except Exception as e:
        print("No se pudo encontrar palabra")
        ExceptionLogCreator(e)
    return resultado

def mostrarDefinicion():
    


win.mainloop()
