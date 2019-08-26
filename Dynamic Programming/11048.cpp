#include <iostream>
#include <cmath>

using namespace std;

int N, M;
int candy[1001][1001];
int dp[1001][1001];

int main(){
	cin.tie(0);
	cin >> N >> M;
	
	for(int i=1; i<=N; i++)
		for(int j=1; j<=M; j++)
			cin >> candy[i][j];
	
	dp[1][1] = candy[1][1];
	
	for(int i=1; i<=N; i++){
		for(int j=1; j<=M; j++){
			dp[i][j] = max(dp[i-1][j], max(dp[i][j-1], dp[i-1][j-1])) + candy[i][j];
		}
	}
	
	cout << dp[N][M];
	
	return 0;
}
