from random import *
def combinar(combinaciones,n):
	for x in range(0,n+1):  
		for y in range(0,n+1):
			for z in range(0,n+1):
				if((x+y+z)==n):
					if( (x!=0 and y!=0) or (x!=0 and z!=0) or (z!=0 and y!=0) ):
						combinaciones.append([x,y,z])
	return combinaciones

def listaFinal(combinacion):
	if(combinacion[0]==0 and combinacion[1]==0):
		return 1
	elif(combinacion[0]==0 and combinacion[2]==0):
		return 1
	elif(combinacion[2]==0 and combinacion[1]==0):
		return 1
	else:
		return 0

def repetido(combinacion,historial):
	if(historial==[]):
		return 0
	for casilla in historial:
		if(casilla==combinacion):
			return 1
	return 0

def automata(especies,historial):
	combinacion=especies.copy()
	r=repetido(combinacion.copy(),historial.copy())
	final=listaFinal(combinacion.copy())
	file1=open("No_fallan.txt","a")
	file2=open("Fallan.txt","a")
	if(r==1):
		historial.append(especies.copy())
		file1.write(str(historial)+" No Falla \n")
	elif(final==1):
		historial.append(especies.copy())
		file2.write(str(historial)+" Falla \n")
	else:
		historial.append(combinacion.copy())
		if(combinacion[0]==0):
			combinacion[0]+=2
			combinacion[1]-=1
			combinacion[2]-=1
			automata(combinacion.copy(),historial.copy())
		elif(combinacion[1]==0):
			combinacion[1]+=2
			combinacion[0]-=1
			combinacion[2]-=1
			automata(combinacion.copy(),historial.copy())
		elif(combinacion[2]==0):
			combinacion[2]+=2
			combinacion[1]-=1
			combinacion[0]-=1
			automata(combinacion.copy(),historial.copy())
		else:
			proceso1=combinacion.copy()
			proceso1[2]+=2
			proceso1[1]-=1
			proceso1[0]-=1
			proceso2=combinacion.copy()
			proceso2[1]+=2
			proceso2[0]-=1
			proceso2[2]-=1
			proceso3=combinacion.copy()
			proceso3[0]+=2
			proceso3[1]-=1
			proceso3[2]-=1
			automata(proceso1.copy(),historial.copy())
			automata(proceso2.copy(),historial.copy())
			automata(proceso3.copy(),historial.copy())
	file1.close()
	file2.close()

def menu():
	file1=open("Fallan.txt","w")
	file2=open("No_fallan.txt","w")
	file1.close()
	file2.close()
	entra=1
	while entra==1:
		print("\t\tSeleccione la opcion deseada\n 1.-Manual\n2.-Automatico\n")
		opc=str(input())
		print(opc)
		if opc=='1':
			manual()
		elif opc=='2':
			automatico()
		print("desea regresar?\n1.-Si\,2.-No\n")
		entra=int(input())
	print ("\t\tADIOS\n")

def manual():
	combinaciones=[]
	historial=[]
	print("Ingresa un numero\n")
	numero=int(input())
	combinaciones=combinar(combinaciones,numero)
	for combinacion in combinaciones:
		automata(combinacion,historial)
		historial=[]

def automatico():
	numero=randint(2,15)
	combinaciones=[]
	historial=[]
	print("El numero seleccionado es :"+str(numero))
	combinaciones=combinar(combinaciones,numero)
	for combinacion in combinaciones:
		automata(combinacion,historial)
		historial=[]

menu()