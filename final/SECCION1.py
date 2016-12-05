# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:52:24 2016

@author: Cecilia
"""
def main():

    def createArray():        
        	#Lee el archivo lineas.txt y lo pasa a un arreglo        
        	lineasMetro = list()        
        	with open('lineas.txt') as f:        
        	    for line in f:        
        	    	line = line.splitlines()         
        	    	if(line != ['']): #ignora los espacios en blanco        
        	    		lineasMetro.append(line[0].split(',')) #crea la lista de listas 
        	return lineasMetro
  
    def vecinos(Grafo,valor):
        lista_vecino=[]
        for i in range (0,len(Grafo)):
            for j in range(0,1):
                if (valor==Grafo[i][0]):
                    lista_vecino.append(Grafo[i][1])
        for i in range (len(Grafo)):
            Grafo[i].reverse()
            if (valor==Grafo[i][0]):
                    lista_vecino.append(Grafo[i][1]) 
        return lista_vecino

    def BPA(Grafo,valor):#recibe al grafo y al valor
        cola=[valor]
        print(cola)
        lista_BFS=[]
        while  len(cola) !=0:
            valor=cola.pop(0)
            lista_BFS.append(valor)
            lista_vecinos=vecinos(Grafo,valor)
            lista_vecinos.sort()
            lista_vecinos.reverse()
            for x in range(len(lista_vecinos)-1,-1,-1):
                if lista_vecinos[x] not in lista_BFS:
                    cola.append(lista_vecinos[x])
            cola=Scan(cola)
        return lista_BFS
        
    def Scan(cola):#revisa que no haya duplicados
        aux=[]
        for item in cola:
            if item not in aux:
                aux.append(item)
        return aux
        
    lineasMETRO=createArray()
    print(BPA(lineasMETRO,'jamaica'))
    
    
main()