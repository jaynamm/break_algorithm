#include <iostream>
#include <string.h>
#include <string>

using namespace std;

int main(){
	int t;
	cin >> t;
	
	string ps;
	char stack[51];
	
	for(int i=0; i<t; i++){
		cin >> ps;
		int index = 0;
		bool check = true;
		
		for(int j=0; j<ps.length(); j++){
			if(ps[0] == ')'){
				check = false;
				break;
			}
			if(ps[j] == '(') {
				stack[index] = ps[j];
				index++;
			} else if (ps[j] == ')'){
				index--;
				if(index < 0) {
					check = false;
					break;
				}
			}
			/*
			for(int k=0; k<index; k++){
				cout << stack[k] << " ";
			}
			cout << "\n";
			*/
		}
		
		if(index > 0) check = false; 
		
		if(check) cout << "YES\n";
		else cout << "NO\n";	
	}

	return 0;
}
