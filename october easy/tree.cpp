#include <bits/stdc++.h>
using namespace std;
#define ll long long

vector<vector<ll>> adjacency;

vector<multimap<ll,ll>> mapping;

vector<ll> vals;
vector<ll> diffs;
vector<ll> answers;

void fillMap(ll node, ll parent){

    mapping[node].insert(make_pair(0, vals[node]));

    ll maxDiff = 0;

    for(auto a : adjacency[node]){
        if(a == parent) continue;
        fillMap(a, node);
        for (auto b : mapping[a]){
            mapping[node].insert(make_pair(b.first + 1, b.second));
            if (abs(b.second - vals[node]) > maxDiff)
                maxDiff = abs(b.second - vals[node]);
        }
        mapping[a].clear();

    }
    
    bool found = false;
    answers[node] = -1;

    if (diffs[node] > maxDiff)
        return;

    for(auto a : mapping[node]){
        if(abs(a.second - vals[node]) >= diffs[node]){
            answers[node] = a.first;
            found = true;
            break;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n;
    cin >> n;
    adjacency.resize(n);
    mapping.resize(n);
    answers.resize(n);

    ll a, b;
    for (ll i = 0; i < n; i ++){
        cin >> a; 
        vals.push_back(a);
    }
    
    for (ll i = 0; i < n; i ++){
        cin >> a; 
        diffs.push_back(a);
    }

    for (ll i = 1; i < n; i++){
        cin >> a >> b;
        adjacency[a - 1].push_back(b - 1);
        adjacency[b - 1].push_back(a - 1);
    }

    fillMap(0, n + 1);

    for(ll i = 0; i < n; i++){
        cout << answers[i] << '\n';
    }
}