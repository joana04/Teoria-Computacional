import random 
def manual():
		cadena=""
		ubi=open ("Camino.txt","a")
		ubi.close()
		print ("\t Usted eligio el modo manual\n Ingrese la cadena de parentesis porfavor")
		cadena=input ()
		archivo=open ("Entrada.txt","a")
		archivo.write(cadena)
		archivo.write("\n")
		archivo.close()
		fp=open ("Validado.txt","a")
		fp.close()
		revision(1)
def automatico():
		cadena =""
		ubi=open ("Camino.txt","a")
		ubi.close()
		print ("\t Usted eligio el modo automatico")
		archivo=open ("Automatico.txt","a")
		l=int (random.randrange(5,20))
		print (l)
		cadena=""
		for a in range (l):
			elem=int(random.randrange(0,2))
			if elem==0:
				cadena=cadena+"(" 
			elif elem==1:
				cadena=cadena+")"
		print (cadena)
		archivo.write(cadena)
		archivo.write("\n")
		archivo.close()
		fp=open ("Validado.txt","a")
		fp.close()
		revision(2)
def revision(j):
	if j==1:
		archivo= open("Entrada.txt","r")
	elif j==2:
		archivo= open("Automatico.txt","r")
	y=0
	for linea in archivo:
		cadena=linea
		estados(cadena,y)
		y=y+1
	archivo.close()
def estados(cadena,y):
	ubi=open ("Camino.txt","a")
	caracter=0
	palabra=cadena.split()
	x=0
	ban1=0
	for i in palabra:
		ban1=0
		tamaño=len(i)
		#estado=0
		tam=0
		c=0
		nop=0
		lista=['']
		ubi.write(i)
		ubi.write("\n")
		for a in (i+","):	
			if a=='(':
				if c==0 :#veo que sea la primera vez que entre 
					lista.extend('B')
					lista [0]='Inicio'
					print (lista )
					print ("\n")
					ubi.write("".join(lista))
					ubi.write("\n")
					lista.extend ('(RB')
					del lista[1]
					lista [0]='B--> (RB ----->'
					print (lista )
					print ("\n")
					ubi.write("".join(lista))
					ubi.write("\n")
					tam=tam+1
					c=1
				elif c==1:
					if ('R' in lista):
						v=int(lista.index('R')+1)
						lista.insert(v,'R')
						lista.insert(v,'R')
						lista.insert(v,'(')
						lista [0]='R--> (RR ----->'
						del lista [v-1]
						print (lista )
						print ("\n")
						ubi.write("".join(lista))
						ubi.write("\n")
						tam=tam+1
					elif ('B' in lista):
						v=int(lista.index('B')+1)
						lista.insert(v,'B')
						lista.insert(v,'R')
						lista.insert(v,'(')
						lista [0]='B--> (RB ----->'
						del lista [v-1]
						print (lista  )
						print ("\n")
						ubi.write("".join(lista))
						ubi.write("\n")
						tam=tam+1
			elif a==')':
				if ('R' in lista):
					v=int(lista.index('R')+1)
					lista.insert(v,')')
					del lista [v-1]
					lista [0]='R--> ) ----->'
					print (lista )
					print ("\n")
					ubi.write("".join(lista))
					ubi.write("\n")
					tam=tam+1
				else :
					nop==1
					tam=tam+1
			elif a==",":
				if ('B' in lista):
					while ('B ' in lista):
						v=int(lista.index('B')+1)
						lista.insert(v,'')
						del lista [v-1]
						lista [0]='B--> e ----->'
						print (lista )
						print ("\n")
						ubi.write("".join(lista))
						ubi.write("\n")
						tam=tam+1
				if('R' in lista ):
					nop=1
					tam=tam+1
			elif nop==1:
				print ("No valida \n")
				ubi.write(lista)
				ubi.write("no valida \n")
				break
			

		if (('B' in lista) and (tam==len(lista)-2)):
			v=int(lista.index('B')+1)
			lista.insert(v,'')
			del lista [v-1]
			lista [0]='B--> e ----->'
			print (lista )
			print ("\n")
			ubi.write("".join(lista))
			ubi.write("\n")
			guardar (i)
		else:
			print ("------Cadena invalida -------")
			ubi.write("No valida \n")
def guardar(i):
	palabra=i
	valida=open ("Validado.txt","a")
	valida.write(palabra)
	valida.write(" \n")
	valida.close()
def menu():
	entra=1
	fp=open ("Validado.txt","w")
	fp.close()
	ubi=open ("Camino.txt","w")
	ubi.close()
	archivo=open ("Automatico.txt","w")
	archivo1=open ("Entrada.txt","w")
	while entra==1:
		print("\t\tSeleccione la opcion deseada\n 1.-Manual\n2.-Automatico\n")
		opc=str(input())
		#opc=str(random.randrange(1,3))
		print(opc)
		if opc=='1':
			manual()
		elif opc=='2':
			automatico()
		print("desea regresar?\n1.-Si\,2.-No\n")
		entra=int(input())
		#entra=random.randrange(0,2)
	print ("\t\tADIOS\n")

menu()
