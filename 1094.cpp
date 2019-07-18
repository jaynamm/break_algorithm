#include <iostream>

using namespace std;

int main() {
	int x;
	int m[8] = {64, 32, 16, 8, 4, 2, 1};
	int cnt = 0;
	cin >> x;
	
	for(int i=0; i<8; i++){
		if(m[i] <= x && x != 0){
			cnt++;
			x -= m[i];
		}
	} 
	
	cout << cnt;
	
	return 0;
}
