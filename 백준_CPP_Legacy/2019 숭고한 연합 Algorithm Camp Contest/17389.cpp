#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
	int n;
	cin >> n;
	char s[n+1];
	
	int sum = 0;
	int bonus = 0;
	int score;
	
	for(int i=1; i<=n; i++){
		cin >> s[i];
		
		if(s[i] == 'O'){
			score = i + bonus;
			sum += score;
			bonus++;
		} else if(s[i] == 'X'){
			bonus = 0;
		}
	}
	
	cout << sum;
	
	return 0;
}
