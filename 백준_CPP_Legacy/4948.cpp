#include <iostream>

using namespace std;

int so[250000];

int main() {
	int n;

	while(true){
		int cnt = 0;
		cin >> n;
		if(n == 0) return 0;
		else {
			for(int i=2; i<=2*n; i++){
				so[i] = i;
			}
			
			for(int i=2; i<=2*n; i++){
				if(so[i] == 0) continue;
				for(int j=i+i; j<=2*n; j+=i){
					so[j] = 0;
				}
			}
			
			for(int i=n+1; i<=2*n; i++){
				if(so[i] != 0) cnt++;
			}
		}
		cout << cnt << "\n";
	}
	
	return 0;
}
