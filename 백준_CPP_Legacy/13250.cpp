#include <iostream>

using namespace std;

double dp[1000001];

int main(){
	cin.tie(0);
	cout << fixed;
	cout.precision(16);	
	
	int n;
	cin >> n;
	
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = (dp[0] + dp[1])/6 + 1;
	dp[3] = (dp[0] + dp[1] + dp[2])/6 + 1;
	dp[4] = (dp[0] + dp[1] + dp[2] + dp[3])/6 + 1;
	dp[5] = (dp[0] + dp[1] + dp[2] + dp[3] + dp[4])/6 + 1;
				
	for(int i=6; i<=n; i++){
		dp[i] = (dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6])/6 + 1;
	}
	/* 시간 초과 
	dp[0] = 0;
	dp[1] = 1;
	
	for(int i=2; i<=n; i++){
		double sum = 0;
	
		for(int j=0; j<i; j++){
			sum += dp[j];
		}
		dp[i] = sum/6 + 1;
	}
	*/
	cout << dp[n] << "\n";
	
	return 0;
}
