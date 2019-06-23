#include <iostream>
#include <stdio.h>

using namespace std;

int main() {

    int n;

    cin >> n;

    for(int i=1; i<=n; i++){
        for(int j=n; j>=i; j--){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
