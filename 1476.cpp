#include <iostream>

using namespace std;

int main() {
	int e, s, m;
	cin >> e >> s>> m;
	
	int year = 1;
	
	while(true){
		if((year-e)%15 == 0 && (year-s)%28 == 0 && (year-m)%19 == 0){
			cout << year;
			return 0;
		}
		year++;
	}
	
	return 0;
}
