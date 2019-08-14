#include <iostream>

using namespace std;

int main(){
	int x;
	cin >> x;
	
	int top = 1;
	int bot = 1;
	int max = 1;
	
	bool change = true;
	
	for(int i=1; i<x; i++){
		//cout << top << "/" << bot << "   max = " << max << "\n";
		if(change == true) {
			if(bot == max) {
				bot++;
				max++;
				change = false;
			} else {
				bot++;
				top--;
			}
		} else {
			if(top == max){
				top++;
				max++;
				change = true;
			} else {
				top++;
				bot--;
			}
		}
	}
	
	if(x == 1) cout << "1/1";
	else cout << top << "/" << bot;
	
	return 0;
}
