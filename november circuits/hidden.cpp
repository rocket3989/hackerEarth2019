#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long

ull gcd(ull a, ull b){
    if(a * b == 0){
        if(a != 1 && b != 1)
            return 2;
        return 1;
    }
    
    while(b){
        ull temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}


int main(){
    int N;
    cin >> N;
    double bestDist = DBL_MAX;
    pair<ull, ull> bestStart;
    
    for(ull i = 0; i < 10000000; i++){
        if(bestDist < i * (double)i) break;
        if(i % 1000 == 0) cout << i << endl;

        for(ull j = 0; j <= i; j++){
            if(gcd(i, j) != 1 && bestDist > i*(double)i + j *(double)j){
                bool checks = true;
                for(int val = 1; val < N * N && checks; val++){
                    if (gcd(i + (val / N), j + (val % N)) == 1) checks = false;
                }
                if (checks){
                    bestDist = i*(double)i + j *(double)j;
                    bestStart = make_pair(i, j);
                    cout << i << ", " << j << endl;
                }
            }
        }
    }
    cout << bestStart.first << ", " << bestStart.second << endl;


}