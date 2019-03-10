C My first program
C print out hello world
      PROGRAM Helloworld
C force explicit type declarations
      IMPLICIT NONE
C variable declaration
      CHARACTER team*15,twk*15
      CHARACTER subname*15
      CHARACTER*1 blank
      CHARACTER*19 stage
      INTEGER count,ios,ios2,ctr,start,counter2,nSUB,sat,hi
	    INTEGER basescore,scoresum,maxscore,minscore,robust,initial
	    INTEGER S(10),st,numnow,decayint
	    REAL decay
	    CHARACTER*4 qt
	    CHARACTER*4 q0,q1,q2,q3,q4,q5,q6,q7,q8,q9
      CHARACTER*9 file1
      CHARACTER*22 file2
      CHARACTER*1 r
      INTEGER num,score
      r=char(13)
      read(*,'(A)') file1
      read(*,'(A)') file2
	    
	    open (unit=7,IOSTAT=ios,ERR=999,FILE=file1,STATUS ='OLD')
	    open (unit=8,IOSTAT=ios2,ERR=999,FILE=file2,
     +        STATUS ='OLD')
      open (unit=9,FILE='reportfor.txt',STATUS='NEW')
      
	  
C program statement
C--FORMAT----------
 10      FORMAT(A)
 11      FORMAT(A,I1,A,I3)
 12      FORMAT(A,A1)
 13      FORMAT(A1)
 123     FORMAT(A,A,I3,A,I3,A,I3,A,I3,A,I3,A,I3,A,I3,A,I3,A,I3,A,
     +         I3,A,I3,A1)
C---INITIAL-------------
      q0 = ' (0)'
	    q1 = ' (1)'
	    q2 = ' (2)'
	    q3 = ' (3)'
	    q4 = ' (4)'
	    q5 = ' (5)'
	    q6 = ' (6)'
	    q7 = ' (7)'
	    q8 = ' (8)'
	    q9 = ' (9)'
	    qt = ' T:'
	    initial=0
	    maxscore=0
	    minscore=0
C	    WRITE(*,'(A)')'2018 CUHK CSE Programming Contest'
C	    WRITE(*,'(A)')'Team Score Report'
C	    WRITE(*,'(A)')r
C-----
        WRITE(9,12)'2018 CUHK CSE Programming Contest',r
	    WRITE(9,12)'Team Score Report',r
	    WRITE(9,13)r
C-----------------------readteam---
 1     read(7,'(A)',IOSTAT=ios,END=2) team
C       WRITE(*,'(A)') team
C       WRITE(*,'(I1)') ios
       IF(ios .EQ. 0) GOTO 2
c       IF(ios .NE. 0) GOTO 999
       
       
C----------------------READ-RECORD-
 2    read(8,'(A,I1,A,I3)',IOSTAT=ios2,END=51)subname,num,stage,score
c      IF(ios2 .NE. 0) GOTO 51
      IF( team .EQ. subname) GOTO 20
      
	    GOTO 2
C-------CHECK-Q-NUM
 20    IF(numnow .EQ. num) GOTO 25
       GOTO 21
C----CAL-SUB
 21   decay=1
      IF(NSUB .NE. 1) THEN
      decay=REAL(1/REAL(NSUB))
      decay=decay*100
      decayint=NINT(decay)
      decay=REAL(REAL(decayint)/100)
      ENDIF
      
C      WRITE(*,'(F6.5)') decay
      robust=100-maxscore+minscore
      IF(maxscore .LE. 30) THEN
        robust=0
      ENDIF
      IF(maxscore .EQ. 100) THEN
         decay=1
      ENDIF
C      WRITE(*,'(I3)') robust 
      hi=0.6*basescore*decay+0.3* scoresum/NSUB+0.1*robust 
c      WRITE(*,'(A,I3,I4)') team,numnow,hi
      
C      WRITE(*,'(A,I3,I3,I5,I5,I5,I5)') team,numnow, NSUB,basescore,
C     +       scoresum,maxscore,minscore
      S(numnow + 1)=hi
	    NSUB=0
      numnow=num
      basescore=0
      scoresum=0
      maxscore=0
      minscore=0
	    GOTO 25
C---UPDATE-SUB
 25   NSUB=NSUB+1
      IF(SCORE .GE. maxscore) THEN
         maxscore=score
      ENDIF
      IF(SCORE .LE. minscore) THEN
         minscore=score
      ENDIF 
      IF(NSUB .EQ. 1) THEN 
        maxscore = score
        minscore = score
      ENDIF
      
      basescore=score
      scoresum=scoresum+score
      GOTO 2
C--------RESET-ALL--
 51   IF(team .EQ. subname) THEN
      NSUB=NSUB+1
      IF(SCORE .GE. maxscore) THEN
         maxscore=score
      ENDIF
      IF(SCORE .LE. minscore) THEN
         minscore=score
      ENDIF 
      IF(NSUB .EQ. 1) THEN 
        maxscore = score
        minscore = score
      ENDIF
      
      basescore=score
      scoresum=scoresum+score
      ENDIF
      
      decay=1
      IF(NSUB .NE. 1) THEN
      decay=REAL(1/REAL(NSUB))
      decay=decay*100
      decayint=NINT(decay)
      decay=REAL(REAL(decayint)/100)
      ENDIF
      IF(maxscore .EQ. 100) THEN
         decay=1
      ENDIF
      
C      WRITE(*,'(F6.5)') decay
      robust=100-maxscore+minscore
      IF(maxscore .LE. 30) THEN
        robust=0
      ENDIF
C      WRITE(*,'(I3)') robust 
      hi=0.6*basescore*decay+0.3* scoresum/NSUB+0.1*robust 
c      WRITE(*,'(A,I3,I4)') team,numnow,hi
      S(numnow + 1)=hi
      st=S(1)+S(2)+S(3)+S(4)+S(5)+S(6)+S(7)+S(8)+S(9)+S(10)
C      WRITE(*,123)team,q0,S(1),q1,S(2),q2,S(3),q3,S(4),q4,S(5),
C     +    q5,S(6),q6,S(7),q7,S(8),q8,S(9),q9,S(10),qt,st
C      WRITE(*,'(A,I3,I3,I5,I5,I5,I5)') team,numnow, NSUB,basescore,
C     +       scoresum,maxscore,minscore
      WRITE(9,123)team,q0,S(1),q1,S(2),q2,S(3),q3,S(4),q4,S(5),
     +    q5,S(6),q6,S(7),q7,S(8),q8,S(9),q9,S(10),qt,st,r
	    NSUB=0
      numnow=0
      basescore=0
      scoresum=0
      maxscore=0
      minscore=0
      S(1)=0
      S(2)=0
      S(3)=0
      S(4)=0
      S(5)=0
      S(6)=0
      S(7)=0
      S(8)=0
      S(9)=0
      S(10)=0
      st=0
	    GOTO 3
C-----RECORD-END
 3    IF(ios .NE. 0) GOTO 999
      close(8)
      
      open (unit=8,IOSTAT=ios2,ERR=999,FILE=file2,
     +        STATUS ='OLD')
	    GOTO 1
C----ENDOFTHEEND---
 999   close(7)
       close(8)
       close(9)
	     STOP
	     END

	  
            
      
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  