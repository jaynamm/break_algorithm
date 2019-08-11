#include <iostream>
#include <cmath>

using namespace std;

int main(){
	cin.tie(0);
	int n;
	cin>>n;
	
	int s[100001];
	int e[100001];
	
	int min = 100001;
	int max = 0;
	int time = 0;
	
	for(int i=0; i<n; i++){
		cin >> s[i] >> e[i];
		
		if(e[i] < min) min = e[i];
		if(s[i] > max) max = s[i];
	}	
	
	int gap = max-min;
	
	if(gap < 0) time = 0;
	else time = gap;
	
	cout << time;

	return 0;
}
