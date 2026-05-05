% Graph
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).

% BFS
bfs(Start, Goal, Path) :-
    bfs_util([[Start]], Goal, Path).

bfs_util([[Goal|Rest]|_], Goal, Path) :-
    reverse([Goal|Rest], Path).

bfs_util([CurrentPath|OtherPaths], Goal, Path) :-
    CurrentPath = [Current|_],
    findall([Next,Current|CurrentPath],
        (edge(Current, Next), \+ member(Next, CurrentPath)),
        NewPaths),
    append(OtherPaths, NewPaths, UpdatedQueue),
    bfs_util(UpdatedQueue, Goal, Path).
