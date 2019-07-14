#include <iostream>

using namespace std;

int main(){

    int n;
    int m = 1;
    cin >> n;

    for(int i=0; i<n; i++){
    	for(int k=0; k<i; k++){
        	cout << " ";
		}
        for(int j=i; j<2*n-m; j++){
        	cout << "*";
        }
        m++;
        cout << "\n";
    }

    return 0;
}
