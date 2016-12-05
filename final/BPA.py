def BPA(list_1,char):
	Queue=[char]
	list_BPA=[]
	while len(list_BPA) != 7:
		char=Queue.pop(0)
		list_aux=partner(list_1,char)
		list_BPA.append(char)
		boolean=1
		for item in list_aux:
			for item_2 in list_BPA:
				if(item == item_2):
					boolean = 0
			if (boolean == 1):
				Queue.append(item)
				print(item)
	return list_BPA

def partner(list_1,char):
	list_partner=[]
	for i in range(0,len(list_1)-1):
		for j in range (0,1):
			if(char == list_1[i][0]):
				list_partner.append(list_1[i][1])
	return list_partner

def main():

	char = "balderas"
	list_1=[["balderas", "cuauhtemoc"],
	["balderas", "juarez"], 
	["balderas", "ninosheroes"], 
	["balderas", "saltodelagua"], 
	["cuauhtemoc", "insurgentes"], 
	["juarez", "hidalgo"]
	]
	list_BPA=BPA(list_1,char)
	print(list_BPA)

main()
