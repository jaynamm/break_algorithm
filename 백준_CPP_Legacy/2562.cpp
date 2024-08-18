#include <iostream>

using namespace std;

int main(){
	
	int num[10];
	int max = 0;
	int flag = 0;
	
	for(int i=1; i<=9; i++){
		cin >> num[i];
		
		if(num[i] > max) {
			max = num[i];
			flag = i;	
		}
	}
	
	cout << max << "\n" << flag << "\n";
	
	return 0;
}
