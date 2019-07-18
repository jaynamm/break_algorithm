#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int n, num, cnt=0;
	cin >> n;
	
	int so[1001];
	
	for(int i=2; i<=1000; i++){
		so[i] = i;
	}
	
	for(int i=2; i<=1000; i++){
		if(so[i] == 0) continue;
		for(int j=i+i; j<=1000; j+=i){
			so[j] = 0;
		}
	}
	
	for(int i=0; i<n; i++){
		cin >> num;
		for(int j=2; j<=1000; j++){
			if(so[j] == num) cnt++;
		}		
	}
	
	cout << cnt;

	return 0;
}
