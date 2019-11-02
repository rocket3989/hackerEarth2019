#include <bits/stdc++.h>
#define ull unsigned long long
#define MOD 1000000007
using namespace std;


ull combination(ull n, ull k){
    ull ans=1;
    k = k>n-k ? n-k : k;
    ull j = 1;
    for(; j <= k; j++, n--){

        if(n % j == 0)
            ans *= n / j;

        else if(ans % j == 0)
            ans = ans / j * n;
        
        else
            ans = (ans * n) / j;
        ans %= MOD;
    }
    return ans;
}


int main(){
    ull l, r, n, sum, curr;
    cin >> l >> r >> n;
    sum = 0;
    
    for(int i = 0; i < n - 1; i ++){
        cin >> curr;
        sum += curr != 0 ? curr : 1;
    }
    
    if(r - l < sum)
        cout << 0;
    else
        cout << combination(n + (r - l - sum), n);
    cout << endl;
}