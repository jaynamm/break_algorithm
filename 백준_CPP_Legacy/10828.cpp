#include <iostream>
#include <string.h>
#include <vector>

using namespace std;


int main(){
	vector<int> stack;
	
	int n;
	cin >> n;
	
	char command[100];
	
	for(int i=0; i<n; i++){
		cin >> command;
		
		if(!strcmp(command, "push")){
			int num;
			cin >> num;
			stack.push_back(num);
		}
		if(!strcmp(command, "pop")){
			if(stack.begin() == stack.end()){
				cout << "-1\n";
			} else {
				cout << stack[stack.size()-1]<< "\n";
				stack.erase(stack.end()-1);
			}			
		}
		if(!strcmp(command, "size")){
			cout << stack.size() << "\n";
		}
		if(!strcmp(command, "empty")){
			if(stack.size() == 0) {
				cout << "1\n";
			} else {
				cout << "0\n";
			}
		}
		if(!strcmp(command, "top")){
			if(stack.size() == 0){
				cout << "-1\n";
			} else{
				cout << stack[stack.size()-1] << "\n";	
			}
		}
	}
	
	return 0;
}
