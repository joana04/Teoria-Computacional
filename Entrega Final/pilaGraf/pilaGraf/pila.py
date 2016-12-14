import claspila
import random
from time import *
from tkinter import *
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
	l=int (random.randrange(5,20))
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
	y=0
	for linea in archivo:
		cadena=linea
		estados(cadena,y)
		y=y+1
	archivo.close()
def eliminar(cadena):
	x=1
	cad=""
	while(x<len(cadena)):
		cad+=cadena[x]
		x+=1
	return cad
def estados(cadena,y):
	root = 	Tk()
	canvas=Canvas(root,width=450,height=450)
	canvas.pack()
	ubi=open ("Camino.txt","a")
	caracter=0
	palabra=cadena.split()
	x=0
	for i in palabra:
		eliminacion=palabra[0]
		ban=0
		pila=claspila.Pila()
		pila.inicializar()
		cad="".join(pila.lista)
		print('Inicio |-' +cad) 
		print ('\n')
		ubi.write("------"+i+"------\n")
		ubi.write("Inicio  |-")
		ubi.write("".join(pila.lista))
		ubi.write("\n")
		canvas.create_line(175,150,175,50)
		canvas.create_line(175,300,175,400)
		estado=Label(root,text="                                                                      ",font=("Arial",12))
		estado.place(x = 170, y = 35)
		estado=Label(root,text=eliminacion,font=("Arial",12))
		estado.place(x = 170, y = 35)
		estado=Label(root,text="                                                                      ",font=("Arial",12))
		estado.place(x = 170, y = 400)
		estado=Label(root,text=str(pila.lista),font=("Arial",12))
		estado.place(x = 170, y = 400)
		estado=Label(root,text=" p "+"  ",font=("Arial",50),fg="black")
		estado.place(x = 150, y = 180)
		sleep(1)
		root.update()
		for a in (i+","):	
			if a=='0':
				pila.push()
				canvas.create_line(175,150,175,50)
				canvas.create_line(175,300,175,400)
				estado=Label(root,text="                                                                      ",font=("Arial",12))
				estado.place(x = 170, y = 35)
				print(eliminacion)
				eliminacion=eliminar(eliminacion)
				print(eliminacion)
				estado=Label(root,text=eliminacion,font=("Arial",12))
				estado.place(x = 170, y = 35)
				estado=Label(root,text="                                                                      ",font=("Arial",12))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=str(pila.lista),font=("Arial",12))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=" p "+"  ",font=("Arial",50),fg="black")
				estado.place(x = 150, y = 180)
				sleep(1)
				root.update()
				cad="".join(pila.lista)
				print ('|-'+cad)
				print ('\n')
				ubi.write("|-")
				ubi.write("".join(pila.lista))
				ubi.write("\n")
			elif a=='1' and pila.tope>1:
				pila.pop()
				canvas.create_line(175,150,175,50)
				canvas.create_line(175,300,175,400)
				estado=Label(root,text="                                                                      ",font=("Arial",12))
				estado.place(x = 170, y = 35)
				eliminacion=eliminar(eliminacion)
				estado=Label(root,text=eliminacion,font=("Arial",12))
				estado.place(x = 170, y = 35)
				estado=Label(root,text="                                                                      ",font=("Arial",12))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=str(pila.lista),font=("Arial",12))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=" q "+"  ",font=("Arial",50),fg="black")
				estado.place(x = 150, y = 180)
				sleep(1)
				root.update()
				cad="".join(pila.lista)
				print ('|-'+cad)
				print ('\n')
				ubi.write("|-")
				ubi.write("".join(pila.lista))
				ubi.write("\n")
			elif a==',' and pila.lista[0]=='Z0' and ban==0:
				print ("---Cadena Valida---")
				ubi.write("---Cadena Valida------------\n")
				guardar(i)
				canvas.create_line(175,150,175,50)
				canvas.create_line(175,300,175,400)
				estado=Label(root,text="                                                                      ",font=("Arial",12))
				estado.place(x = 170, y = 35)
				eliminacion=eliminar(eliminacion)
				estado=Label(root,text=eliminacion,font=("Arial",12))
				estado.place(x = 170, y = 35)
				estado=Label(root,text="                                                                      ",font=("Arial",12))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=str(pila.lista),font=("Arial",12))
				estado.place(x = 170, y = 400)
				estado=Label(root,text=" f "+"  ",font=("Arial",50),fg="black")
				estado.place(x = 150, y = 180)
				sleep(1)
				root.update()
			else:
				ban=1
				print ("---Cadena NO Valida---")
				ubi.write("----Cadena NO Valida----\n")
	root.mainloop()

def guardar(i):
	valida=open ("Validado.txt","a")
	valida.write(i)
	valida.write(" \n")
	valida.close()
menu()