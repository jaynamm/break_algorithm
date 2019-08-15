#include <iostream>
#define MAX 50000001

using namespace std;

char str[MAX];

int main(){
	cin.tie(0);
	int n;
	cin >> n >> str;
	
	int num;
	long long sum = 0, res = 0;
	int d = 1;
	
	for(int i=n-1; i>=0; i--){
		if(i == 0) {
			if('0'<= str[i] && str[i]<='9'){
				num = str[i]-'0';
				sum += num * d;
				d *= 10;
				if(sum>999999) sum = 0;
				res += sum;
			}
		}
		if('0'<=str[i] && str[i]<='9'){
			num = str[i]-'0';
			sum += num * d;
			d *= 10;
		} else {
			d = 1;
			if(sum>999999) sum = 0;
			else {
				res += sum;	
				sum = 0;
			}
		}
	}
	
	cout << res << "\n";

	return 0;
}
