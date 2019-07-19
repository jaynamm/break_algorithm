#include <iostream>

using namespace std;

int num[20];

int main(){
	long long k;
	cin >> k;
	int tmp = 0;
	int n=0;
	
	while(k>0){
		tmp = k%10;
		k = k/10;
		num[n] = tmp;
		n++;
	}
	
	int gap = num[0]-num[1];
	
	for(int i=1; i<n; i++){
		if(num[i-1]-num[i] != gap){
			cout << "ÈïÄ©»×!! <(£ş ? £ş)>";	
			return 0;
		}
	}
	
	cout << "?(?????)?..¡Æ¢½ ²î¿ä¹Ì!!";
		
	return 0;
}
