member(Head,[Head|Tail]).
member(O,[Head|Tail]):-member(O,Tail).

append([],Y,Y).
append([H|T],Y,[H|Z]):- append(T,Y,Z).

lists_concatenatedTails([],[]).
lists_concatenatedTails([[_|Xs0]|Xss],Ys) :-
    append(Xs0,Ys0,Ys),
    lists_concatenatedTails(Xss,Ys0).


intersection([X|Y],M,[X|Z]) :- member(X,M), intersection(Y,M,Z).
intersection([X|Y],M,Z) :- \+ member(X,M), intersection(Y,M,Z).
intersection([],M,[]).

check([],_,0).
check([H|T],List,X):-member(H,List),check(T,List,Y),X is Y + 1.
check([H|T],List,Y):-not(member(H,List)),check(T,List,Y).

count(_,_,[],0).
count(T,R,[A|B],Num):-check(T,A,4),check(R,A,0),count(T,R,B,Num2),Num is Num2 + 1.
count(T,R,[A|B],Num):-not((check(T,A,4),check(R,A,0))),count(T,R,B,Num).

threatening(board(Blackb,Redb),black,C):-count(Redb,Blackb,[[1,7,13,19,25],[5,11,17,23,29],[8,9,10,11,12],[13,14,15,16,17],[1,2,3,4,5],[5,10,15,20,25],[8,15,22,29,36],[14,15,16,17,18],[1,8,15,22,29],[6,12,18,24,30],[9,15,21,27,33],[19,20,21,22,23],[2,8,14,20,26],[6,11,16,21,26],[10,16,22,28,34],[20,21,22,23,24],[2,3,4,5,6],[7,13,19,25,31],[11,17,23,29,35],[25,26,27,28,29],[2,9,16,23,30],[7,8,9,10,11],[11,16,21,26,31],[26,27,28,29,30],[3,9,15,21,27],[7,14,21,28,35],[12,18,24,30,36],[31,32,33,34,35],[4,10,16,22,28],[8,14,20,26,32],[12,17,22,27,32],[32,33,34,35,36]],C).
threatening(board(Blackb,Redb),red,C):-count(Blackb,Redb,[[1,7,13,19,25],[5,11,17,23,29],[8,9,10,11,12],[13,14,15,16,17],[1,2,3,4,5],[5,10,15,20,25],[8,15,22,29,36],[14,15,16,17,18],[1,8,15,22,29],[6,12,18,24,30],[9,15,21,27,33],[19,20,21,22,23],[2,8,14,20,26],[6,11,16,21,26],[10,16,22,28,34],[20,21,22,23,24],[2,3,4,5,6],[7,13,19,25,31],[11,17,23,29,35],[25,26,27,28,29],[2,9,16,23,30],[7,8,9,10,11],[11,16,21,26,31],[26,27,28,29,30],[3,9,15,21,27],[7,14,21,28,35],[12,18,24,30,36],[31,32,33,34,35],[4,10,16,22,28],[8,14,20,26,32],[12,17,22,27,32],[32,33,34,35,36]],C).

get(_,_,[],0).
get(T,R,[A|B],String):-check(T,A,4),check(R,A,0),String = A.
get(T,R,[A|B],String):-not((check(T,A,4),check(R,A,0))),get(T,R,B,String).


win(Blackb,Redb,String):-get(Blackb,Redb,[[1,7,13,19,25],[5,11,17,23,29],[8,9,10,11,12],[13,14,15,16,17],[1,2,3,4,5],[5,10,15,20,25],[8,15,22,29,36],[14,15,16,17,18],[1,8,15,22,29],[6,12,18,24,30],[9,15,21,27,33],[19,20,21,22,23],[2,8,14,20,26],[6,11,16,21,26],[10,16,22,28,34],[20,21,22,23,24],[2,3,4,5,6],[7,13,19,25,31],[11,17,23,29,35],[25,26,27,28,29],[2,9,16,23,30],[7,8,9,10,11],[11,16,21,26,31],[26,27,28,29,30],[3,9,15,21,27],[7,14,21,28,35],[12,18,24,30,36],[31,32,33,34,35],[4,10,16,22,28],[8,14,20,26,32],[12,17,22,27,32],[32,33,34,35,36]],String).

place([H|T],X,Z):-member(H,X),place(T,X,Z).
place([H|T],X,Z):-not(member(H,X)),Z=H.

ai(board(Blackb,Redb),red, BestMove):-win(Redb,Blackb,String),place(String,Redb,Z),BestMove is Z.
ai(board(Blackb,Redb),black, BestMove):-win(Blackb,Redb,String),place(String,Blackb,Z),BestMove is Z.

diff([],M, []).
diff([H|T],M, Z) :- member(H,M),diff(T,M,Z).
diff([H|T],M, [H|Z]) :- not(member(H,M)),diff(T,M,Z).




change_tlc(Before,After):-turn(Before,[[1,3],[2,9],[3,15],[7,2],[9,14],[13,1],[14,7],[15,13]],After).
change_tla(Before,After):-turn(Before,[[1,13],[2,7],[3,1],[7,14],[9,2],[13,15],[14,9],[15,3]],After).

change_trc(Before,After):-turn(Before,[[4,6],[5,12],[6,18],[10,5],[12,17],[16,4],[17,10],[18,16]],After).
change_tra(Before,After):-turn(Before,[[4,16],[5,10],[6,4],[10,17],[12,5],[16,18],[17,12],[18,6]],After).



change_blc(Before,After):-turn(Before,[[19,21],[20,27],[21,33],[25,20],[27,32],[31,16],[32,25],[33,31]],After).
change_bla(Before,After):-turn(Before,[[19,31],[20,25],[21,19],[25,32],[27,20],[31,33],[32,27],[33,21]],After).

change_brc(Before,After):-turn(Before,[[22,24],[23,30],[24,36],[28,23],[30,35],[34,22],[35,28],[36,34]],After).
change_bra(Before,After):-turn(Before,[[22,34],[23,28],[24,22],[28,35],[30,23],[34,36],[35,30],[36,24]],After).


turn(Before,[[X|Y]|Lt],[Y|B]):- member(X,Before),turn(Before,Lt,B).
turn(Before,[[X|Y]|Lt],B):- not(member(X,Before)),turn(Before,Lt,B).
turn(Before,[],[]).



rotate(Sandwish,Piece,Direction,Result):-Piece=top-left,Direction=clockwise,diff(Sandwish,[1,2,3,7,9,13,14,15],Difference),intersection(Sandwish,[1,2,3,7,9,13,14,15],Common),change_tlc(Common,L),flatten(L,After),append(Difference,After,Result).
rotate(Sandwish,Piece,Direction,Result):-Piece=top-left,Direction=anti-clockwise,diff(Sandwish,[1,2,3,7,9,13,14,15],Difference),intersection(Sandwish,[1,2,3,7,9,13,14,15],Common),change_tla(Common,L),flatten(L,After),append(Difference,After,Result).

rotate(Sandwish,Piece,Direction,Result):-Piece=top-right,Direction=clockwise,diff(Sandwish,[4,5,6,10,12,16,17,18],Difference),intersection(Sandwish,[4,5,6,10,12,16,17,18],Common),change_trc(Common,L),flatten(L,After),append(Difference,After,Result).
rotate(Sandwish,Piece,Direction,Result):-Piece=top-right,Direction=anti-clockwise,diff(Sandwish,[4,5,6,10,12,16,17,18],Difference),intersection(Sandwish,[4,5,6,10,12,16,17,18],Common),change_tra(Common,L),flatten(L,After),append(Difference,After,Result).

rotate(Sandwish,Piece,Direction,Result):-Piece=bottom-left,Direction=clockwise,diff(Sandwish,[19,20,21,25,27,31,32,33],Difference),intersection(Sandwish,[19,20,21,25,27,31,32,33],Common),change_blc(Common,L),flatten(L,After),append(Difference,After,Result).
rotate(Sandwish,Piece,Direction,Result):-Piece=bottom-left,Direction=anti-clockwise,diff(Sandwish,[19,20,21,25,27,31,32,33],Difference),intersection(Sandwish,[19,20,21,25,27,31,32,33],Common),change_bla(Common,L),flatten(L,After),append(Difference,After,Result).

rotate(Sandwish,Piece,Direction,Result):-Piece=bottom-right,Direction=clockwise,diff(Sandwish,[22,23,24,28,30,34,35,36],Difference),intersection(Sandwish,[22,23,24,28,30,34,35,36],Common),change_brc(Common,L),flatten(L,After),append(Difference,After,Result).
rotate(Sandwish,Piece,Direction,Result):-Piece=bottom-right,Direction=anti-clockwise,diff(Sandwish,[22,23,24,28,30,34,35,36],Difference),intersection(Sandwish,[22,23,24,28,30,34,35,36],Common),change_bra(Common,L),flatten(L,After),append(Difference,After,Result).


tryhard(board(Blackb,Redb),red,Piece,Direction,Reverse, BestMove,NextBoard):-rotate(Blackb,Piece,Direction,B),rotate(Redb,Piece,Direction,R),ai(board(B,R),red, Best),rotate([Best],Piece,Reverse,Cry),[Laugh]=Cry,BestMove=move(Laugh,Direction,Piece),append(R,[Best],Xd),NextBoard=board(B,Xd).

tryhard(board(Blackb,Redb),black,Piece,Direction,Reverse, BestMove,NextBoard):-rotate(Blackb,Piece,Direction,B),rotate(Redb,Piece,Direction,R),ai(board(B,R),black, Best),rotate([Best],Piece,Reverse,Cry),[Laugh]=Cry,BestMove=move(Laugh,Direction,Piece),append(B,[Best],Xd),NextBoard=board(Xd,R).


notlose(board(Blackb,Redb),black,Piece,Direction,Reverse, BestMove,NextBoard):-rotate(Blackb,Piece,Direction,B),rotate(Redb,Piece,Direction,R),ai(board(B,R),red, Best),rotate([Best],Piece,Reverse,Cry),[Laugh]=Cry,BestMove=move(Laugh,Direction,Piece).
notlose(board(Blackb,Redb),red,Piece,Direction,Reverse, BestMove,NextBoard):-rotate(Blackb,Piece,Direction,B),rotate(Redb,Piece,Direction,R),ai(board(B,R),black, Best),rotate([Best],Piece,Reverse,Cry),[Laugh]=Cry,BestMove=move(Laugh,Direction,Piece).


pentago_ai(board(Blackb,Redb),red, BestMove,NextBoard):-tryhard(board(Blackb,Redb),red,_,clockwise,anti-clockwise, BestMove,NextBoard).
pentago_ai(board(Blackb,Redb),red, BestMove,NextBoard):-tryhard(board(Blackb,Redb),red,_,anti-clockwise,clockwise, BestMove,NextBoard).

pentago_ai(board(Blackb,Redb),black, BestMove,NextBoard):-tryhard(board(Blackb,Redb),black,_,clockwise,anti-clockwise, BestMove,NextBoard).
pentago_ai(board(Blackb,Redb),black, BestMove,NextBoard):-tryhard(board(Blackb,Redb),black,_,anti-clockwise,clockwise, BestMove,NextBoard).

pentago_ai(board(Blackb,Redb),black, BestMove,NextBoard):-notlose(board(Blackb,Redb),black,_,clockwise,anti-clockwise, BestMove,NextBoard).
pentago_ai(board(Blackb,Redb),black, BestMove,NextBoard):-notlose(board(Blackb,Redb),black,_,anti-clockwise,clockwise, BestMove,NextBoard).

pentago_ai(board(Blackb,Redb),red, BestMove,NextBoard):-notlose(board(Blackb,Redb),red,_,clockwise,anti-clockwise, BestMove,NextBoard).
pentago_ai(board(Blackb,Redb),red, BestMove,NextBoard):-notlose(board(Blackb,Redb),red,_,anti-clockwise,clockwise, BestMove,NextBoard).

pentago_ai(board(Blackb,Redb),red, BestMove,NextBoard):-notlose(board(Blackb,Redb),red,_,clockwise,anti-clockwise, BestMove,NextBoard).
pentago_ai(board(Blackb,Redb),red, BestMove,NextBoard):-notlose(board(Blackb,Redb),red,_,anti-clockwise,clockwise, BestMove,NextBoard).

pentago_ai(board(Blackb,Redb),black, BestMove,NextBoard):-notlose(board(Blackb,Redb),black,_,clockwise,anti-clockwise, BestMove,NextBoard).
pentago_ai(board(Blackb,Redb),black, BestMove,NextBoard):-notlose(board(Blackb,Redb),black,_,anti-clockwise,clockwise, BestMove,NextBoard).


random([H|T],M, Z) :- member(H,M),diff(T,M,Z).
random([H|T],M, Z) :- not(member(H,M)),Z = H.

pentago_ai(board(Blackb,Redb),black,BestMove,NextBoard):-BestMove=move(3,clockwise,top-left).
pentago_ai(board(Blackb,Redb),red,BestMove,NextBoard):-BestMove=move(3,clockwise,top-left).





