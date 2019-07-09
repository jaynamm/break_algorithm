#include <iostream>

using namespace std;

int gcd(int a, int b){
	int n;

	while(b!=0){
		n=a%b;
		a=b;
		b=n;
	}
	
	return a;
}

int main(){
	int r, g, n;
	
	cin >> r >> g;
	
	n = gcd(r, g);
	
	for(int i=1; i<=n; i++){
		if(n%i == 0){
			cout << i << " " << r/i << " " << g/i << "\n";
		}
	}
	
	return 0;
}
