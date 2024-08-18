#include <iostream>

using namespace std;

int so[1000001];

int main() {
	int m, n;
	cin >> m >> n;
	
	for(int i=2; i<=n; i++){
		so[i] = i;
	}
	
	for(int i=2; i<=n; i++){
		if(so[i] == 0) continue;
		for(int j=i+i; j<=n; j+=i){
			so[j] = 0;
		}
	}
	
	for(int i=m; i<=n; i++){
		if(so[i] != 0) cout << so[i] << "\n";			
	}
	
	return 0;
}
