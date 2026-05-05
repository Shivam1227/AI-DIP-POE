% Graph definition
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).

% DFS
dfs(Start, Goal, Path) :-
    dfs_util(Start, Goal, [Start], Path).

dfs_util(Goal, Goal, Visited, Path) :-
    reverse(Visited, Path).

dfs_util(Current, Goal, Visited, Path) :-
    edge(Current, Next),
    \+ member(Next, Visited),
    dfs_util(Next, Goal, [Next|Visited], Path).
