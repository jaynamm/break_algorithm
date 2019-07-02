#include <iostream>

using namespace std;

int main(){
	int n;
	cin >>n;
	double score[n+1];
	int m = 0;
	
	for(int i=0; i<n; i++){
		cin >> score[i];
		if(m < score[i]) {
			m = score[i];
		}
	}
	
	double res[n+1];
	double sum = 0;
	
	for(int i=0; i<n; i++){
		res[i] = score[i]/m*100;
		sum += res[i];
	}
	
	cout << sum/n << "\n";
	
	return 0;
}
