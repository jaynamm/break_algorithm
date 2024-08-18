#include <iostream>

using namespace std;

int main(){
	cin.tie(0);	
	int T, n, cnt;
	cin >> T;
	
	int dp[101];
	
	for(int i=1; i<=100; i++) dp[i] = 1;
		
	for(int i=2; i<=100; i++){
		for(int j=1; j<=100; j++){
			if(i == 2){
				if(j%i == 0) {
					dp[j] = 0;
				}
			} else {
				if(j%i == 0){
					if(dp[j] == 0) dp[j] = 1;
					else if(dp[j] == 1) dp[j] = 0;
				}	
			}
		}
	}
	
	for(int i=0; i<T; i++){
		cin >> n;
		cnt = 0;
		for(int j=1; j<=n; j++){
			if(dp[j] == 1) cnt++;
		}
		cout << cnt << "\n";
	}

	return 0;
}
