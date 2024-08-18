#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

int main(){
	int k;
	cin >> k;
	
	int money;
	
	vector<int> wallet;
	
	for(int i=0; i<k; i++){
		cin >> money;
		if(money == 0) {
			if(wallet.size() != 0){
				wallet.pop_back();
			}
		} else {
			wallet.push_back(money);
		}
	}
	
	int sum = 0;
	
	for(int i=0; i<wallet.size(); i++){
		sum += wallet[i];
	}
	
	cout << sum;
	
	return 0;
}
