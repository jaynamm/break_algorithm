#include <iostream>
#include <string.h>

using namespace std;

int stack[100001];
char res[200001];

int main(){
	int n;
	cin >> n;
	
	int top = 0, istack = 0, ires = 0;
	int num[n+1];
	
	for(int i=0; i<n; i++){
		cin >> num[i];
		
		//cout << "num : " << num[i] << " top : " << top << "\n";
		
		if(num[i] > top) {
			for(int j=top+1; j<=num[i]; j++){
				stack[istack++] = j;
				res[ires++] = '+';
				//cout << "push : " << stack[istack-1] << " +\n";
			}
		} else {
			if(stack[istack-1] != num[i]) {
				cout << "NO\n";
				return 0;
			}
		}
		//cout << "pop : " << stack[istack-1]<< " -\n";
		istack--;
		res[ires++] = '-';
				
		if(top < num[i]) top = num[i];
	}
	
	for(int i=0; i<ires; i++){
		cout << res[i] << "\n";
	}
	
	return 0;
}
