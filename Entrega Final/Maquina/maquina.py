import random
def menu():
	entra=1
	fp=open ("Validado.txt","w")
	fp.close()
	fp1=open ("Camino.txt","w")
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
def manual():
		archivo1=open ("Entrada.txt","w")
		cadena=""
		ubi=open ("Camino.txt","a")
		ubi.close()
		print ("\t Usted eligio el modo manual\n Ingrese la cadena de 0's y 1's porfavor")
		cadena=input ()
		archivo=open ("Entrada.txt","a")
		archivo.write(cadena)
		archivo.write("\n")
		archivo.close()
		revision(1)
def automatico():
	archivo=open ("Automatico.txt","w")
	cadena =""
	ubi=open ("Camino.txt","a")
	ubi.close()
	print ("\t Usted eligio el modo automatico")
	archivo=open ("Automatico.txt","a")
	l=int (random.randrange(5,1000))
	print (l)
	cadena=""
	for a in range (l):
		elem=int(random.randrange(0,2))
		if elem==0:
			cadena=cadena+"1" 
		elif elem==1:
			cadena=cadena+"0"
	print (cadena)
	archivo.write(cadena)
	archivo.write("\n")
	archivo.close()
	revision(2)
def revision(j):
	if j==1:
		archivo= open("Entrada.txt","r")
	elif j==2:
		archivo= open("Automatico.txt","r")
	for linea in archivo:
		cadena=linea
		estados(cadena)
	archivo.close()
def estados(cadena):
	ubi=open ("Camino.txt","a")
	caracter=0
	palabra=cadena.split()
	palabra=palabra
	x=0
	for i in (palabra):
		v=i+"B"
		ban=0
		lista=[]
		index=0
		ubi=open ("Camino.txt","a")
		lista.extend(v)
		lista.insert(index,'---- Inicio -----> ')
		proceso (lista)
		del lista[index]
		cad=" ".join(lista)
		lista.insert(index,' q0->')
		proceso (lista)
		del lista [index]
		estado=0
		sigue=1
		while sigue==1:
			if estado==0:
				if lista[index]=='0':	
					lista.insert(index+1,' q1->')
					lista[index]="X"
					proceso(lista)
					del lista[index+1]
					index =index+1
					estado=1
				elif lista[index]=='Y':
					lista.insert(index+1,' q3->')
					lista[index]="Y"
					proceso(lista)
					del lista[index+1]
					index=index+1
					estado=3
				else :
					sigue=0
					lis=[]
					lis.extend('No Valida')
					proceso(lis)
			elif estado==1:
				if lista[index]=='0':	
					lista.insert(index+1,' q1->')
					lista[index]="0"
					proceso(lista)
					del lista[index+1]
					index =index+1
					estado=1
				elif lista[index]=='1':
					lista[index]="Y"
					lista.insert(index-1,' q2->')
					proceso(lista)
					del lista[index-1]
					index=index-1
					estado=2
				elif lista[index]=='Y':
					lista.insert(index+1,' q3->')
					lista[index]="Y"
					proceso(lista)
					del lista[index+1]
					index=index+1
					estado=1
				else :
					sigue=0
					lis=[]
					lis.extend('No Valida')
					proceso(lis)
			elif estado==2:
				if lista[index]=='0':
					lista[index]="0"	
					lista.insert(index-1,' q1->')
					proceso(lista)
					del lista[index-1]
					index =index-1
					estado=2
				elif lista[index]=='X':
					lista[index]="X"
					lista.insert(index+1,' q0->')
					proceso(lista)
					del lista[index+1]
					index=index+1
					estado=0
				elif lista[index]=='Y':
					lista[index]="Y"
					lista.insert(index-1,' q3->')
					proceso(lista)
					del lista[index-1]
					index=index-1
					estado=2
				else :
					sigue=0
					lis=[]
					lis.extend('No Valida')
					proceso(lis)
			if estado==3:
				if lista[index]=='B':	
					lista[index]="B"
					lista.insert(index-1,' q4-> ')
					proceso(lista)
					del lista[index-1]
					lista.insert (index+1, '------Fin Valida------')
					proceso (lista)
					index =index+1
					estado=4
					guardar(i)
					sigue=0
				elif lista[index]=='Y':
					lista.insert(index+1,' q4->')
					lista[index]="Y"
					proceso(lista)
					del lista[index+1]
					index=index+1
					estado=3
				else :
					sigue=0
					lis=[]
					lis.extend('No Valida')
					proceso(lis)


def proceso(lista):
	ubi=open ("Camino.txt","a")
	cad=" ".join(lista)
	print ('|-  '+cad)
	print ('\n')
	ubi.write("|-  ")
	ubi.write(" ".join(lista))
	ubi.write("\n")

def guardar(i):
	valida=open ("Validado.txt","a")
	valida.write(i)
	valida.write(" \n")
	valida.close()
menu()