#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> order;
vector<set<pair<int, int>>> children;
vector<bool> isParent;


bool dfs(int node, int& currentCost){
    if(!isParent[node])
        return false;

    set<pair<int, int>>::iterator child;

    while(children[node].size()){
        
        child = children[node].upper_bound(make_pair(currentCost - 1,0));
        
        if(child == children[node].end()){

            currentCost = 0;
            child = children[node].upper_bound(make_pair(0,0));
        }

        currentCost = child -> first;
        order[node].push_back(child -> second);

        dfs(child -> second, currentCost);
        
        children[node].erase(child++);
       
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
    
    dfs(0, currentCost);

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


// maxSize of child array == 20
// ~10 nodes with 20 children
// ~15 nodes with 0 children