#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int n[9];
	int sum = 0;
	int res = 0;
	
	for(int i=0; i<9; i++){
		cin >> n[i];
		sum += n[i];
	}
	
	for(int i=0; i<9; i++){
		for(int j=i+1; j<9; j++){
			res = sum - n[i] - n[j];
			if(res == 100){
				n[i] = 0;
				n[j] = 0;
				break;
			}
		}
		if(res == 100){
			break;
		}
	}
	
	sort(n, n+9);
	
	for(int i=0; i<9; i++){
		if(n[i] != 0){
			cout << n[i] << "\n";
		}
	}
	
	return 0;
}
