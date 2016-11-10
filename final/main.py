def createArray():
	#Lee el archivo lineas.txt y lo pasa a un arreglo
	lineasMetro = list()
	with open('lineas.txt') as f:
	    for line in f:
	    	line = line.splitlines()
	    	if(line != ['']): #ignora los espacios en blanco
	    		lineasMetro.append(line[0].split(',')) #crea la lista de listas 
	return lineasMetro




lineasMetro = createArray()

