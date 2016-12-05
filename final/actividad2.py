

#BubbleSort Optimizado
def bubbleSortOptimized(A):
    n = len(A)
    i = 1
    comparaciones = 0
    flag = True
    print("Numero de elementos de la lista: ", n)
    while i < n-1 and flag:
        flag = False
        print "Pasada: " + str(i)
        for j in range(0, n-i):
            print(A)
            comparaciones += 1
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                flag = True
        i+=1
    print("comparaciones: ", comparaciones)
    print("iteraciones: ", i-1)
    return A

def save(A):
    archivo = open("lista.txt", "w")
    for linea in A:
        archivo.write(linea + "\n")
    archivo.close()





def actividad2():
    estaciones = ['balderas', 'cuauhtemoc', 'juarez', 'ninosheroes', 'saltodelagua', 'insurgentes', 'hidalgo', 'hospitalgeneral', 'doctores', 'isabellacatolica', 'sanjuandeletran', 'sevilla', 'bellasartes', 'guerrero', 'revolucion', 'centromedico', 'obrera', 'pinosuarez', 'chapultepec', 'alllende', 'garibaldilagunilla', 'buenavista', 'tlatelolco', 'sancosme', 'chilpancingo', 'etiopiaplazadelatransparencia', 'lazarocardenas', 'chabacano', 'merced', 'sanantonioabad', 'zocalo', 'juanacatlan', 'lagunilla', 'laraza', 'normal', 'patriotismo', 'eugenia', 'jamaica', 'laviga', 'viaducto', 'candelaria', 'allende', 'tacubaya', 'tepito', 'autobusesdelnorte', 'misterios', 'potrero', 'colegiomilitar', 'divisiondelnorte', 'frayservando', 'mixiuhca', 'santaanita', 'xola', 'morelos', 'sanlazaro', 'constituyentes', 'observatorio', 'snpedrodelospinos', 'institutodelpetroleo', 'vallegomez', 'deportivo18demarzo', 'popotla', 'zapata', 'velodromo', 'coyuya', 'villadecortes', 'canaldelnorte', 'floresmagon', 'moctezuma', 'auditorio', 'snantonio', 'lindavista', 'politecnico', 'vallejo', 'consulado', 'indiosverdes', 'lavilla-basilica', 'cuitlahuac', '20denoviembre', 'coyoacan', 'parquedelosvenados', 'ciudaddeportiva', 'iztacalco', 'nativitas', 'romerorubio', 'balbuena', 'polanco', 'mixcoac', 'norte45', 'bondojito', 'eduardomolina', 'martincarrera', 'tacuba', 'insurgentessur', 'viverosderechoshumanos', 'ejecentral', 'puebla', 'apatlaco', 'oceania', 'boulevardpuertoaereo', 'sanjoaquin', 'barrancadelmuerto', 'ferreria', 'talisman', 'aragon', 'panteones', 'refineria', 'miguelangeldequevedo', 'ermita', 'pantitlan', 'aculco', 'deportivooceania', 'terminalaerea', 'gomezfarias', 'azcapotzalco', 'cuatrocaminos', 'camarones', 'copilco', 'generalanaya', 'mexicaltzingo', 'portales', 'hangares', 'zaragoza', 'escuadron201', 'bosquedearagon', 'tezozomoc', 'aquilesserdan', 'universidad', 'tasquena', 'atlalilco', 'nativias', 'villadearagon', 'elrosario', 'iztapalapa', 'puebloculhuacan', 'nezahualcoyotl', 'cdelaestrella', 'esimeculhuacan', 'impulsora', 'uam1', 'tomatlan', 'riodelosremedios', 'constde1917', 'calle11', 'muzquiz', 'perifericoote', 'ecatepec', 'tezonco', 'olimpica', 'olivos', 'plazadearagon', 'nopalera', 'ciudadazteca', 'zapotitlan', 'tlatenco', 'tlahuac']
    listaOrdenada = bubbleSortOptimized(estaciones)
    save(listaOrdenada)

actividad2()

