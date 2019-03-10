000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. HELLO.
      *
      *
      * CSCI3180 Principles of Programming Languages
      *
      * --- Declaration ---
      *
      * I declare that the assignment here submitted is original except for source
      * material explicitly acknowledged. I also acknowledge that I am aware of
      * University policy and regulations on honesty in academic work, and of the
      * disciplinary guidelines and procedures applicable to breaches of such policy
      * and regulations, as contained in the website
      * http://www.cuhk.edu.hk/policy/academichonesty/
      *
      * Assignment 1
      * Name : Poon King Hin
      * Student ID : 1155077526
      * Email Addr : khpoon6@cse.cuhk.edu.com
      *
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
000043     SELECT IN-FILE
000044         ASSIGN TO 'teams.txt'
000045         ORGANIZATION IS LINE SEQUENTIAL.
000043     SELECT INPUT-FILE
000044         ASSIGN TO 'submission-records.txt'
000045         ORGANIZATION IS LINE SEQUENTIAL.
000043     SELECT OUT-FILE
               ASSIGN TO 'reportcob.txt'
000045         ORGANIZATION IS LINE SEQUENTIAL.
000050*
000060 DATA DIVISION.
000061 FILE SECTION.
000062 FD IN-FILE.
       01 NAM PIC X(15).
       FD INPUT-FILE.
           01 TEAM-DATA.
              03 NAM2 PIC X(15).
              03 IDD PIC 9.
              03 OUTCOME PIC X(19).
              03 SCORE PIC 9(3).
       FD OUT-FILE.

           01 PRINTLINE.
               03 P1 PIC X(15).
               03 P2 PIC X(4).
               03 P3 PIC ZZ9.
               03 P4 PIC X(4).
               03 P5 PIC ZZ9.
               03 P6 PIC X(4).
               03 P7 PIC ZZ9.
               03 P8 PIC X(4).
               03 P9 PIC ZZ9.
               03 P10 PIC X(4).
               03 P11 PIC ZZ9.
               03 P12 PIC X(4).
               03 P13 PIC ZZ9.
               03 P14 PIC X(4).
               03 P15 PIC ZZ9.
               03 P16 PIC X(4).
               03 P17 PIC ZZ9.
               03 P18 PIC X(4).
               03 P19 PIC ZZ9.
               03 P20 PIC X(4).
               03 P21 PIC ZZ9.
               03 P22 PIC X(3).
               03 P23 PIC ZZZ9.
               03 P24 PIC X.

           01 FIRR.
               03 FIR PIC X(33).
               03 F1 PIC X.
           01 SECC.
              03 SEC PIC X(17).
              03 S1 PIC X.
           01 THII.
              03 THI PIC X(1).
              03 T1 PIC X.

000000*
000000*
000000*
000000*
000000*
000000*
000000*
000000 WORKING-STORAGE SECTION.
000000     01  UPDATE-DATA.
               03 MAX PIC 999.
               03 MIN PIC 999.
               03 BASE PIC 999.
               03 SCORESUM PIC 999.
               03 NSUB PIC 99.
03         01  SUMOUT.
               03 SOUT PIC 999 OCCURS 10 TIMES.
           01  NUMBER-NOW PIC 9.
           01  DECAY PIC 9V99.
           01  ROBUST PIC 999.
           01  TSCORE PIC 9999.
           01 OUTSCORE PIC Z9999.
000000*
000000*
000000*
000000*
000000*
000180 PROCEDURE DIVISION.
000181* MAIN PROGRAM
000190 MAIN-PARAGRAPH.
000200     OPEN INPUT IN-FILE.
           OPEN INPUT INPUT-FILE.
           OPEN OUTPUT OUT-FILE.
           MOVE 0 TO NUMBER-NOW.
      *    DISPLAY '2018 CUHK CSE Programming Contest'.
      *    DISPLAY 'Team Score Report'.
      *    DISPLAY ' '.
           MOVE '2018 CUHK CSE Programming Contest' TO FIR.
           MOVE X'0D' TO F1.
           WRITE FIRR.
           MOVE 'Team Score Report' TO SEC.
           MOVE X'0D' TO S1.
           WRITE SECC.
           MOVE ' ' TO THI.
           MOVE X'0D' TO T1.
           WRITE THII.



           GO TO READ-TEAM.
       READ-TEAM.
           READ IN-FILE INTO NAM
             AT END  GO TO TEAM-END.
      *       DISPLAY NAM.

             GO TO READ-RECORD.
       READ-RECORD.
           READ INPUT-FILE INTO TEAM-DATA
               AT END  GO TO RESET-ALL.

               IF NAM = NAM2 THEN
      *             DISPLAY TEAM-DATA
                   GO TO NUMBER-CHECK
               END-IF.
               GO TO READ-RECORD.
       TEAM-END.
           CLOSE IN-FILE.
           CLOSE INPUT-FILE.
           CLOSE OUT-FILE.
           STOP RUN.
       RECORD-END.
           CLOSE INPUT-FILE.
           OPEN INPUT INPUT-FILE.
           GO TO READ-TEAM.
       NUMBER-CHECK.
             IF IDD = NUMBER-NOW THEN
               GO TO UPDATE-SUB
             END-IF.
             GO TO CAL-SUB.
       CAL-SUB.
      *     DISPLAY NSUB,MAX,MIN,SCORESUM,BASE.
           IF MAX <= 30 THEN
               MOVE 0 TO ROBUST
           END-IF.
           IF MAX >30 THEN
               COMPUTE ROBUST= 100 - MAX + MIN
           END-IF.
           MOVE 1 TO DECAY.
           IF BASE NOT = 100 THEN
              COMPUTE DECAY = 1 / NSUB
           END-IF.
           COMPUTE SOUT(NUMBER-NOW + 1)=0.6 * BASE * DECAY +
                   0.3 * SCORESUM / NSUB + 0.1 * ROBUST.
      *     DISPLAY NAM,SOUT(NUMBER-NOW + 1).
           GO TO RESET-SUB.
       UPDATE-SUB.
           COMPUTE NSUB = NSUB + 1 .
           ADD SCORE TO SCORESUM GIVING SCORESUM.
           MOVE SCORE TO BASE.
           IF NSUB = 1 THEN
               MOVE SCORE TO MAX
               MOVE SCORE TO MIN
               GO TO READ-RECORD
           END-IF.
           IF SCORE >= MAX THEN
               MOVE SCORE TO MAX
               GO TO READ-RECORD
           END-IF.
           IF SCORE <= MIN THEN
               MOVE SCORE TO MIN
               GO TO READ-RECORD
           END-IF.
           GO TO READ-RECORD.
       RESET-SUB.
           MOVE 0 TO NSUB.
           MOVE 0 TO MAX.
           MOVE 0 TO MIN.
           MOVE 0 TO SCORESUM.
           MOVE 0 TO BASE.
           MOVE IDD TO NUMBER-NOW.
           GO TO UPDATE-SUB.
       RESET-ALL.
      *     DISPLAY NSUB,MAX,MIN,SCORESUM,BASE.
           IF MAX <= 30 THEN
               MOVE 0 TO ROBUST
           END-IF.
           IF MAX >30 THEN
               COMPUTE ROBUST= 100 - MAX + MIN
           END-IF.
           MOVE 1 TO DECAY.
           IF BASE NOT = 100 THEN
              COMPUTE DECAY = 1 / NSUB
           END-IF.

           COMPUTE SOUT(NUMBER-NOW + 1)=0.6 * BASE * DECAY +
                   0.3 * SCORESUM / NSUB + 0.1 * ROBUST.
           COMPUTE TSCORE = SOUT(1) + SOUT(2) + SOUT(3) + SOUT(4) +
                    + SOUT(5) + SOUT(6) + SOUT(7) + SOUT(8) + SOUT(9)+
                     + SOUT(10).
      *     DISPLAY NAM,' (0)', SOUT(1),' (1)',SOUT(2),' (2)',SOUT(3),
      *             ' (3)',SOUT(4),' (4)',SOUT(5),' (5)',SOUT(6),
      *             ' (7)',SOUT(8),' (8)',SOUT(9),' (9)',SOUT(10),
      *             ' T:',TSCORE.
           MOVE NAM TO P1.
           MOVE ' (0)' TO P2.
           MOVE SOUT(1) TO P3.
           MOVE ' (1)' TO P4.
           MOVE SOUT(2) TO P5.
           MOVE ' (2)' TO P6.
           MOVE SOUT(3) TO P7.
           MOVE ' (3)' TO P8.
           MOVE SOUT(4) TO P9.
           MOVE ' (4)' TO P10.
           MOVE SOUT(5) TO P11.
           MOVE ' (5)' TO P12.
           MOVE SOUT(6) TO P13.
           MOVE ' (6)' TO P14.
           MOVE SOUT(7) TO P15.
           MOVE ' (7)' TO P16.
           MOVE SOUT(8) TO P17.
           MOVE ' (8)' TO P18.
           MOVE SOUT(9) TO P19.
           MOVE ' (9)' TO P20.
           MOVE SOUT(10) TO P21.
           MOVE ' T:' TO P22.
           MOVE TSCORE TO P23.
           MOVE X'0D' TO P24.
           WRITE PRINTLINE.

           MOVE 0 TO NSUB.
           MOVE 0 TO MAX.
           MOVE 0 TO MIN.
           MOVE 0 TO SCORESUM.
           MOVE 0 TO BASE.
           MOVE 0 TO NUMBER-NOW.
           MOVE 0 TO SOUT(1).
           MOVE 0 TO SOUT(2).
           MOVE 0 TO SOUT(3).
           MOVE 0 TO SOUT(4).
           MOVE 0 TO SOUT(5).
           MOVE 0 TO SOUT(6).
           MOVE 0 TO SOUT(7).
           MOVE 0 TO SOUT(8).
           MOVE 0 TO SOUT(9).
           MOVE 0 TO SOUT(10).
           MOVE 0 TO TSCORE.
           GO TO RECORD-END.
