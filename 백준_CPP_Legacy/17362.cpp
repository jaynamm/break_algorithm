#include <iostream>

using namespace std;

int main(){
	cin.tie(0);
	
	int n;
	cin >> n;
	
	/*
	1 2 3 4
	        5
	  8 7 6
	9
	  10 11 12
	          13
      16 15 14
    17
      ...
	*/
	
	if(n%8 >= 1 && n%8 <= 5){
		cout << n%8;
	} else if(n%8 == 6){
		cout << "4\n";
	} else if(n%8 == 7){
		cout << "3\n";
	} else if(n%8 == 0){
		cout << "2\n";
	} 
		
	return 0;
}
