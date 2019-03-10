/* Insert header here */
/* 
 CSCI3180 Principles of Programming Languages

 --- Declaration ---

 I declare that the assignment here submitted is original except for source
 material explicitly acknowledged. I also acknowledge that I am aware of
 University policy and regulations on honesty in academic work, and of the
 disciplinary guidelines and procedures applicable to breaches of such policy
and regulations, as contained in the website
 http://www.cuhk.edu.hk/policy/academichonesty/

 Assignment 4
 Name : Poon King Hin
 Student ID : 1155077526
 Email Addr : khpoon6@cse.cuhk.edu.hk
*/

/* 1a */
uint_num(0).
uint_num(s(X)):- uint_num(X).

/* 1b */
gt(suc(_), 0).
gt(suc(X), suc(Y)) :- gt(X,Y).

/* 1c */
/* Your query 
?- gt(suc(suc(suc(0))),N).
*/

/* 1d */
sum(0,X,X).
sum(s(X),Y,Z) :- sum(X,s(Y),Z).
product(0,_,0).
product(s(X),Y,Z) :- product(X,Y,N) , sum(Y,N,Z).

/* 1e */
/* Your query 
?- product(s(s(0)),s(s(s(0))),N).
*/

/* 1f */
/* Your query 
?- product(N,s(s(s(s(0)))), s(s(s(s(s(s(s(s(0))))))))).
*/

/* 2a */
nth(X,[X|_],1).
nth(X,[_|L],K) :- nth(X,L,K1), K is K1 + 1.


/* 2b */
third(X,L):-nth(X,L,3).

