#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int sco[51];
	int hong;
	int count;
	
	for(int i=0; i<50; i++){
		cin >> sco[i];
	}
	
	cin >> hong;
	
	for(int i=0; i<50; i++){
		if(sco[i] == hong) {
			count = i+1;
		}
	}
	
	if(1 <= count && count <= 5) {
		cout << "A+\n";
	} else if(6 <= count && count <= 15) {
		cout << "A0\n";
	} else if(16 <= count && count <= 30) {
		cout << "B+\n";
	} else if(31 <= count && count <= 35) {
		cout << "B0\n";
	} else if(36 <= count && count <= 45) {
		cout << "C+\n";
	} else if(46 <= count && count <= 48) {
		cout << "C0\n";
	} else if(49 <= count && count <= 50) {
		cout << "F\n";
	}
	
	return 0; 
}
