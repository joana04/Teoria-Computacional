import random 
from tkinter import *
def grafico():
	ventana=Tk()
	g=Canvas(ventana,bg="#FBEFFB",width=500, height=500)
	g.pack()
	ventana.title("Autómata de Paridad ")
	ventana.geometry("400x400")
	color="#ECCEF5"
	color1="#380B61"
	etiqueta = Label(ventana, bg="#FBEFFB",text="Autómata de Paridad",fg=color1, font="Harrington")
	g.create_oval(40,50,140,150, fill=color)
	g.create_oval(45,55,135,145, fill=color)
	etiqueta1=Label(ventana, bg=color,text="q0",fg=color1, font="Harrington").place(x=79,y=83)
	g.create_oval(240,50,340,150, fill=color)
	etiqueta2=Label(ventana, bg=color,text="q1",fg=color1, font="Harrington").place(x=279,y=83)
	g.create_oval(240,250,340,350, fill=color)
	etiqueta3=Label(ventana, bg=color,text="q2",fg=color1, font="Harrington").place(x=79,y=283)
	g.create_oval(40,250,140,350, fill=color)
	etiqueta4=Label(ventana, bg=color,text="q3",fg=color1, font="Harrington").place(x=279,y=283)
	color3="#FF0080"
	color4="#F7819F"
	g.create_arc(10,100,40,100, start=0, extent =180, style='arc')
	g.create_oval(35,97.5,40,102.5, fill=color4)
	g.create_arc(129,85,249,54, start=360, extent =180, style='arc')#arriba
	g.create_arc(129,115,249,146, start=360, extent =-180, style='arc')#abajo
	g.create_arc(240,132,270,265, start=90, extent =180, style='arc')#izquierda
	g.create_arc(310,132,340,265, start=90, extent =-180, style='arc')#derecha
	g.create_arc(129,286,249,255, start=360, extent =180, style='arc')#arriba2
	g.create_arc(129,316,251,347, start=360, extent =-180, style='arc')#abajo2
	g.create_arc(45,132,65,265, start=90, extent =180, style='arc')#izquierda
	g.create_arc(115,132,135,265, start=90, extent =-180, style='arc')#derecha
	g.create_oval(246.5,68.5,251.5,73.5, fill=color4)
	g.create_oval(127,128.5,132,133.5, fill=color4)
	g.create_oval(325.5,262.5,330.5,267.5, fill=color4)
	g.create_oval(251.5,131.5,256.5,136.5, fill=color4)
	g.create_oval(246.5,268.5,251.5,273.5, fill=color4)
	g.create_oval(127,329.5,132,334.5, fill=color4)
	g.create_oval(51.5,261.5,57.5,266.5, fill=color4)
	g.create_oval(123.5,131.5,128.5,136.5, fill=color4)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="1",fg=color3, font="Harrington").place(x=179,y=38)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="1",fg=color3, font="Harrington").place(x=179,y=133)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="0",fg=color3, font="Harrington").place(x=232,y=190)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="0",fg=color3, font="Harrington").place(x=332,y=193)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="0",fg=color3, font="Harrington").place(x=179,y=238)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="0",fg=color3, font="Harrington").place(x=179,y=333)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="1",fg=color3, font="Harrington").place(x=40,y=185)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="1",fg=color3, font="Harrington").place(x=130,y=185)
	g.place(x=0,y=0)
	etiqueta.pack()
	g.mainloop() 
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
def menu():
	entra=1
	while entra==1:
		print("\t\tSeleccione la opcion deseada\n 1.-Manual\n2.-Automatico\n3.-Grafico\n")
		#opc=str(input())
		opc=str(random.randrange(1,4))
		if opc=='1':
			manual()
		elif opc=='2':
			automatico()
		elif opc=='3':
			print("\t\tFue seleccionado el modo Grafico\n")
			grafico()
		print("desea regresar?\n1.-Si\,2.-No\n")
			#entra=int(input())
		entra=random.randrange(0,2)
	print ("\t\tADIOS\n")

menu()