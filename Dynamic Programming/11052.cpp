#include <iostream>

using namespace std;

int main() {
	cin.tie(0);
	
	int dp[10001];
	
	int N;
	cin >> N;
	
	int P[N+1];
	
	dp[0] = P[0] = 0;

	for(int i=1; i<=N; i++) {
		cin >> P[i];	
	}

	for(int i=1; i<=N; i++) {
		for(int j=1; j<=i; j++) {
			dp[i] = max(dp[i], dp[i-j]+P[j]);
		}
	}
	
	cout << dp[N];

	return 0;
}
