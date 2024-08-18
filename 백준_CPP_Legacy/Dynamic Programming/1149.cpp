#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

long RGB[3][1001];

int main(){
	cin.tie(0);
	int n;
	cin >> n;
	
	for(int i=0; i<n; i++) cin >> RGB[0][i] >> RGB[1][i] >> RGB[2][i];
	
	for(int i=1; i<n; i++){
		RGB[0][i] += min(RGB[1][i-1], RGB[2][i-1]);
		RGB[1][i] += min(RGB[0][i-1], RGB[2][i-1]);
		RGB[2][i] += min(RGB[0][i-1], RGB[1][i-1]);
	}
	
	cout << min(RGB[0][n-1], min(RGB[1][n-1], RGB[2][n-1]));
	
	return 0;
}
