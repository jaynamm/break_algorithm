#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	
	int h, w, n;
	
	for(int i=0; i<t; i++){
		cin >> h >> w >> n;
		
		int floor = 1;
		int num = 1;
		
		for(int j=1; j<n; j++){
			if(floor == h){
				floor = 1;
				num++;
			} else {
				floor++;
			}			
		}
		
		cout << floor*100 + num << "\n";
	}
	
	return 0;
}
