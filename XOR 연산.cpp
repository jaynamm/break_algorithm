#include <iostream>
#include <string.h>
#include <bitset> 

using namespace std;

int main(){
	cout << bitset<8>('A') << "\n";
	cout << bitset<8>('C') << "\n";
	cout << bitset<8>('U') << "\n";
	char x = ('U' ^ 'C');
	cout << bitset<8>('U' ^ 'C') << "\n";
	cout << bitset<8>('C' ^ x) << "\n";
	cout << (char)('^' ^ x) << "\n";
	cout << (char)('A' ^ 10) << "\n";
	cout << (char)('B' ^ 10) << "\n";
	
	return 0;
}

