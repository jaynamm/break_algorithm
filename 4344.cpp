#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    cin.tie(0);
    ios::sync_with_stdio(false);

    int c, n;

    cin >> c;

    int sum =0 ;
    double avg = 0;
    double cnt = 0;

    for(int i=0; i<c; i++){
        cin >> n;
        int score[n];
        for(int j=0; j<n; j++){
            cin >> score[j];
            sum += score[j];
        }

        avg = sum/n;

        for(int k=0; k<n; k++){
            if(score[k] > avg) {
                cnt++;
            }
        }

        double res = (double)(cnt/n)*100;

        printf("%.3lf%c \n", res, '%');

        sum = 0;
        avg = 0;
        cnt = 0;
    }

    return 0;
}
