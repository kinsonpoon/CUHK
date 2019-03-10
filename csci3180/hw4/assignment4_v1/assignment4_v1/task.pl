/* Insert header here */


append([],Y,Y).
append([H|T],Y,[H|Z]):- append(T,Y,Z).

intersection([X|Y],M,[X|Z]) :- member(X,M), intersection(Y,M,Z).
intersection([X|Y],M,Z) :- \+ member(X,M), intersection(Y,M,Z).
intersection([],M,[]).

compare(T1,T2):- not(T1=T2),task(T1,Start1,End1),task(T2,Start2,End2),(Start2>=End1;Start1>=End2).


task(t1, 2, 4).
task(t2, 4, 6).
task(t3, 3, 7).
task(t4, 8, 9).
task(t5, 1, 10).
task(t6, 10, 1).


/* 1a */
check_task(T):- task(T,Start,End),End>=Start.
/* example query: check_task(t1);
   result: yes */

/* 1b */
compatible(T1,T2):- check_task(T1),check_task(T2),compare(T1,T2).
/* example query: compatible(t1, t2);
   result: yes */

/* 1c */
member(Head,[Head|Tail]).
member(O,[Head|Tail]):-member(O,Tail).

fuck([X|Y],M,[H|T]):-member(X,T),compatible(X,H),fuck(M,M,[Y]).
fuck([X|Y],[]):-fuck([Y],[Y],[Y]).
fuck([],[],[]).

pairs([A|T],[A,B]) :- member(B,T).
pairs([_|T],[A,B]) :- pairs(T,[A,B]).


xdd([H,T]) :- compatible(H,T).
dosomething([]).
dosomething([H|T]) :- xdd(H), dosomething(T).

compatible_list(List):-findall(X,pairs(List,X),L),dosomething(L).


/** example query: compatible_list([t1, t2, t3]);
   result: no */

