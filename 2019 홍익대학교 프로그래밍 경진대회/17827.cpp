#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	cin.tie(0);
	int N, M, V;
	cin >> N >> M >> V;
	
	int C[N+1];
	
	for(int i=0; i<N; i++){
		cin >> C[i];
	}
	
	int K;
	
	for(int i=0; i<M; i++){
		cin >> K;
		if(K < V) {
			cout << C[K] << "\n";
		} else {
			int head = V-1;
			int length = N - head;
			cout << C[(K-head)%length + head] << "\n";
		}
	}
	
	return 0;
}
