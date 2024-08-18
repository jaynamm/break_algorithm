#include <iostream>
#include <string.h>

using namespace std;

int main(){
	char s[101];
	cin >> s;
	
	string ans;
	ans += s[0];
	
	int cnt = 0;
	
	for(int i=1; i<=strlen(s); i++){
		//cout << "s["<<i<<"] : "<< s[i] << "\n";
		if(s[i-1] == s[i]-1){
			ans += s[i];
		} else {
			//cout << "ans : " << ans << "\n";
			//cout << "ans size : " << ans.size() << "\n";
			if(ans.size() == 3) cnt++;
			ans = "";	
			ans += s[i];
		}
	}
	
	cout << cnt;
	
	return 0;
}
