#include <stdlib.h>
#include <time.h>

int Random(int inferior,int superior){
	srand(time(NULL));
	int numero=(rand() % superior) + inferior;
	return numero;
}
