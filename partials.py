import os
import wikipedia

def ExceptionLogCreator(excepcion):
    excepcion = str(excepcion)
    error = str(excepcion)
    logName =str(excepcion[:25] + ".txt")
    log = open(logName, "w")
    log.write(error)
    log.close()
    print("Log was created")
    return True


# def suma(a,b):
#     resultado = a+b
#     return resultado


# try:
#     numero =int( input("Numero 1 :"))
#     numero2 =int( input("Numero 2 :"))
# except Exception as e:
#     print('no se pudo sumar los valores' + str(e))
#     ExceptionLogCreator(e)
# os.system('pause')



def wikipedia_word_search(palabra):
    
    palabra = str(palabra)
    resultado = str("0")
    try:
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(palabra,sentences=1)
        resultado = str(wiki)
    except Exception as e:
        print("No se pudo encontrar palabra")
        ExceptionLogCreator(e)
    return resultado

# print( wikipedia_word_search("python"))