#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M, L, R, K, test;
    cin >> N >> M >> L >> R >> K;

    long long * res = new long long[N];

    test = N % M;
    long long count = 0;


    for(long long i = L; i <= R; i++){
        if (N % i == test and i != M)
            res[count++] = i;
    }
    cout << count << '\n';

    if(count <= K){
        for(long long i = 0; i < count; i++)
            cout << res[i] << ' ';
        cout << '\n';
    }
    else
        cout << -1 << '\n';
    
}