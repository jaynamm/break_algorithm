#include <iostream>
#include <cmath>

using namespace std;

int main(){
	double a, b, v;
	double tmp1, tmp2;
	double cnt = 0;
	cin >> a >> b >> v;
	
	// (2 -1) + (2 -1) + (2 -1) + 2 = 5
	
	tmp1 = v-a;
	tmp2 = a-b;
	cnt = ceil(tmp1/tmp2) + 1;
	
	// ceil 함수 리턴형이 double 같은 실수이기 때문에 int형이나 long형으로 캐스팅해줘야 정답.
	cout << (int)cnt << "\n";
	
	return 0;
}
