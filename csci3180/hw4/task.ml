(* Insert header here *)
(* 
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
*)
val tasks = [
  ("t1", 2, 4),
  ("t2", 4, 6),
  ("t3", 3, 7),
  ("t4", 8, 9),
  ("t5", 1, 10),
  ("t6", 10, 1)
];
val A= 1
val B= 10
val C= 2
val D= 3

(* 1a *)
fun check_task(T:string, tasklist:(string * int * int) list)=
	if null tasklist
	then false
	else if #1 (hd tasklist)= T 
	then if #3 (hd tasklist) >= #2 (hd tasklist)
		then true
		else false
	else check_task(T , tl tasklist);
(* example query: check_task("t1", tasks); *)
(* result: val it = true : bool *)
(*ML: check task(T:string, tasklist:(string * int * int) list):bool*)
(*i.e. val check task = fn : string * (string * int * int) list -> bool*)
(*check_task("t10",tasks);*)
check_task("t1",tasks);
check_task("t6",tasks);
check_task("t7",tasks);
(* 1b *)
fun return(T:string, tasklist:(string * int * int) list)=
	if null tasklist
	then ("no",0,0)
	else if #1 (hd tasklist)= T
	then if #3 (hd tasklist) >= #2 (hd tasklist)
		then hd tasklist
		else ("no",0,0)
	else return(T , tl tasklist);

return("t1",tasks);
return("t2",tasks);
return("t6",tasks);
return("t7",tasks);

fun compatible(T1:string, T2:string, tasklist:(string * int * int) list)=
  let
  	val (h1,h2,h3) = return(T1,tasklist) 
  	val (t1,t2,t3) = return(T2,tasklist) 
  in
  	if  h1 = "no"
  	then false
  	else if t1 = "no"
  		then false
  		else if h2 >= t3
  			then true
  			else if t2 >= h3
  				then true
  				else false

  end ;

compatible("t1","t2",tasks);
compatible("t2","t3",tasks);
(* example query: compatible("t1", "t2", tasks); *)
(* result: val it = true : bool *)
(*ML: compatible(T1:string, T2:string, tasklist:(string * int * int) list):bool,*)
(*i.e. val compatible = fn : string * string * (string * int * int) list-> bool)*)

(* 1c *)

fun sum(List : string list,List2: string list)=
	if null List 
	then []
	else if null List2
	then if null (tl (tl List))
		then []
			else
				sum(tl List,tl (tl List))
	else
		(hd List,hd List2)::sum(List,tl List2);
sum(["t1","t2","t3","t4"],["t2","t3","t4"]);

fun check(Loop:(string*string) list,tasklist: (string * int * int) list)=
		if null Loop
		then true
		else if compatible(#1 (hd Loop),#2 (hd Loop),tasklist)
			then check(tl Loop,tasklist)
			else false;

fun compatible_list(L: string list, tasklist: (string * int * int) list)=
	let
		val List = sum(L,tl(L))
	in
		if check(List,tasklist)
		then true
		else false
	end ;
compatible_list(["t1", "t2", "t3"], tasks);
compatible_list(["t1", "t2", "t4"], tasks);
(* example query: compatible_list(["t1", "t2", "t3"], tasks); *)
(*ML: compatible list(L: string list, tasklist: (string * int * int) list):bool*)
(*i.e. val compatible list = fn : string list * (string * int * int) list*)
(* result: val it = false : bool *)

