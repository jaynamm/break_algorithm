#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	cin.tie(NULL);
	
	int n, m;
	cin >> n;	
	int a[n+1];
	
	for(int i=0; i<n; i++){
		cin >> a[i];
	}
	
	sort(a, a+n);
	
	cin >> m;	
	int input[m+1];
		
	for(int i=0; i<m; i++){
		cin >> input[i];
		//cout << "input[" << i << "] : " << input[i] << "\n";
		
		int s = 0, e = n, mid;
		//cout << "s : " << s << " / e = " << e << " / mid : " << mid << "\n";
		
		bool check = false;
		
		while(s <= e){
			mid = (s+e)/2;
			//cout << "mid : " << mid << "\n";
			//cout << "input : " << input[i] << " / mid : " << a[mid] << "\n";
			if(input[i] < a[mid]){
				e = mid-1;
			} else if(input[i] > a[mid]) {
				s = mid+1;
			} else {
				check = true;
				break;
			}	 
		}
		if(check) cout << "1\n";
		else cout << "0\n";
	}
	
	return 0;
}
