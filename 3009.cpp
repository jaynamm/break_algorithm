#include <iostream>

using namespace std;

int main() {
	int x[4], y[4];
	int xr, yr;
	
	for(int i=0; i<3; i++){
		cin >> x[i] >> y[i];
	}
	
	if(x[0] == x[1] && x[0] != x[2]) xr = x[2];
	else if(x[1] == x[2] && x[1] != x[0]) xr = x[0];
	else if(x[2] == x[0] && x[2] != x[1]) xr = x[1];
	
	if(y[0] == y[1] && y[0] != y[2]) yr = y[2];
	else if(y[1] == y[2] && y[1] != y[0]) yr = y[0];
	else if(y[2] == y[0] && y[2] != y[1]) yr = y[1];
	
	cout << xr << " " << yr;
	
	return 0;
}
