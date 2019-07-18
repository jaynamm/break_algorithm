#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int m, n;
	cin >> m >> n;
	
	int so[10001];
	
	for(int i=2; i<=n; i++){
		so[i] = i;
	}
	
	for(int i=2; i<=n; i++){
		if(so[i] == 0) continue;
		for(int j=i+i; j<=n; j+=i){
			so[j] = 0;
		}
	}
	
	int sum = 0;
	int min = 10001;
	
	for(int i=m; i<=n; i++){
		if(so[i] != 0) {
			sum += so[i];
			if(so[i] <= min) min = so[i];
		}
	}
	
	if(sum == 0) cout << "-1";
	else cout << sum << "\n" << min;
	
	return 0;
}
