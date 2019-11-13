#include <iostream>
#include <algorithm>

using namespace std;

int arr[1024][1024];

int main(){

	int N;
	cin >> N;	
	
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			cin >> arr[i][j];
		}
	}
	
	while(N!=1) {
		int temp[N/2][N/2];
		for(int i=0; i<N; i+=2){
			for(int j=0; j<N; j+=2){
				int set[4];
				set[0] = arr[i][j];
				set[1] = arr[i+1][j];
				set[2] = arr[i][j+1];
				set[3] = arr[i+1][j+1];
				
				sort(set, set+4);
				temp[i/2][j/2] = set[2];
			}
		}
		
		N/=2;
		
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				arr[i][j] = temp[i][j];
			}
		}
	}
	
	cout << arr[0][0];
	
	return 0;
}
