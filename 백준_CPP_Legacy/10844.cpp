#include <iostream>
#define mod 1000000000
using namespace std;

int dp[101][10];

int main(){

    int n;
    cin >> n;

    // 1�ڸ� �� ��, 1�� �̹Ƿ� 1�� set
    // 0�� �ü� ���⶧���� 0�� ����
    for(int i=1; i<=9; i++){
        dp[1][i] = 1;
    }

    for(int i=2; i<=n; i++){
        for(int j=0; j<=9; j++){
            if(j == 0){
                dp[i][j] = dp[i-1][j+1] % mod; // '0' �� ��, '1' �� ����
            } else if(j == 9){
                dp[i][j] = dp[i-1][j-1] % mod; // '9' �� ��, '8' �� ����
            } else{
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod; // �� ���� ����
            }
        }
    }

    int sum = 0;

    for(int i=0; i<=9; i++){
        sum = (sum + dp[n][i]) % mod;
    }

    cout << sum << "\n";

    return 0;
}
