#include <iostream>
#include <cmath>
#include <stdio.h>
#define _USE_MATH_DEFINES

using namespace std;

int main() {
	int r;
	cin >> r;
	// ��Ŭ���� ������ ���� ���� 2*��*R*R
	// �ý� ������ ���� ���� 2(R*R) 
	
	printf("%.6f\n", M_PI*(r*r));
	printf("%.6f\n", (double)(2*r*r));
		
	return 0;
}

/* ª�� �ҽ� (����) 

#include <iostream>
#include <cmath>
#include <stdio.h>
#define _USE_MATH_DEFINES

using namespace std;

int main() {
	int r;
	cin >> r;	
	printf("%.6f\n%.6f", M_PI*(r*r), (double)(2*r*r));
	return 0;
}

*/
