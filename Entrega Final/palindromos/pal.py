import random 
def menu():
	entra=1
	fp=open("Palindromo.txt","w")
	fp.close()
	ubi=open ("Camino.txt","w")
	ubi.close()
	while entra==1:
		ubi=open ("Camino.txt","a")
		ubi.close()
		fp=open ("Palindromo.txt","a")
		fp.close()
		print("\n\t\tSeleccione la opcion deseada\n 1.-Manual\n 2.-Automatico\n")
		opc=str(input())
		#opc=str(random.randrange(1,3))
		if opc=='1':
			manual()
		elif opc=='2':
			automatico()
		print("\n\nDesea regresar?\n1.-Si\,2.-No\n")
		entra=int(input())
		#entra=random.randrange(0,2)
	print ("\t\tADIOS\n")
def manual():
	print ("\n\t Usted eligio el modo manual\n Ingrese la longitud del palindromo\n")
	long =int (input ())
	creacion(long)
def automatico():
	print ("\n\t Usted eligio el modo automatico\n ")
	long =int (random.randint(1,1000))
	print (" La longitud del palindromo es: "+str(long))
	creacion(long)
def creacion (long):
	ubi=open ("Camino.txt","a")
	ubi.write('long= '+ str(long)+' --> ')
	derecha=''
	izquierda=''
	palabra=''
	bandera=0
	if (long %2 )!=0:
		repeticiones=int((long-1)/2)
		bandera=1
	else :
		repeticiones=int(long/2)
	for a in range (repeticiones):
		sel=random.randrange(0,2)
		if sel==0:
			derecha='0'+derecha
			izquierda=izquierda+'0'
			ubi.write(' 0 --> ')
		if sel==1:
			derecha='1'+derecha
			izquierda=izquierda+'1'
			ubi.write(' 1 --> ')
	if bandera==1:
		med=random.randrange(0,2)
		if med==0:
			palabra=derecha+'0'+izquierda
			ubi.write(' P --> 0 ')
			ubi.write('\n')
		if med==1:
			palabra=derecha+'1'+izquierda
			ubi.write(' P --> 1 ')
			ubi.write('\n')
	else:
		palabra=derecha+izquierda
		ubi.write(' P --> e ')
		ubi.write('\n')

	primero=derecha+'(P)'+izquierda
	guardar(palabra, primero, long)

def guardar(palabra, primero, long):
	fp=open ("palindromo.txt","a")
	fp.write('long= '+ str(long)+' --> ')
	fp.write(primero+' --> ')
	fp.write(palabra)
	fp.write("\n")
	fp.close()
menu()

