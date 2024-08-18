#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
	cin.tie(0);
	int n;
	cin >> n;
	
	/*
		1 : 1
		2 : 10
		3 : 100 101
		4 : 1000 1001 1010
		5 : 10000 10001 10010 10100 10101
	*/
	
	long long dp[100];
	
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 1;
	
	for(int i=3; i<=n; i++){
		dp[i] = dp[i-1] + dp[i-2];
	}
	
	cout << dp[n];
	
	return 0;
}
