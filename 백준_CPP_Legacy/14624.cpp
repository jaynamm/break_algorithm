#include <iostream>

using namespace std;

int main() {
	cin.tie(0);
	
	int n;
	cin >> n;
	
	if(n % 2 == 0) {
		cout << "I LOVE CBNU\n";
	} else {
		for(int i=0; i<n; i++){
			cout << "*";
		}
		cout << "\n";
		
		for(int i=0; i<=n/2; i++) {
			for(int j=0; j<n; j++) {
				if(i == 0) {
					if(j == n/2-i) {
						cout << "*";
						break;
					} else {
						cout << " ";
					}
				} else {
					if(j == n/2-i) {
						cout << "*";
					} else if(j == n/2+i) {
						cout << "*";
						break;
					} else {
						cout << " ";
					}
				}
			}
			if(i != n/2) cout << "\n";		
		}
	}

	return 0;
}
