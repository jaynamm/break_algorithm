#include <iostream>

using namespace std;

int main(){
	int a, b, c;
	cin >> a >> b >> c;
	
	// 만든 비용이 판매 비용보다 크면 손익분기점을 넘기지 못한다.
	// 따라서, 만든 비용이 더 적어야 한다. 
	if(b >= c) {
		cout << "-1\n";
		return 0;
	}
	// 판매비용 - 제작비용 이 이익이기 때문에 고정 비용을 나눈 후 1을 더해주면 손익분기점을 넘기게 된다. 
	if(a/(c-b)+1 <= 0) cout << "-1\n";
	else cout << a/(c-b)+1 << "\n";

	
	return 0;
}
