#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;

struct Train{
    Train(){}
    Train(int _source, int _dest, int _time, int _cost, int _period, int _id){
        source = _source;
        dest = _dest;
        time = _time;
        cost = _cost;
        period = _period;
        eval = 1;
        id = _id;
    }
    int source, dest, time, cost, period, id;
    ull eval;
};

int n, m, A, B;

vector<vector<Train>> trainsFrom;


bool dfs(int city, set<int>& visited, deque<int>& path){

    if (city == n) {
        for(auto &train : path)
            cout << train << ' ';

        return true;
    
    }

    visited.insert(city);

    for (auto &train : trainsFrom[city]){
        if (visited.find(train.dest) != visited.end() || train.eval == -1) continue;

        path.push_back(train.id);
        if (dfs(train.dest, visited, path))
            return true;
        path.pop_back();
        train.eval = -1
    }
    visited.erase(city);
    return false;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m >> A >> B;

    trainsFrom.resize(n + 1);

    int source, dest, time, cost, period, id;

    for(int i = 0; i < m; i++){
        cin >> source >> dest >> time >> cost >> period;
        
        if (source != dest) 
            trainsFrom[source].push_back(Train(source, dest, time, cost, period, i + 1));

    }
    set<int> visited;
    deque<int> path;
    visited.insert(1);

    dfs(1, visited, path);

    // cout << costOf << endl;

    // for(auto a: bestFrom){
    //     cout << a.first << ' ' << a.second << endl;
    // }

    // while(currCity != n){
    //     cout << bestTrainFrom[currCity].id << ' ';
    //     currCity = bestTrainFrom[currCity].dest;
    // }
    
    cout << endl;

}