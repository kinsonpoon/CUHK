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
(* 1a *)
(*(\c.c(\a.\b.b))((\a.\b.\f.f a b)p q)*)
(*⇒B(λa.λb.λf.f a b) p q (λa.λb.b)*)
(*⇒B(λb.λf.f p b) q (λa.λb.b)*)
(*⇒B(λf.f p q) (λa.λb.b)*)
(*⇒B(λa.λb.b) p q*)
(*⇒B(λb.b) q*)
(*⇒B q*)
(* 1b *)
(*(\c.c(\a.\b.b))((\a.\b.\f.f a b)p q)*)
(*((\a.\b.\f.f a b)p q(\c.c(\a.\b.b))*)
(*⇒B((\b.\f.f p b)q(\c.c(\a.\b.b))*)
(*⇒B((.\f.f p q)(\c.c(\a.\b.b))*)
(*⇒B (\a.\b.b)p q*)
(*⇒B (\b.b)q*)
(*⇒B q*)
(* 2a *)
(* (\x.\y.(mul x((\x.(add x 3))y)))7 8 *)
(*⇒ a(\x.\y.(mul x(\x'.(add x' 3)y)))7 8 *)
(*⇒ B(\y.(mul 7(\x'.(add x' 3)y)))8 *)
(*⇒ B((mul 7(\x'.(add x' 3))8))*)
(*⇒ δ(7*(\x'.(add x' 3))8)*)
(*⇒ B(7*(add 8 3))*)
(*⇒ δ(7*11)*)
(*⇒ 77*)
(* 2b *)
(* (\x.\y.(mul x((\x.(add x 3))y)))7 8 *)
(*⇒δ(\x.\y.(mul x((\x.(x+3))y)))7 8 *)
(*⇒a(\x'.\y.(mul x'((\x.(x+3))y)))7 8 *)
(*⇒B(\x'.\y.(mul x'((7+3))y)) 8 *)
(*⇒(\x'.\y.(mul x'(10)y)) 8 *)
(*⇒δ(\x'.\y.(x'* 10)y) 8 *)
(*⇒B(\y.(8* 10)y)*)
(*⇒B(\y.(80)y)*)
(*⇒B 80*)
(* 2c *)
fun f (X:int) (Y:int)=X*(Y+3); 
f 7 8;
(* λx.λy.mul x (add y 3)*)
(* Example query: f 7 8 *)
(*3a*)
(*First printf:2 *)
(*because m=1, k=f1=1+1=2 *)
(*Second printf:8 *)
(*because m=f2=5(λx.(x+3))=5+3=8 *)
(*Third printf:8 *)
(*because swap(k,m),k->m=8*)
(*Forth printf:8 *)
(*because the function loop doesn't change the value of k*)
(*3b*)
(*yes,because eval normal is the same as normal subsuition*)
(*3c*)
(*their life time will be only in the running time of function swap, because they are create as local varible in the function swap, and will be killed when the function swap is finished*)
(*3d*)
(*Static scoping*)
(*because i think this project will build funciton based on many sub function,and many variable with the same and similar name*)
(*therefore i think it is much better to use Static scoping,as to enhance readability, and prevent bugs *)