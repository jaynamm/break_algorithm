#include <iostream>

using namespace std;

int main(){
	int n, num;
	int sum = 0;
	cin >> n;
	
	for(int i=1; i<=1000000; i++){
		sum = i;
		num = i;
		while(num>0){
			sum += num%10;
			num = num/10;
		}
		if(sum == n){
			cout << i << "\n";
			return 0;
		}
	}
	
	cout << 0 << "\n";
	
	return 0;
}
