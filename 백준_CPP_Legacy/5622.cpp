#include <iostream>

using namespace std;

int main(){
	string s;	
	int time[28] = {3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 11};
	int sum = 0;
	
	cin >> s;
	
	for(int i=0; i<s.length(); i++){
		sum += time[s[i]-65];
	}
	
	cout << sum << "\n";
	
	return 0;
}
