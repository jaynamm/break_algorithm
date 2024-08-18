#include <iostream>
#include <cmath>

using namespace std;

int main(){
	int n;
	int cnt = 0;
	cin >> n;
	
	int x[n+1];
	int y[n+1];
	int s[n+1];
	
	for(int i=0; i<n; i++){
		cin >> x[i] >> y[i];
	}
	
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			if(i != j){
				if(x[i] < x[j] && y[i] < y[j]){
					cnt++;
				}
			}
		}
		s[i] = 1+cnt;
		cnt = 0;
	}
	
	for(int i=0; i<n; i++){
		cout << s[i] << " ";
	}
	
	return 0;
}
