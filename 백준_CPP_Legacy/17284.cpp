#include <iostream>

using namespace std;

int main(){
	char btn;
	int mon = 5000;
	
	while(true){
		cin.get(btn);
		if(btn=='\n') break;
		
		if(btn=='1'){
			mon -= 500;
		} else if(btn=='2') {
			mon -= 800;
		} else if(btn=='3') {
			mon -= 1000;
		}
	}
	
	cout << mon;
	
	return 0;
}
