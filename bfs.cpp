#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int V = 5; // number of vertices

    vector<vector<int>> adj(V);

    // Sample graph (undirected)
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0};
    adj[3] = {1};
    adj[4] = {1};

    vector<bool> visited(V, false);
    queue<int> q;

    int start = 0;

    visited[start] = true;
    q.push(start);

    cout << "BFS Traversal: ";

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        cout << node << " ";

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    return 0;
}