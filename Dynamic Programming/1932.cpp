#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdio.h>

using namespace std;

int tr[501][501];

int main(){
	cin.tie(0);
	int n;
	cin >> n;
	
	/*
		     1
		    2 3
	  	   4 5 6
		  7 8 9 10
		11 12 13 14 15
		
		     1
		    1 2
		   1 2 3
		  1 2 3 4
		 1 2 3 4 5
	*/
	
	for(int i=1; i<=n; i++) 
		for(int j=1; j<=i; j++)
			cin >> tr[i][j];
	
	int maxsum = 0;
	int dp[n+1][n+1] = {0};
	dp[1][1] = tr[1][1];
	
	for(int i=2; i<=n; i++){
		for(int j=1; j<=i; j++){
			if(j == 1){
				dp[i][j] = tr[i][j] + dp[i-1][j];
			} else if(j == i){
				dp[i][j] = tr[i][j] + dp[i-1][j-1];
			} else {
				dp[i][j] = tr[i][j] + max(dp[i-1][j-1], dp[i-1][j]);
			}
			//printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
		}
	}
	
	for(int i=1; i<=n; i++) {
		//printf("dp[%d][%d] = %d\n", n, i, dp[n][i]);
		maxsum = max(maxsum, dp[n][i]);	
	}
	
	cout << maxsum;
	
	return 0;
}
