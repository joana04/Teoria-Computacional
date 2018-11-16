#include "Random.h"
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>


void agregarCaracter(int,int,int,int,char []);
int comenzar(int);
void menu(void);
void Manual(void);
void Automatico(void);
void repetitivo(void);

int main()
{
	menu();
	repetitivo();
}

void menu(void){
	system ("color 8F" );
	int rep;
	int opc=0;
	do{
	printf("\t\tUniverso binario 1\n Seleccione la opcion deseada:\n 1.-Manual \n2..-Automatico\n");
		scanf("%d",&opc);
		//opc=Random(1,2);
		if(opc==1){
		Manual();
		}
		if(opc==2){
		Automatico();
		}
		printf("\n\t\tDesea ingresar otro valor? \n 1.-Si \n 2.- No \n");
		scanf("%d",&rep);
		//rep=Random(0,2)
	}while(rep==1);
	printf("\t\tAdios\n");
}

void repetitivo(void){
	int num=0;
	printf("\nQuieres que se repita? \n 1.Si \n 2. No \n");
	num=Random(1,2);
	if(num==1){
		printf("\n Opcion 1 seleccionada\n");
		menu();
	}else{
		printf("\n Opcion 2 seleccionada, Adios\n");
		return ;
	}
}

void Manual(void){
	int potencia=0;
		printf("\t\tSelecciono el modo Manual\n");
		printf("Incerte la potencia  ");
		scanf("%d",&potencia);
		printf("\nLa potencia insertada es: %d",potencia);
		comenzar(potencia);
		}


void Automatico(void){
	int potencia;
		printf("\t\tSelecciono el modo Automatico\n");
		potencia=Random(0,1000);
		printf("La potencia seleccionada automaticamente= %d",potencia);
		comenzar(potencia);
		
		
}

int comenzar(int potencia){
	FILE *archivo;
	char cadena[potencia];
	int senal;
	senal=potencia;
	int cantidad=pow(2,potencia);
	int contador=1;
	int bandera=0;
	archivo=fopen("archivo.txt","w");
	fprintf(archivo,"A={");
	for(int i=0;i<cantidad;i++){
		int posicion=0;
		int bandera=0;
		do{
			if(potencia==0){
				bandera =1;
				
			}
			else{
				if(potencia==1 && contador%2==1){
					cadena[posicion]='0';
				}
				else{
					if(potencia==1 && contador%2==0){
						cadena[posicion]='1';
					}
					else{
							if(contador<=cantidad/2){
								cadena[posicion]='0';
							}
							else{
								cadena[posicion]='1';
								contador=contador-(cantidad/2);		
								}
					}
				}
			}
			
				printf ("bit= %c", cadena[posicion]);
				fprintf(archivo,"%c" ,cadena[posicion]);
			posicion++;
			potencia--;
			
		}while(posicion!=senal && bandera==0);
		
				for(int x=0;x<posicion;x++){
					fprintf(archivo,"%c" ,cadena[x]);
				}
					if(i!=cantidad-1 && i<cantidad){
					fprintf(archivo,",");
					}
					cantidad++;
		}
	fprintf(archivo,"}");
		fclose(archivo);
		return 0;
	}


