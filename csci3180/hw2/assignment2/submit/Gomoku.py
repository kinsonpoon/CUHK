# -*- coding: utf-8 -*-
"""
/*
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
 * Assignment 2
 * Name : Poon King Hin
 * Student ID : 1155077526
 * Email Addr : khpoon6@cse.cuhk.edu.hk
 */
"""
import random

class Gomoku:
    def __init__(self):
        gameBoard=[]
        for i in range(9):
            column=[]
            for j in range(9):
                column.append(" ")
            gameBoard.append(column)
        print "Please choose player 1 (O):"
        print "1. Human"
        print "2. Computer Player"
        input1= int(raw_input("Your choice is:"))
        if input1 == 1:
            print "Player O is Human"
        else:
            print "Player O is Computer"
#create player1
#
#
        print "Please choose player 2 (X):"
        print "1. Human"
        print "2. Computer Player"
        input2= int(raw_input("Your choice is:"))
        if input2 == 1:
            print "Player X is Human"
        else:
            print "Player X is Computer"
        self.gameBoard=gameBoard
        self.player1=input1
        self.player2=input2
        self.turn="O"
    def createPlayer(self,symbol,playerNum):
        if playerNum==1:
            result=Human(symbol,self.gameBoard)
            return result
        else:
            result=Computer(symbol,self.gameBoard)
            return result
    def startGame(self):
        self.player1=self.createPlayer("O",self.player1)
        self.player2=self.createPlayer("X",self.player2)
        self.printGameBoard()
        while self.checkWin()==True and self.checkTie()==True:
            self.gameBoard=self.player1.nextMove()
            self.printGameBoard()
            self.gameBoard=self.player2.nextMove()
            self.printGameBoard()
            
    def printGameBoard(self):
        print"",
        for k in range(1,10):
            print "|",k,
        print "|"
        for i in range(9):
            print (str(i+1) + "|"),
            for j in range(9):
                print self.gameBoard[i][j],"|",
            print ""
    def checkWin(self):
        for i in range(9):
            for j in range(9):
                if self.gameBoard[i][j]!=" " and not(i>=4 and j>=4):
                    if(i<=4 and j<=4):
                        if self.gameBoard[i][j]!=" " and self.gameBoard[i][j]==self.gameBoard[i+1][j] and self.gameBoard[i][j]==self.gameBoard[i+2][j] and self.gameBoard[i][j]==self.gameBoard[i+3][j] and self.gameBoard[i][j]==self.gameBoard[i+4][j]:
                            print "Player",self.gameBoard[i][j]," win"
                            return False
                        if self.gameBoard[i][j]!=" " and self.gameBoard[i][j]==self.gameBoard[i][j+1] and self.gameBoard[i][j]==self.gameBoard[i][j+2] and self.gameBoard[i][j]==self.gameBoard[i][j+3] and self.gameBoard[i][j]==self.gameBoard[i][j+4]:
                            print "Player",self.gameBoard[i][j]," win"
                            return False
                        if self.gameBoard[i][j]!=" " and self.gameBoard[i][j]==self.gameBoard[i+1][j+1] and self.gameBoard[i][j]==self.gameBoard[i+2][j+2] and self.gameBoard[i][j]==self.gameBoard[i+3][j+3] and self.gameBoard[i][j]==self.gameBoard[i+4][j+4]:
                            print "Player",self.gameBoard[i][j]," win"
                            return False
                    elif i>=4:
                        if self.gameBoard[i][j]!=" " and self.gameBoard[i][j]==self.gameBoard[i][j+1] and self.gameBoard[i][j]==self.gameBoard[i][j+2] and self.gameBoard[i][j]==self.gameBoard[i][j+3] and self.gameBoard[i][j]==self.gameBoard[i][j+4]:
                            print "Player",self.gameBoard[i][j]," win"
                            return False
                        if self.gameBoard[i][j]!=" " and self.gameBoard[i][j]==self.gameBoard[i-1][j+1] and self.gameBoard[i][j]==self.gameBoard[i-2][j+2] and self.gameBoard[i][j]==self.gameBoard[i-3][j+3] and self.gameBoard[i][j]==self.gameBoard[i-4][j+4]:
                            print "Player",self.gameBoard[i][j]," win"
                            return False
                    else:
                        if self.gameBoard[i][j]!=" " and self.gameBoard[i][j]==self.gameBoard[i+1][j] and self.gameBoard[i][j]==self.gameBoard[i+2][j] and self.gameBoard[i][j]==self.gameBoard[i+3][j] and self.gameBoard[i][j]==self.gameBoard[i+4][j]:
                            print "Player",self.gameBoard[i][j]," win"
                            return False
                        
                        
        return True
    def checkTie(self):
        for i in range(9):
            for j in range(9):
                if self.gameBoard[i][j]==" ":
                    return True
                
        print "Tie"
        return False
        
class Player(object):
    def __init__(self, symbol, gameBoard):
        self.symbol=symbol
        self.gameBoard=gameBoard
    
        
class Human(Player):
    def nextMove(self):
        input=raw_input("Type the row and col to put the disc:")
        while int(input[0]) > 9 or int(input[2]) > 9 or int(input[0])<1 or int(input[2]) < 1:
                print"invalid input"
                input=raw_input("Type the row and col to put the disc:")
        while self.gameBoard[int(input[0])-1][int(input[2])-1]!=" ":
                print"invalid input"
                input=raw_input("Type the row and col to put the disc:")
        self.gameBoard[int(input[0])-1][int(input[2])-1]=self.symbol
        return self.gameBoard
class Computer(Player):
    def nextMove(self):
        input=[random.randint(1,9)]
        input.append(random.randint(1,9))
        while self.gameBoard[int(input[0])-1][int(input[1])-1]!=" ":
            input=[random.randint(1,9)]
            input.append(random.randint(1,9))   
        self.gameBoard[int(input[0])-1][int(input[1])-1]=self.symbol
        return self.gameBoard
    


    

play=Gomoku()
play.startGame()
