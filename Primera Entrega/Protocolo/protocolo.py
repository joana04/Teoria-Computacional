import random 
import time
from tkinter import *
def grafico(encendido):
	ventana=Tk()
	g=Canvas(ventana,bg="#FBEFFB",width=600, height=600)
	g.pack()
	ventana.title("Protocolo")
	ventana.geometry("600x400")
	color="#ECCEF5"
	color1="#380B61"
	etiqueta = Label(ventana, bg="#FBEFFB",text="Protocolo",fg=color1, font="Harrington")
	g.create_oval(40,100,140,200, fill=color)
	g.create_oval(45,105,135,195, fill=color)
	etiqueta1=Label(ventana, bg=color,text="Ready",fg=color1, font="Harrington").place(x=59,y=135)
	g.create_oval(440,100,540,200, fill=color)
	etiqueta2=Label(ventana, bg=color,text="Sending",fg=color1, font="Harrington").place(x=459,y=135)
	color3="#FF0080"
	color4="#F7819F"
	g.create_arc(10,150,40,150, start=0, extent =180, style='arc')
	g.create_oval(35,147.5,40,152.5, fill=color4)
	g.create_arc(129,158,449,80, start=360, extent =180, style='arc')#arriba
	g.create_arc(127,146,453,223, start=360, extent =-180, style='arc')#abajo2
	g.create_oval(446.5,118.5,451.5,123.5, fill=color4)
	g.create_oval(122.5,188.5,127.5,183.5, fill=color4)
	g.create_oval(360,216.5,365,221.5, fill=color4)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="data in",fg=color3, font="Harrington").place(x=190,y=38)
	etiqueta4=Label(ventana, bg="#FBEFFB",text="ack",fg=color3, font="Harrington").place(x=180,y=223)
	if encendido==1:
		g.create_oval(269,60,309,100, fill="#FF0040")
	elif encendido==0:
		g.create_oval(269,60,309,100, fill="#FBEFFB")
	g.create_rectangle(280,200,360,284, fill="#2F0B3A")
	etiqueta4=Label(ventana, bg="#2F0B3A",text="Autómata ",fg="#F5A9F2", font="Harrington").place(x=283,y=214)
	etiqueta4=Label(ventana, bg="#2F0B3A",text="Paridad ",fg="#F5A9F2", font="Harrington").place(x=290,y=234)
	g.place(x=0,y=0)
	etiqueta.pack()
	g.mainloop() 
def creacion():
	archivo=open ("Automatico.txt","w")
	for a in range (50):
		cadena=""
		for i in range(32):
			cadena+=str(random.randrange(0,2))
		archivo.write(str(a)+".-"+cadena+"\n")
def revision():
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
					ban1=1
					ubi.write("FIN\n")
					guardar(i)
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
	archivo=open ("Automatico.txt","w")
	encendido=1
	while encendido==1:
		encendido=random.randrange(0,2)
		camprot=open ("camprot.txt","a")
		if encendido==1:
			grafico(1)
			print ("\t\tEncendido\n")
			camprot.write("Encendido -> ")
			creacion()
			camprot.write("Creacion -> ")
			ubi=open ("Camino.txt","w")
			ubi.close()
			fp=open ("Validado.txt","w")
			fp.close()
			archivo=open ("Automatico.txt","r")
			archivo.read()
			archivo.close()
			print ("\t\tRevision en curso\n")
			camprot.write("Revision -> Fin\n ")
			time.sleep(2)
			revision()
		else:
			grafico(0)
			camprot.write("No encendido \n ")
			print ("\t\tNo esta encendido\n")
		encendido=random.randrange(0,2)
	print ("\t\tYa no esta encendido\n")
	camprot.write("Ya no esta encendido \n ")


menu()





