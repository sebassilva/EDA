def BinarySearch(A, item, start, end): 
	if start >= end: 
		print("False because")
		return False
	center = int((end-start)/2) + start
	print("center", center)
	print("start", start)
	print("end", end)
	if A[center] == item: 
		print(center)
		print("A es igual a center")
		#print (center)
		return center + 1
	else: 
		if item > A[center]:
			BinarySearch(A, item, center+1, end)
		else: 
			BinarySearch(A, item, start, center-1)




estaciones = ['balderas', 'cuauhtemoc', 'juarez', 'ninosheroes', 'saltodelagua', 'insurgentes', 'hidalgo', 'hospitalgeneral', 'doctores', 'isabellacatolica', 'sanjuandeletran', 'sevilla', 'bellasartes', 'guerrero', 'revolucion', 'centromedico', 'obrera', 'pinosuarez', 'chapultepec', 'alllende', 'garibaldilagunilla', 'buenavista', 'tlatelolco', 'sancosme', 'chilpancingo', 'etiopiaplazadelatransparencia', 'lazarocardenas', 'chabacano', 'merced', 'sanantonioabad', 'zocalo', 'juanacatlan', 'lagunilla', 'laraza', 'normal', 'patriotismo', 'eugenia', 'jamaica', 'laviga', 'viaducto', 'candelaria', 'allende', 'tacubaya', 'tepito', 'autobusesdelnorte', 'misterios', 'potrero', 'colegiomilitar', 'divisiondelnorte', 'frayservando', 'mixiuhca', 'santaanita', 'xola', 'morelos', 'sanlazaro', 'constituyentes', 'observatorio', 'snpedrodelospinos', 'institutodelpetroleo', 'vallegomez', 'deportivo18demarzo', 'popotla', 'zapata', 'velodromo', 'coyuya', 'villadecortes', 'canaldelnorte', 'floresmagon', 'moctezuma', 'auditorio', 'snantonio', 'lindavista', 'politecnico', 'vallejo', 'consulado', 'indiosverdes', 'lavilla-basilica', 'cuitlahuac', '20denoviembre', 'coyoacan', 'parquedelosvenados', 'ciudaddeportiva', 'iztacalco', 'nativitas', 'romerorubio', 'balbuena', 'polanco', 'mixcoac', 'norte45', 'bondojito', 'eduardomolina', 'martincarrera', 'tacuba', 'insurgentessur', 'viverosderechoshumanos', 'ejecentral', 'puebla', 'apatlaco', 'oceania', 'boulevardpuertoaereo', 'sanjoaquin', 'barrancadelmuerto', 'ferreria', 'talisman', 'aragon', 'panteones', 'refineria', 'miguelangeldequevedo', 'ermita', 'pantitlan', 'aculco', 'deportivooceania', 'terminalaerea', 'gomezfarias', 'azcapotzalco', 'cuatrocaminos', 'camarones', 'copilco', 'generalanaya', 'mexicaltzingo', 'portales', 'hangares', 'zaragoza', 'escuadron201', 'bosquedearagon', 'tezozomoc', 'aquilesserdan', 'universidad', 'tasquena', 'atlalilco', 'nativias', 'villadearagon', 'elrosario', 'iztapalapa', 'puebloculhuacan', 'nezahualcoyotl', 'cdelaestrella', 'esimeculhuacan', 'impulsora', 'uam1', 'tomatlan', 'riodelosremedios', 'constde1917', 'calle11', 'muzquiz', 'perifericoote', 'ecatepec', 'tezonco', 'olimpica', 'olivos', 'plazadearagon', 'nopalera', 'ciudadazteca', 'zapotitlan', 'tlatenco', 'tlahuac']
index = BinarySearch(estaciones, 'saltodelagua', 0, len(estaciones))
