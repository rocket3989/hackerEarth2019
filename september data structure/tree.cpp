#include <bits/stdc++.h> 
using namespace std; 
int R = 0; 
  
// n -> it represent total number of nodes 
// len -> it is the maximum length of array to hold  
//          ancestor of each node. In worst case,  
// the highest value of ancestor a node can have is n-1. 
// 2 ^ len <= n-1 
// len = O(log2n) 
int getLen(int n) 
{ 
    return (int)(log(n) / log(2)) + 1; 
} 
  
// ancstr represents 2D matrix to hold ancestor of node. 
// Here we pass reference of 2D matrix so that the change 
// made occur directly  to the original matrix 
// depth[] stores depth of each node 
// len is same as defined above 
// n is total nodes in graph 
// R represent root node 
void setancestor(vector<vector<int> >& ancstr, 
           vector<int>& depth, int* node, int len, int n) 
{ 
    // depth of root node is set to 0 
    depth[R] = 0; 
  
    // if depth of a node is -1 it means its depth  
    // is not set otherwise we have computed its depth 
    for (int j = 1; j <= len; j++) { 
        for (int i = 0; i < n; i++) { 
            ancstr[node[i]][j] = ancstr[ancstr[node[i]][j - 1]][j - 1]; 
  
            // if ancestor of current node is R its height is 
            //  previously not set, then its height is  2^j 
            if (ancstr[node[i]][j] == R && depth[node[i]] == -1) { 
  
                // set the depth of ith node 
                depth[node[i]] = pow(2, j); 
            } 
  
            // if ancestor of current node is 0 means it  
            // does not have root node at its 2th power  
            // on its path so its depth is 2^(index of  
            // last non zero ancestor means j-1) + depth  
            // of 2^(j-1) th ancestor 
            else if (ancstr[node[i]][j] == 0 &&  
                     node[i] != R && depth[node[i]] == -1) { 
                depth[node[i]] = pow(2, j - 1) +  
                                 depth[ancstr[node[i]][j - 1]]; 
            } 
        } 
    } 
} 
  
// c -> it represent child 
// p -> it represent ancestor 
// i -> it represent node number 
// p=0 means the node is root node 
// R represent root node 
// here also we pass reference of 2D matrix and depth 
// vector so that the change made occur directly to 
// the original matrix and original vector 
void constructGraph(vector<vector<int> >& ancstr, 
            int* node, vector<int>& depth, int* isNode, 
                                   int c, int p, int i) 
{ 
    // enter the node in node array 
    // it stores all the nodes in the graph 
    node[i] = c; 
  
    // to confirm that no child node have 2 ancestors 
    if (isNode == 0) { 
        isNode = 1; 
  
        // make ancestor of x as y 
        ancstr[0] = p; 
  
        // ifits first ancestor is root than its depth is 1 
        if (R == p) { 
            depth = 1; 
        } 
    } 
    return; 
} 
  
// this function will delete leaf node 
// x is node to be deleted 
void removeNode(vector<vector<int> >& ancstr,  
                    int* isNode, int len, int x) 
{ 
    if (isNode[x] == 0) 
        cout << "node does not present in graph " << endl; 
    else { 
        isNode[x] = 0; 
  
        // make all ancestor of node x as 0 
        for (int j = 0; j <= len; j++) { 
            ancstr[x][j] = 0; 
        } 
    } 
    return; 
} 
  
// x -> it represent new node to be inserted 
// p -> it represent ancestor of new node 
void addNode(vector<vector<int> >& ancstr, 
      vector<int>& depth, int* isNode, int len,  
                                 int x, int p) 
{ 
    if (isNode[x] == 1) { 
        cout << " Node is already present in array " << endl; 
        return; 
    } 
    if (isNode[p] == 0) { 
        cout << " ancestor not does not present in an array " << endl; 
        return; 
    } 
  
    isNode[x] = 1; 
    ancstr[x][0] = p; 
  
    // depth of new node is 1 + depth of its ancestor 
    depth[x] = depth[p] + 1; 
    int j = 0; 
  
    // while we don't reach root node 
    while (ancstr[x][j] != 0) { 
        ancstr[x][j + 1] = ancstr[ancstr[x][j]][j]; 
        j++; 
    } 
  
    // remaining array will fill with 0 after  
    // we find root of tree 
    while (j <= len) { 
        ancstr[x][j] = 0; 
        j++; 
    } 
    return; 
} 
  
// LA function to find Lth level ancestor of node x 
void LA(vector<vector<int> >& ancstr, vector<int> depth,  
                              int* isNode, int x, int L) 
{ 
    int j = 0; 
    int temp = x; 
  
    // to check if node is present in graph or not 
    if (isNode[x] == 0) { 
        cout << "Node is not present in graph " << endl; 
        return; 
    } 
  
    // we change L as depth of node x - 
    int k = depth[x] - L; 
    // int q = k; 
    // in this loop we decrease the value of k by k/2 and 
    // increment j by 1 after each iteration, and check for set bit 
    // if we get set bit then we update x with jth ancestor of x 
    // as k becomes less than or equal to zero means we 
    // reach to kth level ancestor 
    while (k > 0) { 
  
        // to check if last bit is 1 or not 
        if (k & 1) { 
            x = ancstr[x][j]; 
        } 
  
        // use of shift operator to make k = k/2  
        // after every iteration 
        k = k >> 1; 
        j++; 
    } 
    cout << L << "th level acestor of node "
               << temp << " is = " << x << endl; 
  
    return; 
} 
  
int main() 
{ 
    // n represent number of nodes 
    int n = 12; 
  
    // initialization of ancestor matrix 
    // suppose max range of node is up to 1000 
    // if there are 1000 nodes than also length  
    // of ancestor matrix will not exceed 10 
    vector<vector<int> > ancestor(1000, vector<int>(10)); 
  
    // this vector is used to store depth of each node. 
    vector<int> depth(1000); 
  
    // fill function is used to initialize depth with -1 
    fill(depth.begin(), depth.end(), -1); 
  
    // node array is used to store all nodes 
    int* node = new int[1000]; 
  
    // isNode is an array to check whether a 
    // node is present in graph or not 
    int* isNode = new int[1000]; 
  
    // memset function to initialize isNode array with 0 
    memset(isNode, 0, 1000 * sizeof(int)); 
  
    // function to calculate len 
    // len -> it is the maximum length of array to  
    // hold ancestor of each node. 
    int len = getLen(n); 
  
    // R stores root node 
    R = 2; 
  
    // construction of graph 
    // here 0 represent that the node is root node 
    constructGraph(ancestor, node, depth, isNode, 2, 0, 0); 
    constructGraph(ancestor, node, depth, isNode, 5, 2, 1); 
    constructGraph(ancestor, node, depth, isNode, 3, 5, 2); 
    constructGraph(ancestor, node, depth, isNode, 4, 5, 3); 
    constructGraph(ancestor, node, depth, isNode, 1, 5, 4); 
    constructGraph(ancestor, node, depth, isNode, 7, 1, 5); 
    constructGraph(ancestor, node, depth, isNode, 9, 1, 6); 
    constructGraph(ancestor, node, depth, isNode, 10, 9, 7); 
    constructGraph(ancestor, node, depth, isNode, 11, 10, 8); 
    constructGraph(ancestor, node, depth, isNode, 6, 10, 9); 
    constructGraph(ancestor, node, depth, isNode, 8, 10, 10); 
  
    // function to pre compute ancestor matrix 
    setancestor(ancestor, depth, node, len, n); 
  
    // query to get 1st level ancestor of node 8 
    LA(ancestor, depth, isNode, 8, 1); 
  
    // add node 12 and its ancestor is 8 
    addNode(ancestor, depth, isNode, len, 12, 8); 
  
    // query to get 2nd level ancestor of node 12 
    LA(ancestor, depth, isNode, 12, 2); 
  
    // delete node 12 
    removeNode(ancestor, isNode, len, 12); 
  
    // query to get 5th level ancestor of node 
    // 12 after deletion of node 
    LA(ancestor, depth, isNode, 12, 1); 
  
    return 0; 
} 