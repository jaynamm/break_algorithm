#include <iostream>

using namespace std;

int main(){
	
	int n;
	int cnt = 0;
	int n1=0, n2=0;
	
	cin >> n;
	
	if(n < 100) {
		cout << n;
		
	} else{
		for(int i=100; i<=n; i++){
			n1 = (i/100) - ((i%100)/10);
			n2 = (i%100)/10 - i%10;
			if(n1 == n2) {
				cnt++;	
			}
		}
		cout << (cnt + 99);
	}
	
	return 0;
}
