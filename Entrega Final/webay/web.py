from tkinter import *
def grafico():
	root = 	Tk()
	root.title('Grafico')
	p=Canvas(root,width=1000,height=700)
	p.pack()
	p.create_line(140,325,250,200)
	p.create_line(140,375,250,500)
	p.create_line(350,200,650,200)
	p.create_line(350,500,850,500)
	p.create_line(100,10,100,690)
	p.create_line(700,10,700,690)
	p.create_line(100,10,700,10)
	p.create_line(100,690,900,690)
	p.create_line(100,50,500,50)
	p.create_line(100,100,300,100)
	p.create_line(320,100,670,100)
	p.create_line(300,100,300,650)
	p.create_line(320,100,320,200)
	p.create_line(100,650,300,650)
	p.create_line(500,50,500,150)
	p.create_line(500,550,500,700)
	p.create_line(100,675,500,675)
	p.create_line(470,100,470,200)
	p.create_line(670,100,670,300)
	p.create_line(900,690,900,350)
	p.create_line(880,640,880,530)
	p.create_line(330,640,330,530)
	p.create_line(530,640,530,350)
	p.create_line(730,640,730,350)
	p.create_line(330,640,880,640)
	p.create_line(300,350,900,350)
	p.create_line(320,300,670,300)
	p.create_line(320,300,320,500)
	p.create_line(520,180,520,300)
	p.create_oval(50, 300, 150, 400,fill="pink")
	p.create_oval(250, 150, 350, 250,fill="pink")
	p.create_oval(450, 150, 550, 250,fill="pink")
	p.create_oval(650, 150, 750, 250,fill="pink")
	p.create_oval(250, 450, 350, 550,fill="pink")
	p.create_oval(450, 450, 550, 550,fill="pink")
	p.create_oval(650, 450, 750, 550,fill="pink")
	p.create_oval(850, 450, 950, 550,fill="pink")
	p.create_oval(95, 95, 105, 105,fill="black")
	p.create_oval(95, 45, 105, 55,fill="black")
	p.create_oval(95, 5, 105, 15,fill="black")
	p.create_oval(95, 290, 105, 300,fill="black")
	p.create_oval(95, 400, 105, 410,fill="black")
	p.create_oval(95, 645, 105, 655,fill="black")
	p.create_oval(95, 670, 105, 680,fill="black")
	p.create_oval(95, 685, 105, 695,fill="black")
	p.create_oval(695, 685, 705, 695,fill="black")
	p.create_oval(725, 645, 735, 635,fill="black")
	p.create_oval(725, 355, 735, 345,fill="black")
	p.create_oval(525, 645, 535, 635,fill="black")
	p.create_oval(525, 355, 535, 345,fill="black")
	p.create_oval(325, 550, 335, 540,fill="black")
	p.create_oval(295, 355, 305, 345,fill="black")
	p.create_oval(295, 260, 305, 250,fill="black")
	p.create_oval(315, 155, 325, 145,fill="black")
	p.create_oval(475, 95, 465, 105,fill="black")
	p.create_oval(675, 95, 665, 105,fill="black")
	p.create_oval(440, 195, 450, 205,fill="black")
	p.create_oval(640, 195, 650, 205,fill="black")
	p.create_oval(240, 195, 250, 205,fill="black")
	p.create_oval(440, 495, 450, 505,fill="black")
	p.create_oval(640, 495, 650, 505,fill="black")
	p.create_oval(240, 495, 250, 505,fill="black")
	p.create_oval(840, 495, 850, 505,fill="black")
	p.create_oval(515, 305, 525, 295,fill="black")
	p.create_oval(315, 455, 325, 445,fill="black")
	l=Label(root,text="w")
	l.place(x=200,y=260)
	l=Label(root,text="e")
	l.place(x=400,y=180)
	l=Label(root,text="b")
	l.place(x=600,y=180)
	l=Label(root,text="y")
	l.place(x=800,y=480)
	l=Label(root,text="a")
	l.place(x=600,y=480)
	l=Label(root,text="b")
	l.place(x=400,y=480)
	l=Label(root,text="e")
	l.place(x=200,y=420)
	l=Label(root,text="w")
	l.place(x=300,y=300)
	l=Label(root,text="w")
	l.place(x=400,y=340)
	l=Label(root,text="w")
	l.place(x=600,y=340)
	l=Label(root,text="w")
	l.place(x=800,y=340)
	l=Label(root,text="e")
	l.place(x=400,y=640)
	l=Label(root,text="e")
	l.place(x=600,y=640)
	l=Label(root,text="e")
	l.place(x=800,y=640)
	l=Label(root,text="w")
	l.place(x=400,y=100)
	l=Label(root,text="w")
	l.place(x=600,y=100)
	l=Label(root,text="-a-e-w")
	l.place(x=600,y=15)
	l=Label(root,text="-b-e-w")
	l.place(x=400,y=30)
	l=Label(root,text="-e-w")
	l.place(x=200,y=90)
	l=Label(root,text="-b-e-w")
	l.place(x=200,y=620)
	l=Label(root,text="-a-e-w")
	l.place(x=400,y=665)
	l=Label(root,text="-a-y-w")
	l.place(x=600,y=675)
	l=Label(root,text="-e-w")
	l.place(x=800,y=675)
	l=Label(root,text="e")
	l.place(x=420,y=290)
	l=Label(root,text="e")
	l.place(x=620,y=290)
	l=Label(root,text="q0",bg="pink")
	l.place(x=90,y=330)
	l=Label(root,text="q1",bg="pink")
	l.place(x=290,y=180)
	l=Label(root,text="q2",bg="pink")
	l.place(x=490,y=180)
	l=Label(root,text="q3",bg="pink")
	l.place(x=690,y=180)
	l=Label(root,text="q4",bg="pink")
	l.place(x=290,y=480)
	l=Label(root,text="q5",bg="pink")
	l.place(x=490,y=480)
	l=Label(root,text="q6",bg="pink")
	l.place(x=690,y=480)
	l=Label(root,text="q7",bg="pink")
	l.place(x=890,y=480)
	l=Label(root,text="w")
	l.pack()
	l.place(x=0,y=0)
	root.mainloop()

def manual():
		cadena=""
		ubi=open ("Camino.txt","w")
		ubi.close()
		Coordenadas=open ("Coordenadas.txt","w")
		Coordenadas.close()
		print ("\t Usted eligio el modo manual\n Ingrese el texto porfavor")
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
			archivo= open("Manual.txt","r")
		elif j==2:
			archivo= open("Automatico.txt","r")
		y=0
		for linea in archivo:
			cadena=linea
			estados(cadena, y)
			y=y+1
		archivo.close()
def estados(cadena, y):
	ubi=open ("Camino.txt","a")
	Coordenadas=open ("Coordenadas.txt","a")
	caracter=0
	x=0
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
				if a=="e" or a=="E":
					estado=4
				elif a=="w" or a=="W":
					estado=1
				else :
					estado=0	
			elif estado==1:
				ubi.write("q1 -"+a+"-->")
				if a=="e" or a=="E":
					estado=2
				elif a=="w" or a=="W":
					estado=1
				else:
					estado=0
			elif estado==2:
				ubi.write("q2 -"+a+"-->")
				if a=="e" or a=="E":
					estado=4
				elif a=="b" or a=="B":
					estado=3
				else :
					estado=0
			elif estado==3:
				guardar(i)
				ubi.write("q3-"+a+"-->FIN Valida\n")
				ban1=1
				if a=="a" or a=="A":
					estado=6
				elif a=="w" or a=="W":
					estao=1
				elif a=="e" or a =="E":
					estado=4
				else:
					estado=0
			elif estado==4:
				ubi.write("q4 --->")
				if a=="e" or a=="E":
					estado=4
				elif a=="w" or a=="W":
					estado=1
				elif a=="b" or a=="B":
					estado=5
				else:
					estado=0
			elif estado==5:
				ubi.write("q5 -"+a+"-->")
				if a=="e" or a=="E":
					estado=4
				elif a=="w" or a=="W":
					estado=1
				elif a=="a" or a=="A":
					estado=6
				else:
					estado=0
			elif estado==6:
				ubi.write("q6 -"+a+"-->")
				if a=="e" or a=="E":
					estado=4
				elif a=="w" or a=="W":
					estado=1
				elif a=="y" or a=="Y":
					estado=7
				else:
					estado=0
			elif estado==7:
				ubi.write("q7 --->FIN Valida\n")
				if a=="e" or a=="E":
					estado=4
				elif a=="w" or a=="W":
					estado=1
				else:
					estado=0
				if ban1==0:
					guardar (i)
					ban1=1
			
		x=x+1
		if ban1==1:
			Coordenadas.write("Ubicacion:" + str(y+1) + "," + str(x) +  "\n")	
		elif ban1==0:
			ubi.write("No Valida\n")
				
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
		opc=str(input())
		#opc=str(random.randrange(1,4))
		if opc=='1':
			manual()
		elif opc=='2':
			automatico()
		elif opc=='3':
			print("\t\tFue seleccionado el modo Grafico\n")
			grafico()
		print("desea regresar?\n1.-Si\,2.-No\n")
		entra=int(input())
		#entra=random.randrange(0,2)
	print ("\t\tADIOS\n")

menu()