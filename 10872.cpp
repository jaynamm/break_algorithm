#include <iostream>

using namespace std;

int res = 1;

void factorial(int n){
	if(n==0){
		cout << res << "\n";
	} else {
		res *= n;
		factorial(n-1);	
	}
	
}

int main(){
	int n;
	cin >> n;
	
	factorial(n);
	
	return 0;
}
