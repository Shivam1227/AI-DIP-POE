% Graph
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).
edge(e, f).

% Path finding
path(Start, End, Path) :-
    travel(Start, End, [Start], Path).

travel(End, End, Visited, Path) :-
    reverse(Visited, Path).

travel(Current, End, Visited, Path) :-
    edge(Current, Next),
    \+ member(Next, Visited),
    travel(Next, End, [Next|Visited], Path).
