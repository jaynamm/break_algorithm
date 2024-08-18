#include <iostream>
#include <string>

using namespace std;

const int MAX = 53;

int r[MAX];
int a[MAX];

int main(){
	cin.tie(0);
	int n, s;
	cin >> n;
	string str, remainder;
		
	for(int i=0; i<n; i++){
		cin >> s;
		a[s]++;
	}
	
	getline(cin, remainder);
	getline(cin, str);
	
	// 	'A'-64 = 1 'Z'-64 = 26 'a'-70 = 27 'z'-70 = 52
	
	for(int i=0; i<str.length(); i++){
		if('a' <= str[i] && str[i] <= 'z') {
			r[str[i]-70]++;
		} else if('A' <= str[i] && str[i] <= 'Z'){
			r[str[i]-64]++;
		} else if(str[i] == ' ') {
			r[0]++;
		}
	}
	
	bool check = true;
	
	for(int i=1; i<MAX; i++){
		if(a[i] != r[i]){
			check = false;
			break;
		}
	}

	if(check) cout << "y";
	else cout << "n";
	
	return 0;
}
