import os

def ExceptionLogCreator(excepcion):
    excepcion = str(excepcion)
    error = str(excepcion)
    logName =str(excepcion[:25] + ".txt")
    log = open(logName, "w")
    log.write(error)
    log.close()
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