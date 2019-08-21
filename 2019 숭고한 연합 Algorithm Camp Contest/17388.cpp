#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
	int s, k, h;
	cin >> s >> k >> h;
	
	int sum = s + k + h;
	
	if(sum >= 100) cout << "OK\n";
	else {
		int mincol = min(s, min(k, h));
		
		if(mincol == s) cout << "Soongsil\n";
		if(mincol == k) cout << "Korea\n";
		if(mincol == h) cout << "Hanyang\n";
	}
	
	return 0;
}
