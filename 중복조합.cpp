#include <iostream>

using namespace std;

int sel[8];
int cnt;

int Comb(int index, int count){
	if(count == 6){
		for(int i=0; i<6; i++){
			cout << sel[i] << " ";
		}
		cnt++;
		cout << "\n";
		cout << cnt << "\n";
		return 0;
	}
	
	for(int i=index; i<100; i++){
		sel[count] = i+1;
		Comb(i, count+1);
	}
}

int main(){
	Comb(0, 0);
	
	return 0;
}
