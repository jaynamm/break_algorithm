#include <iostream>

using namespace std;

int n, m, k, ii, jj, x, y;
int num[301][301];

int main(){
	cin.tie(0);
	cin >> n >> m;
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			cin >> num[i][j];		
		}
	}
	
	cin >> k;
	
	for(int i=0; i<k; i++){
		cin >> ii >> jj >> x >> y;
		int sum = 0;
		
		for(int j=ii; j<=x; j++){
			for(int l=jj; l<=y; l++){
				sum += num[j][l];
			}
		}
		cout << sum << "\n";
	}
	
	return 0;
}
