#include <iostream>
#include <cmath>
#include <stdio.h>
#define _USE_MATH_DEFINES

using namespace std;

int main() {
	int r;
	cin >> r;
	// 유클리드 기하학 원의 넓이 2*ㅠ*R*R
	// 택시 기하학 원의 넓이 2(R*R) 
	
	printf("%.6f\n", M_PI*(r*r));
	printf("%.6f\n", (double)(2*r*r));
		
	return 0;
}

/* 짧은 소스 (성공) 

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
