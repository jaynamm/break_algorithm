#include <iostream>
#include <string>
#include<stdio.h>

using namespace std;
int cnt[10];
int main(){
    int n;
    int count = 0;

    int a;
    cin>>a;

    while(a/10)
    {

        cnt[a%10]++;
        a/=10;
    }
    cnt[a%10]++;

    cnt[6] = (cnt[6] + cnt[9])%2==1 ?(cnt[6] + cnt[9])/2+1:(cnt[6] + cnt[9])/2;

    int tmp = 0;

    for(int i=0;i<9;i++){
            tmp = max(tmp, cnt[i]);

        }

    printf("%d", tmp);

    return 0;
}
