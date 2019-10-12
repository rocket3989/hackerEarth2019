#include <bits/stdc++.h>
using namespace std;
int MAX = 20;

vector<int> phi(MAX);
vector<int> primes;
 
 

int main(){
    for(int p = 1; p < MAX; p++)
        phi[p] = p;

    for(int p = 2; p < MAX; p++){
        if (phi[p] == p){
            primes.push_back(p);
            
            phi[p] = p - 1;
    
            for(int i = p * 2; i < MAX; i += p)
                phi[i] = (phi[i] / p) * (p - 1);
        }
    }
    
    int cases, N;
    cin >> cases;
    for(int tc = 0; tc < cases; tc++){

        cin >> N;

        int countOut = N - phi[N], divisors = 1;

        for(auto p: primes){
            int count = 0;
            while (N % p == 0){
                N = N / p;
                count += 1;
            }   
            divisors *= count + 1;
        }
        cout << countOut - divisors + 1 << '\n';
    }
    
}
 
  