#include <bits/stdc++.h>
#define ull unsigned long long
#define MOD 1000000007
using namespace std;


vector<vector<ull>> adj;
vector<bool> visited;
vector<ull> disc;
vector<ull> low;
vector<ull> parent;
vector<ull> children;
set<pair<ull, ull>> cuts;


ull N, M;
ull t = 0;

ull modInverse(int a) 
{ 
    ull y = 0, x = 1; 
    ull m = MOD;
  
  
    while (a > 1) 
    { 
        ull q = a / m; 
        ull t = m; 
        m = a % m, a = t; 
        t = y; 

        y = x - q * y; 
        x = t; 
    } 
    if (x < 0) 
       x += MOD; 
  
    return x; 
} 


ull dfs(ull node){
    visited[node] = true;
    disc[node] = t;
    low[node] = t;
    t += 1;
    children[node] = 1;

    for(auto other : adj[node]){
        if (not visited[other]){
            parent[other] = node;
            children[node] += dfs(other);
            
            low[node] = min(low[node], low[other]);
            
            if (low[other] > disc[node])
                cuts.insert(make_pair(min(node, other), max(node, other)));
        }
        else if (other != parent[node])
            low[node] = min(low[node], low[other]);

    }
    return children[node];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    adj.resize(N + 1);
    visited.resize(N + 1, false);
    parent.resize(N + 1, -1);
    low.resize(N + 1, 100002);
    disc.resize(N + 1, 100002);
    children.resize(N + 1, 100002);

    ull u, v;
    for (ull i = 0; i < M; i++){
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    ull aWin = 0;

    if (dfs(1) != N)
        cout << "0 0";
    else if (cuts.size() == 0)
        cout << "0 0";
    else if(N % 2 == 1)
        cout << "0 1";
    else{
        for (auto edge : cuts){
            ull count = min(children[edge.first], children[edge.second]);
            if (count % 2 == 0)
                aWin += 1;
        }
        ull sz = cuts.size();
        
        ull shared = __gcd(sz, aWin);

        cout << ((aWin / shared) * modInverse(sz / shared)) % MOD << ' ';

        ull bWin = N - aWin;
        shared = __gcd(sz, bWin);

        cout << ((bWin / shared) * modInverse(sz / shared)) % MOD;
    }


}