% Facts
student(rahul, it, 8.5).
student(priya, cs, 9.1).
student(amit, it, 7.2).
student(sneha, cs, 8.9).
student(karan, it, 6.5).

% Rules
is_it_student(X) :-
    student(X, it, _).

is_topper(X) :-
    student(X, _, CGPA),
    CGPA >= 9.0.

eligible_for_placement(X) :-
    student(X, _, CGPA),
    CGPA >= 7.0.

low_performer(X) :-
    student(X, _, CGPA),
    CGPA < 7.0.
