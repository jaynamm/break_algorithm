#include <iostream>
#include <cmath>

using namespace std;

int T, N, M;
long long int dp[31][31];

int main(){
	cin.tie(0);
	cin >> T;
	
	for(int i=1; i<30; i++){
		dp[i][0] = 1;
		for(int j=1; j<30; j++){
			if(i == j) dp[i][j] = 1;
			else dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
		}
	}
	/*
	for(int i=1; i<30; i++){
		for(int j=1; j<i; j++){
			cout << i << " / " << j << " : " << dp[i][j] << "\n";
		}
	}
	*/
	for(int i=0; i<T; i++){
		cin >> N >> M;
		cout << dp[M][N] << "\n";
	}
	
	return 0;
}

// DP 이용한 조합 문제 
