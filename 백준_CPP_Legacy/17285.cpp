#include <iostream>
#include <string.h>

using namespace std;

int main(){
	char t[101];
	cin >> t;
	
	char key = t[0] ^ 'C';
	
	for(int i=0; i<strlen(t); i++){
		cout << (char)(t[i] ^ key);
	}
	
	return 0;
}
