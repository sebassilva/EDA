#Universidad Nacional Autónoma de México
#Facultad de Ingeniería
#Ingeniería en Computación
#Estructuras de Datos y Algoritmos
#UrlTimePlot.py
#Creado por:
#Aguilera, Tania
#López, Gerardo
#Silva, Sebastián
#Licencia de Software: MIT

#Si se llegara a presentar el error: "unknown locale UTF-8", copiar y pegar esta línea en la consola:
# "echo -e "export LC_ALL=en_US.UTF-8\nexport LANG=en_US.UTF-8" >> ~/.bashrc && source ~/.bashrc"
#Importa las librerías necesarias para su funcionamiento
import urllib.request
from time import time
from matplotlib import pyplot as plt
from matplotlib import style
#Se definen los arreglos en el que se almacenan los tiempos y las URLS, así como variables globales necesarias
timeArray = []
urlArray = []
otherUrl = True
i=0

def responseTime(urlToParse):
	#Obtiene el tiempo que se tarda en obtener respuesta y parsear su contenido de un servidor
    global i
    i+=1
    t0 = time()
    partial=0;
    #Hace la petición y lee el contenido de la respuesta
    response = urllib.request.urlopen(urlToParse).read()
    partial= time()-t0
    print("Tiempo: "+ format(partial) + " de "+ urlToParse)
    #Agrega el tiempo al arreglo de tiempos
    timeArray.append(partial)
    urlArray.append(i)
  

while otherUrl is True: 
	#Pide tantas direcciones como se quieran comparar
	url = input("Ingresa una dirección a comparar: ")
	if url: 
		try: 
			#Si se ingresó una cadena válida
			responseTime(url)
			print(otherUrl)
		except ValueError:
			print("Ingresa una dirección válida")
		otherUrl = True
	else: 
		#Si no se ingresó ninguna URL
		if len(urlArray) > 1: 
			otherUrl = False
			style.use('ggplot')
			x = urlArray
			y = timeArray
			plt.bar(x, y, align='center')
			plt.title('Tiempo de respuesta')
			plt.ylabel('Tiempo [s]')
			plt.xlabel('# de url')
			#imprime la gráfica
			plt.show()
			break
		else: 
			print("Ingresa al menos una dirección.")




