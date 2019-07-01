#include <iostream>

using namespace std;

int main(){

	int n[8] = {0};
	int asc = 0;
	int desc = 8;
		
	for(int i=0; i<8; i++){
		cin >> n[i];
		if(n[i] == i+1) {
			asc++;
		} else if(n[i] == 8-i) {
			desc--;
		}
	}
	
	if(asc == 8) cout << "ascending\n";
	else if(desc == 0) cout << "descending\n";
	else cout << "mixed\n";
	
	return 0;
}
