import random 
def manual():
		cadena=""
		ubi=open ("Camino.txt","w")
		ubi.close()
		print ("\t Usted eligio el modo manual\n Ingrese la cadena de i's y 0's porfavor")
		cadena=input ()
		archivo=open ("Manual.txt","w")
		archivo.write(cadena)
		archivo.close()
		fp=open ("Validado.txt","w")
		fp.close()
		revision(1)
def automatico():
		cadena =""
		ubi=open ("Camino.txt","w")
		ubi.close()
		print ("\t Usted eligio el modo automatico")
		archivo=open ("Automatico.txt","r")
		archivo.read()
		archivo.close()
		fp=open ("Validado.txt","w")
		fp.close()
		revision(2)
def revision(j):
		if j==1:
			archivo= open("Manual.txt","r")
		elif j==2:
			archivo= open("Automatico.txt","r")
		for linea in archivo:
			cadena=linea
			estados(cadena)
		archivo.close()
def estados(cadena):
	ubi=open ("Camino.txt","a")
	palabra=cadena.split()
	ban2=0
	ban1=0
	for i in palabra:
		ban1=0
		ban2=0
		tamaño=len(i)
		estado=0
		c=0
		for a in (i+","):		
			if estado==0:
				ubi.write("q0 -"+a+"-->")
				if a=="0":
					estado=2
				elif a=="1":
					estado=1
				elif tamaño==c :
					if a=="," or a==".":
						if ban2==0:
							ban1=1
							ubi.write("FIN\n")
							guardar(i[0:len(i)])
						else :
							ban1=1
							ubi.write("FIN\n")
							guardar(i[0:len(i)-1])
				elif tamaño==c+1:
					if a=="," or a==".":
						estado=0
						ban2=1	
			elif estado==1:
				ubi.write("q1 -"+a+"-->")
				if a=="0":
					estado=3
				elif a=="1":
					estado=0
			elif estado==2:
				ubi.write("q2 -"+a+"-->")
				if a=="0":
					estado=0
				elif a=="1":
					estado=3
			elif estado==3:
				if a=="0":
					estado=1
				elif a=="1":	
					estado=2
			if ban1==0 and tamaño==c:
				ubi.write("No Valida\n")
			c=c+1	
def guardar(i):
	palabra=i
	valida=open ("Validado.txt","a")
	valida.write(palabra)
	valida.write("\n")
	valida.close()

#automatico()		
manual()