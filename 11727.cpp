#include <iostream>

using namespace std;

int main(){
	cin.tie(0);
	int n; 	
	cin >> n;
	
	int dp[n+1];
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 3;
	
	for(int i=3; i<=n; i++){
		dp[i] = (dp[i-1] + dp[i-2]*2)%10007;
	}
	
	cout << dp[n];
	 	
	return 0;
}
