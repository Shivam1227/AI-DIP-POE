#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {
    int V = 5;

    vector<vector<int>> adj(V);

    // Same sample graph
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0};
    adj[3] = {1};
    adj[4] = {1};

    vector<bool> visited(V, false);
    stack<int> st;

    int start = 0;

    st.push(start);

    cout << "DFS Traversal (Iterative): ";

    while (!st.empty()) {
        int node = st.top();
        st.pop();

        if (!visited[node]) {
            visited[node] = true;
            cout << node << " ";
        }

        // Push neighbors (reverse order for consistency)
        for (int i = adj[node].size() - 1; i >= 0; i--) {
            int neighbor = adj[node][i];
            if (!visited[neighbor]) {
                st.push(neighbor);
            }
        }
    }

    return 0;
}