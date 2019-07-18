#include <iostream>

using namespace std;

int main() {
	double s;
	cin.tie(0);
	cin >> s;
	
	double sum = 0;
	int cnt = 0;
	
	for(int i=1; sum<=s; i++){
		sum += i;
		cnt++;
		if(sum > s){
			cnt--;
			break;
		}	
	}
	
	cout << cnt;
	
	return 0;
}
