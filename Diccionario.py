# Este programa debe buscar el significado de una palabra en wikipedia con la api de python
# e ir haciendo una base de datos en un excel de todas las palabras buscadas con su significado
import tkinter as TK
from tkinter import messagebox
from partials import *
from wikipediaapi import Wikipedia
import os

###  Variables ####
padx = 10
pady = 10
bg = 'royal blue'
def main():
    win = TK.Tk()
    win.title("Traductor")
    win.geometry('300x100')
    win.config(bg='royal blue')
    labelTitular = TK.Label(
    win, text="¿Qué palabra quieres buscar?", font=5, padx=padx, bg=bg,fg='white')
    labelTitular.pack()
    entryPalabra = TK.Entry(win, width=32)
    entryPalabra.pack(pady=pady)
    btnTraducir = TK.Button(win, text="Traduce", width=15,command=lambda:mostrarDefinicion(entryPalabra.get()))
    btnTraducir.pack()
    win.mainloop()

# main()
def DefinitionWin(titutlo,resultado):
    titulo = str(titutlo)
    resultado = str(resultado)
    Definition = TK.Tk()
    Definition.geometry("300x400")
    Definition.title('Definicion')
    Definition.config(bg=bg)
    Titulo = TK.Label(Definition,text=titulo,font=('Times New Roman ',20),justify='center',bg=bg,fg='white')
    Titulo.pack(pady=2)
    definicionBody= TK.LabelFrame(Definition,bg=bg,text="definicion")
    definicionBody.pack(fill='both',expand='yes',padx=padx,pady=5)
    textoBody = TK.Label(definicionBody,text=resultado,justify='center',bg=bg,fg='white',wraplength=350)
    textoBody.pack(pady=2,padx=5)
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

def mostrarDefinicion(Palabra_Buscada):
        titulo = str(Palabra_Buscada)
        if(len(titulo)<1):
            messagebox.showerror(title='Campo Vacion',
                                    message="Debe rellenar el campo d palabra")
        else:
            resultado=wikipedia_word_search(titulo)
            DefinitionWin(titulo,resultado)
main()

