#include <iostream>

using namespace std;

int main(){
	int a, b, c;
	cin >> a >> b >> c;
	
	// ���� ����� �Ǹ� ��뺸�� ũ�� ���ͺб����� �ѱ��� ���Ѵ�.
	// ����, ���� ����� �� ����� �Ѵ�. 
	if(b >= c) {
		cout << "-1\n";
		return 0;
	}
	// �Ǹź�� - ���ۺ�� �� �����̱� ������ ���� ����� ���� �� 1�� �����ָ� ���ͺб����� �ѱ�� �ȴ�. 
	if(a/(c-b)+1 <= 0) cout << "-1\n";
	else cout << a/(c-b)+1 << "\n";

	
	return 0;
}
