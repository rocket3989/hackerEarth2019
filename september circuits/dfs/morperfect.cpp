#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> order;
vector<set<pair<int, int>>> children;
vector<bool> isParent;


bool dfs(int node){
    if(!isParent[node])
        return false;

    set<pair<int, int>>::iterator child = children[node].begin();

    while(children[node].size()){
        
        // child = children[node].upper_bound(make_pair(currentCost - 1,0));

        order[node].push_back(child -> second);

        bool parent = dfs(child -> second);
        
        children[node].erase(child++);

        if(parent || child == children[node].end())
            child = children[node].begin();
       
    }
    return true;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // ifstream cin("input.txt");
    // ofstream cout("output.txt");

    int n, parent, currentCost = 0;
    cin >> n;

    order.resize(n);
    children.resize(n);
    isParent.resize(n, false);

    vector<int> cost(n);

    for(int i = 0; i < n; i++)
        cin >> cost[i];

    for(int i = 1; i < n; i++){
        cin >> parent;
        children[parent - 1].insert(make_pair(cost[i], i));
        isParent[parent - 1] = true;
    }
    
    dfs(0);

    for(auto node : order){
        if(node.size() == 0){
            cout << 0 << '\n';
        }
        else{
            for(int i : node){
                cout << i + 1 << ' ';
            }
            cout << '\n';
        }
    }
}