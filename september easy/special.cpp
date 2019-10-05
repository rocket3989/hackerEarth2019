#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<long> vals;

    long n, k, temp;

    cin >> n >> k;

    for(int i = 0; i < n; i++){
        cin >> temp;
        vals.push_back(temp);
    }
    
    sort(vals.begin(), vals.end());
    
    long long sum = 0;

    for(int i = 0; i < n - k; i++)
        sum += vals[i];
    cout << sum;



}