#include <iostream>

using namespace std;

int main(){

	int a;
	int b = 42;
	int rest[10] = {0};
	int sum = 0;
	
	for(int i=0; i<10; i++){
		cin >> a;
		rest[i] = a%b;
		for(int j=0; j<=i; j++){
			if(rest[i] == rest[j] && i != j){
				sum --;
				break;
			}
		}
		sum++;
	}
		
	cout << sum << "\n";
		
	return 0;
}
