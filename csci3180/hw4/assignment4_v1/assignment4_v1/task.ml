(* Insert header here *)
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
val tasks = [
  ("t1", 2, 4),
  ("t2", 4, 6),
  ("t3", 3, 7),
  ("t4", 8, 9),
  ("t5", 1, 10),
  ("t6", 10, 1)
];


(* 1a *)
fun check_task(T:string, tasklist:(string * int * int) list)=
	if null tasklist
	then false
	else if #1 (hd tasklist)= T
	then true
	else check_task(T , tl tasklist)
(* example query: check_task("t1", tasks); *)
(* result: val it = true : bool *)
(*ML: check task(T:string, tasklist:(string * int * int) list):bool*)
(*i.e. val check task = fn : string * (string * int * int) list -> bool*)
(*check_task("t10",tasks);*)

fun compare(T:string, tasklist:(string * int * int) list,Y:int,Z:int)
  if null tasklist
  then false
  else if #1 (hd tasklist)= T
  then true
  else check_task(T , tl tasklist,#2 hd(tl tasklist),#3 hd(tl tasklist))
(* 1b *)
fun compatible(T1:string, T2:string, tasklist:(string * int * int) list))=
  let val A=1
      val B=10
      val C=2
      val D=3
  if null tasklist
  then false
  else if check_task(T1,tasklist,A,B) and check_task(T2,tasklist,C,D) and (C>=B | A>=D)
  then true
  else
  false

(* example query: compatible("t1", "t2", tasks); *)
(* result: val it = true : bool *)
(*ML: compatible(T1:string, T2:string, tasklist:(string * int * int) list):bool,*)
(*i.e. val compatible = fn : string * string * (string * int * int) list-> bool)*)

(* 1c *)
(* fun compatible_list()*)
(* example query: compatible_list(["t1", "t2", "t3"], tasks); *)
(* result: val it = false : bool *)

