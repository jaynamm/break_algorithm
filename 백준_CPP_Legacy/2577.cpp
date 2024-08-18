#include <iostream>

using namespace std;

int main(){
	
	int a, b, c;
	int res = 0;
	
	cin >> a >> b >> c;
	
	res = a*b*c;
	
	int tmp = res;
	int n;
	int num[100] = {0};
	
	while(tmp > 0){
		n = tmp%10;
		num[n]++;	
		tmp = tmp/10;
	}

	for(int i=0; i<10; i++){
		cout << num[i] << "\n";
	}
	return 0;
}
