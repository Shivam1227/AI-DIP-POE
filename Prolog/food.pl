likes(john, pizza).
likes(john, burger).
likes(mary, salad).
likes(mary, pizza).
likes(david, burger).

vegetarian(salad).
vegetarian(pizza).

foodie(X) :-
    likes(X, pizza),
    likes(X, burger).

veg_lover(X) :-
    likes(X, Food),
    vegetarian(Food).

common_food(X, Y, Food) :-
    likes(X, Food),
    likes(Y, Food).
