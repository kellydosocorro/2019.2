#include<iostream>
using namespace std;

typedef struct Ponto {
	int x;
	int y;	
}ponto;

typedef struct Reta {
	ponto P1;
	ponto P2;
	float m;	
}reta;

main() {
	
	reta Exemplo;
	
	Exemplo.P1.x = 0;
	Exemplo.P1.y = 3;
	
	Exemplo.P2.x = 3;
	Exemplo.P2.y = 9;
	
	

}

