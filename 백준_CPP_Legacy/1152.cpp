#include <iostream>
#include <string>

#define MAX 1000001

using namespace std;

int main(){
	string str;
	int cnt = 1;

	getline(cin, str);
	
	for(int i=0; i<str.length(); i++){
		if(str[i] == ' '){ // ���ڰ� ������ ���
			cnt++;
		}
	}
	
	if(str[0] == ' ' || str[0] == '\0'){ // ó�� ������ ���� ��� 
		cnt--;
	}
	
	if(str[str.length()-1] == ' '){ // �� �ڰ� ������ �ܿ� 
		cnt--;
	}
		
	cout << cnt;

	return 0;
}
