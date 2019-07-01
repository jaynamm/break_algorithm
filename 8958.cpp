#include <iostream>

using namespace std;

int main(){

	int n;
	cin >> n;
	int res[n+1];
	
	string str;
	
	for(int i=0; i<n; i++){
		cin >> str;
		int sum = 0;
		int num[str.size()];
		for(int j=0; j<str.size(); j++){
			if(str.substr(j,1) == "O"){
				num[j]  = 1 + num[j-1];
			} else {
				num[j] = 0;
			}
			sum += num[j];
		}
		cout << sum << "\n";
	}
	
	return 0;
}
