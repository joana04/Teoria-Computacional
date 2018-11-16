import random 
from tkinter import *
def grafico ():
	ventana=Tk()
	g=Canvas(ventana,bg="#FBEFFB",width=800, height=200)
	g.pack()
	ventana.title("Autómata terminación -ere ")
	ventana.geometry("800x200")
	color="#ECCEF5"
	color1="#380B61"
	etiqueta = Label(ventana, bg="#FBEFFB",text="Autómata terminación -ere",fg=color1, font="Harrington")
	g.create_oval(40,50,140,150, fill=color)
	etiqueta1=Label(ventana, bg=color,text="q0",fg=color1, font="Harrington").place(x=79,y=83)
	g.create_oval(240,50,340,150, fill=color)
	etiqueta2=Label(ventana, bg=color,text="q1",fg=color1, font="Harrington").place(x=279,y=83)
	g.create_oval(440,50,540,150, fill=color)
	etiqueta3=Label(ventana, bg=color,text="q2",fg=color1, font="Harrington").place(x=479,y=83)
	g.create_oval(640,50,740,150, fill=color)
	g.create_oval(645,55,735,145, fill=color)
	etiqueta4=Label(ventana, bg=color,text="q3",fg=color1, font="Harrington").place(x=679,y=83)
	color3="#FF0080"
	color4="#F7819F"
	g.create_arc(10,100,40,100, start=0, extent =180, style='arc')
	g.create_oval(35,97.5,40,102.5, fill=color4)
	g.create_arc(129,85,249,54, start=360, extent =180, style='arc')
	g.create_arc(329,85,449,54, start=360, extent =180, style='arc')
	g.create_arc(529,85,649,54, start=360, extent =180, style='arc')
	g.create_arc(532,100,649,154, start=360, extent =-180, style='arc')
	g.create_arc(327,100,655,175, start=360, extent =-180, style='arc')
	g.create_arc(240,90,270,164, start=332, extent =-180, style='arc')
	g.create_oval(246.5,68.5,251.5,73.5, fill=color4)
	g.create_oval(446.5,68.5,451.5,73.5, fill=color4)
	g.create_oval(646.5,68.5,651.5,73.5, fill=color4)
	g.create_oval(237.5,106.5,242.5,111.5, fill=color4)
	g.create_oval(324.5,133.5,329.5,138.5, fill=color4)
	g.create_oval(530.5,125.5,535.5,130.5, fill=color4)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="e",fg=color3, font="Harrington").place(x=579,y=33)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="r",fg=color3, font="Harrington").place(x=379,y=33)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="e",fg=color3, font="Harrington").place(x=179,y=33)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="r",fg=color3, font="Harrington").place(x=579,y=133)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="e",fg=color3, font="Harrington").place(x=479,y=168)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="e",fg=color3, font="Harrington").place(x=250,y=160)
	g.place(x=0,y=0)
	etiqueta.pack()
	g.mainloop() 
def manual():
		cadena=""
		ubi=open ("Camino.txt","w")
		ubi.close()
		Coordenadas=open ("Coordenadas.txt","w")
		Coordenadas.close()
		print ("\t Usted eligio el modo manual\n Ingrese la cadena porfavor")
		cadena=input ()
		archivo=open ("Entrada.txt","w")
		archivo.write(cadena)
		archivo.close()
		fp=open ("Validado.txt","w")
		fp.close()
		revision(1)
def automatico():
		cadena =""
		ubi=open ("Camino.txt","w")
		ubi.close()
		Coordenadas=open ("Coordenadas.txt","w")
		Coordenadas.close()
		print ("\t Usted eligio el modo automatico")
		archivo=open ("Automatico.txt","r")
		archivo.read()
		archivo.close()
		fp=open ("Validado.txt","w")
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
	Coordenadas=open ("Coordenadas.txt","a")
	caracter=0
	palabra=cadena.split()
	x=0
	ban1=0
	for i in palabra:
		ban1=0
		tamaño=len(i)
		estado=0
		c=0
		for a in i:		
			if estado==0:
				ubi.write("q0 -"+a+"-->")
				if a=="e" or a=="E":
					estado=1
				else:
					estado=0	
			elif estado==1:
				ubi.write("q1 -"+a+"-->")
				if a=="r" or a=="R":
					estado=2
				elif a=="e" or a=="E":
					estado=1
				else :
					estado=0
			elif estado==2:
				ubi.write("q2 -"+a+"-->")
				if a=="e" or a=="E":
					estado=3
				else:
					estado=0
			elif estado==3:
				if tamaño==c:
					ubi.write("q3 -"+a+"FIN")
					ban1=1
					guardar(i)
					Coordenadas.write("Ubicacion:" + str(y+1) + "," + str(x+1) + "," + str(caracter-c) + "\n")
				elif tamaño==c+1:
					estado=5
				elif a=="r" or a=="R":
					ubi.write("q3 -"+a +"-->")
					estado=2
				elif a=='e' or a=='E':
					ubi.write("q3 -"+a +"-->")
					estado=1
				else:
					estado=0
			elif estado==5:
				if a=="," or a=="." or a=="?" or a=="!" or a=="}" or a=="]" or a==")" or a=="'" :
					guardar(i[0:len(i)-1])
					ubi.write("q3 -"+a+"FIN")
					ban1=1
					Coordenadas.write("Ubicacion:" + str(y+1) + "," + str(x+1) + "," + str(caracter-c) + "\n")		
			c=c+1
		if estado==3:				
				if tamaño==c:
					ubi.write("q3 -"+a+"FIN")
					ban1=1
					guardar(i)
					Coordenadas.write("Ubicacion:" + str(y+1) + "," + str(x+1) + "," + str(caracter-c) + "\n")
				elif tamaño==c+1:
					estado=5
				else:
					estado=0				
		elif estado==5:
				if a=="," or a=="." or a=="?" or a=="!" or a=="}" or a=="]" or a==")" or a=="'" :
					guardar(i[0:len(i)-1])
					ubi.write("q3 -"+a+"FIN")
					ban1=1
					Coordenadas.write("Ubicacion:" + str(y+1) + "," + str(x+1) + "," + str(caracter-c) + "\n")	
		if ban1==0:
			ubi.write("No Valida\n")
		else:
			ubi.write("\n")
		x=x+1
		caracter=caracter+c
def guardar(i):
	palabra=i
	valida=open ("Validado.txt","a")
	valida.write(palabra)
	valida.write(" ")
	valida.close()
def menu():
	entra=1
	while entra==1:
		print("\t\tSeleccione la opcion deseada\n 1.-Manual\n2.-Automatico\n3.-Grafico\n")
		#opc=str(input())
		opc=str(random.randrange(1,4))
		print(opc)
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