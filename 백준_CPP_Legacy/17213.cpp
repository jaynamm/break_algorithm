#include <iostream>

using namespace std;

int sel[8];
int cnt;
int n, m;

int Comb(int index, int count){
	if(count == m-n){
		cnt++;
		return 0;
	}
	
	for(int i=index; i<n; i++){
		sel[count] = i+1;
		Comb(i, count+1);
	}
}

int main(){
	cin >> n >> m;
	Comb(0, 0);
	cout << cnt << "\n";
	return 0;
}
