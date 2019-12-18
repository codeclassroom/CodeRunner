#include<stdio.h>

int main(){
	int F1 = 0, F2 = 1, F3, n = 15;
	if(n == 2) printf ("%d %d ", F1, F2);
	else{
		printf("%d %d", F1, F2);
		do{
			F3 = F1 + F2;
			printf("%d ", F3);
			F1 = F2;
			F2 = F3;
			n--;
		}while(n > 2);
	}
	return 0;
}
