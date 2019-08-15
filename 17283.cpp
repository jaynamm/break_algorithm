#include <iostream>

using namespace std;

int main(){
	cin.tie(0);
	int l, r;
	cin >> l >> r;
	
	int n=l, sum=0, t=2;
	
	while(true){
		n*=(double)r/100;
		if(n<=5) break;
		sum+=t*n;
		t*=2;
	}
		
	cout << sum << "\n";
	
	return 0;
}
