import os
from googletrans import Translator
import requests
from bs4 import BeautifulSoup

# print("Introdusca la url de su pagina")
url ="https://stackabuse.com/text-translation-with-google-translate-api-in-python/"# "https://docs.python.org/2.1/ext/callingPython.html"
# url= input(str(":"))
fileName = "index.html"
filename = "resultado.html"

pagina = open(fileName,"w")
request = requests.get(url)
line = str(request.text)
pagina.write(line)
pagina.close()

fileread = open(fileName,"r")
content = fileread.read()
fileread.close()
soup = BeautifulSoup(content,'html.parser')
line = soup.get_text()

trans = Translator()
result = trans.translate(line,dest='es')

print(line)
pagina = open(filename,"w")
pagina.write(str(result.text))
fileread.close()




os.system("pause")