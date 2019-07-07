#include <iostream>

using namespace std;

int main(){
	int n, m;
	int max = 0;
	int sum = 0;
	
	cin >> n >> m;
	
	int num[n+1];
	
	for(int i=0; i<n; i++){
		cin >> num[i];
	}
	
	for(int i=0; i<n; i++){
		for(int j=i+1; j<n; j++){
			for(int k=j+1; k<n; k++){
				sum = num[i] + num[j] + num[k];
				if(sum > max && sum <= m) max = sum;
			}
		}
	}
	
	cout << max << "\n";
	
	return 0;
}
