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
	
	// ceil �Լ� �������� double ���� �Ǽ��̱� ������ int���̳� long������ ĳ��������� ����.
	cout << (int)cnt << "\n";
	
	return 0;
}
