#include "Random.h"
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

int c=0;
int b=0;

void Conversion(int[],int);
int archivarDec(int, int);
void archivarBin(char Numero[], int, int);
void Primos(int);
void Menu();
void Manual();
void Automatico();
int inicializarConjunto(int[]);

int main(int argc, char** argv) {
	system ("color 8F" );
		FILE *fp;
		fp=fopen("archivo.txt","w");
		int rep;
		//Manual();
	
	do{
		rep=0;
		Menu();
		printf ("\t\tDesea ingresar otro valor?\n 1= Si \n 2=No\n");
//		scanf("%d",&rep);
		rep=Random(0,2);
		
	}while(rep==1);
	

	printf ("\t\tGracias Por su Visita \n\t\tAdios");
}

void Menu(void){
	int opc=0;
	printf("\t\t\t\tNUMEROS PRIMOS\t\t\n MENU :\n 1.- Operacion Manual \n 2.-Operacion automatica\n\n");
//	scanf("%d",&opc);
	opc=Random(0,2);
	if(opc+1==1){
		Manual();
	}
	if(opc+1==2){
		Automatico();
	}
}
void Manual(){
	int limite=0;
		printf("Usted selecciono la forma manual\n");
		printf("introduzca el numero de limite=   ");
		scanf("%d",&limite);
		printf ("\n");
		Primos(limite);
}
void Automatico(){
	printf("Usted selecciono la forma automatica\n");
		int limite=0;
		limite=Random(1,750);
		printf("El numero random del limite es=  %d \n ", limite);
		Primos(limite);
	
	
}

void Coma(){
	FILE *fp;
	fp=fopen("archivo.txt","a");
	fprintf(fp,",");
	
}

void Cerrar(){
	FILE *fp;
		b=0;
		fp=fopen("archivo.txt","a");
		fprintf(fp,"}")	;
		fprintf(fp,"\n")	;
}

int archivarDec(int num, int b){
	int x[130];
	int i;
	x[i]=num;
		FILE *fp;
			if (b==0){
			fp=fopen("archivo.txt","a");
			fprintf(fp,"A={");
			fprintf(fp,"%d" ,x[i]);
			}
			if (b>0){
				fprintf(fp,"%d" ,x[i]);
			}	
	i++;
	return 0;	
}

void archivarBin(char Numero[15], int lim, int ban){
	int bit;
	int a;
		a=lim;
	FILE *fp;
	fp=fopen("archivo.txt","a");
	if (ban ==0)fprintf(fp,"Ab={");
	
	for (a=lim-1; a>=0;a--){
		fprintf(fp,"%d",Numero[a]);
	}
}

int inicializarConjunto(int Conjunto[171]){
	int i;
	for (i=0; i<=127; i++){
		Conjunto [i]=0;
	}
}

void Primos(int limite){
	int num;
	int f=0;
	int conjunto[171];
	int i=0;
	int b=0;
	int c=0;
	int a;
	int bandera;
	inicializarConjunto (conjunto);
				if (limite==0){
				FILE *fp;
				fp=fopen("archivo.txt","a");
				fprintf(fp,"A={e}");
				fprintf(fp,"\n");
				fprintf(fp,"Ab={}");
				fprintf(fp,"\n");
			}
	for (num=1; num<=limite; num++){
		bandera=0;
		for(a=2; a<num; a++){
			if (num%a==0){
				bandera=1;
			}
		}	
		if (bandera==0){
				conjunto [i]=num;
				if (f!=0){
				  Coma();
				}
				archivarDec(num,b);
				c=1;
				b=1;
				f=1;
				i++;
		}
			if (num==limite) {
			Cerrar ();
			Conversion(conjunto,i);
		}
	}
	}
	
void Conversion (int conjunto [171], int lim){
	char numero [10];
	int bit;
	int decimal;
	int i=0;
	int h=0;
	int car;
	int ban=0;
do{
	decimal=conjunto[i];
	h=0;
	do{
		bit= decimal%2;
		numero[h]= (char)bit;
		decimal=decimal/2;
		h++;
	} while (decimal>0);
		i++;
		archivarBin (numero,h,ban);
			if (i!=lim) Coma(); 
		ban=1;
}while (i!=lim);
	Cerrar();
	return ;	
}


