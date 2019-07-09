#include <iostream>

using namespace std;

int main(){
	string num;
	string res[2];
	
	for(int i=0; i<2; i++){
		cin >> num;
		
		int tmp;
		
		tmp = num[0];
		num[0] = num[2];
		num[2] = tmp;
		
		res[i] = num;
	}
	
	if(res[0] > res[1]){
		cout << res[0] << "\n";
	} else {
		cout << res[1] << "\n";
	}
	
	return 0;
}
