% Facts
male(john).
male(paul).
male(mike).
male(david).

female(lisa).
female(susan).
female(anna).
female(kate).

parent(john, paul).
parent(john, lisa).
parent(susan, paul).
parent(susan, lisa).

parent(paul, mike).
parent(paul, anna).
parent(lisa, david).
parent(lisa, kate).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    male(X),
    grandparent(X, Y).

grandmother(X, Y) :-
    female(X),
    grandparent(X, Y).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
