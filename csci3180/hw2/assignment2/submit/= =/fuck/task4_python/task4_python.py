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

class SurvivalGame:
     def __init__(self):
         print "Welcome to Kafustrok. Light blesses you."
         while True:
             try:
                 self.n= int(raw_input("Input number of players: (a even number)"))
                 break
             except:
                 pass
         self.teleportObjects=[]
         for i in range(self.n):
             if i < (self.n)/2:
                 self.teleportObjects.append(str(i))
             else:
                 self.teleportObjects.append(str(i-(self.n)/2))

         self.D=10
     def getPlayer(self,randx,randy):
         for i in range(self.n):
             pos=self.teleportObjects[i].getPos()
             if int(pos.getX()) == int(randx) and int(pos.getY()) == int(randy):
                 return self.teleportObjects[i]
         return 1
         
             
     
     
     
     def positionOccupied(self,randx,randy):
         for item in self.teleportObjects:
             pos=item.getPos()
             if pos.getX() == randx and pos.getY() == randy:
                 return True
         return False
     def printBoard(self):
         printObject=[]
         for i in range(10):
            column=[]
            for j in range(10):
                column.append("  ")
            printObject.append(column)
         for num in range(len(self.teleportObjects)):
             try:
                 printObject[self.teleportObjects[num].getPos().getX()][self.teleportObjects[num].getPos().getY()]=self.teleportObjects[num].getName()
                 number=num
             except:
                 printObject[self.teleportObjects[num].getPos().getX()][self.teleportObjects[num].getPos().getY()]="O"+str(num-number-1)
         for i in range(10): 
             print " |",i,
         print " |"
         printline=""
         for i in range(55):
             printline=printline+"-"
         print printline
         for i in range(10):
             print (str(i) + "|"),
             for j in range(10):
                 print printObject[i][j],"|",
             print""
             print printline
     def gameStart(self):
         for i in range(len(self.teleportObjects)/2):
             if i==len(self.teleportObjects)/2 -1:
                 self.teleportObjects[i]=Human(0,0,i,self,1)
                 self.teleportObjects[i+len(self.teleportObjects)/2]=Chark(0,0,i,self,1)
             else:
                 self.teleportObjects[i]=Human(0,0,i,self,0)
                 self.teleportObjects[i+len(self.teleportObjects)/2]=Chark(0,0,i,self,0)
         self.teleportObjects.append(Obstacle(0,0,0,self))
         self.teleportObjects.append(Obstacle(0,0,1,self))

         turn=0
         numOfAlivePlayers=self.n
         while numOfAlivePlayers>1:
             if (turn == 0):
                 for item in self.teleportObjects:
                     item.teleport()
                 print "Everything gets teleported.."
             self.printBoard()
             
             t = self.teleportObjects[turn]
             if t.health>0:
                 t.askForMove()
                 print ""
             turn = (turn + 1) % self.n
             numOfAlivePlayers = 0
             for i in range(self.n):
                 if self.teleportObjects[i].health>=0:
                     numOfAlivePlayers=numOfAlivePlayers+1
             
         print "Game over."
         self.printBoard()
        
            
             
class Player(object):
    def __init__(self,healthCap,mob,posx,posy,index,game):
        self.maxhealth=healthCap
        self.health=healthCap
        self.mob=mob
        self.pos=Pos(posx,posy)
        self.index=index
        self.game=game
    def getHealth(self):
        return self.maxhealth
    def getPos(self):
            return self.pos
    def teleport(self):
            randx=random.randint(1,9)
            randy=random.randint(1,9)
            while self.game.positionOccupied(randx,randy)==True:
                randx=random.randint(1,9)
                randy=random.randint(1,9)
            self.equipment.enhance()
            self.pos.setPos(randx,randy)
    def getName(self):
        return self.myString
    def askForMove(self):
        print"Your health is ",self.health,".Your position is (",self.pos.posx,",",self.pos.posy,").Your mobility is",self.mob
        print "You now have following options: "
        print "1. Move"
        if self.equipment.getRange()==5:
            print "2. Heal"
        else:
            print"2. Attack"
        print"3. End tne turn"
        while True:
            try:
                a=int(raw_input())
                break
            except:
                pass
        if a == 1:
            while True:
                try:
                    position=raw_input("Specify your target position (Input 'x y').")
                    break
                except:
                    pass
            try:
                posx=int(position[0])
                posy=int(position[2])
                if self.pos.distance(posx, posy) > self.mob:
                    print "Beyond your reach. Staying still."
                elif self.game.positionOccupied(posx, posy)==True:
                    print "Position occupied. Cannot move there."
                else:
                    
                    self.pos.setPos(posx, posy)
                    print "Beyond your reach. Staying still."
                    self.game.printBoard()

                    if self.equipment.getRange()==5:
                        b=int(raw_input("You can now \n1.heal\n2.End the turn"))
                        if b==1:

                            if self.equipment.getRange()==5:
                                attackpos=raw_input("Input position to heal. (Input 'x y')")
                            else:
                                attackpos=raw_input("Input position to attack. (Input 'x y')")

                            attx=int(attackpos[0])
                            atty=int(attackpos[2])
                    #weapon shit
                            self.equipment.action(attx, atty)
            except:
                print "Beyond your reach. Staying still."
        if a==2:
            while True:
                try:
                    if self.equipment.getRange()==5:
                        attackpos=raw_input("Input position to heal. (Input 'x y')")
                    else:
                        attackpos=raw_input("Input position to attack. (Input 'x y')")
                    break
                except:
                    pass
            try:
                attx=int(attackpos[0])
                atty=int(attackpos[2])
                self.equipment.action(attx, atty)
            except:
                print "Beyond your reach. Staying still."
            #weapon shit
    def increaseHealth(self,h):
        self.health=min(self.health+h,self.maxhealth)
        if self.myString[1]!=str(self.index):
            if self.health>0:
                self.myString=self.myString[1]+str(self.index)
    def decreaseHealth(self,h):
        self.health=self.health-h
        if self.health<=0:
            self.myString="C"+self.myString[0]
            

class Obstacle(object):
    def __init__(self,posx,posy,index,game):
        self.pos=Pos(posx,posy)
        self.index=index
        self.game=game
    def getPos(self):
            return self.pos
    def teleport(self):
            randx=random.randint(1,9)
            randy=random.randint(1,9)
            while self.game.positionOccupied(randx,randy)==True:
                randx=random.randint(1,9)
                randy=random.randint(1,9)
            self.pos.setPos(randx,randy)
class Human(Player):
    def __init__(self,posx,posy,index,game,last):
        super(Human,self).__init__(80, 2, posx, posy, index, game)
        self.myString = 'H' + str(index)
        if last==1:
            self.equipment=Wand(self)
        else:
            self.equipment = Rifle(self)
    def askForMove(self):
        if self.equipment.getRange()==5:
            print "You are a human", self.myString, "using Wand. (Range:",self.equipment.getRange(),", Effect:",self.equipment.getEffect(),")"
        else:
            print "You are a human", self.myString, "using Rifle. (Range:",self.equipment.getRange(),", Ammo #:",self.equipment.getAmmo(),", Damage per shot:",self.equipment.getEffect(),")"
        super(Human,self).askForMove()
class Chark(Player):
    def __init__(self,posx,posy,index,game,last):
        super(Chark,self).__init__(100, 4, posx, posy, index, game)
        self.myString = 'C' + str(index)
        if last==1:
            self.equipment=Wand(self)
        else:
            self.equipment = Axe(self)
    def askForMove(self):
        if self.equipment.getRange()==5:
            print "You are a Chark", self.myString, "using Wand. (Range:",self.equipment.getRange(),", Effect:",self.equipment.getEffect(),")"
        else:
            print "You are a Chark", self.myString, "using Axe. (Range:",self.equipment.getRange(),", Damage:",self.equipment.getEffect(),")"
        super(Chark,self).askForMove()

        
class Pos(object):
    def __init__(self,posx,posy):
        self.posx=posx
        self.posy=posy
    def setPos(self,x,y):
        self.posx=x
        self.posy=y
    def getX(self):
        return self.posx
    def getY(self):
        return self.posy
    def distance(self,parameter_A, parameter_B=None):
        if isinstance(parameter_B, int):

            return (int(self.posx) - int(parameter_A))+(int(self.posy) - int(parameter_B))
        else:


            return (int(self.posx) - int(parameter_A))+(int(self.posy) - int(parameter_A))

class Wand(object):
    def __init__(self,owner):
        self.range=5
        self.effect=5
        self.owner=owner
    def getEffect(self):
        return self.effect
   
    def getRange(self):
        return self.range
    def enhance(self):
        self.effect=self.effect+5
    def action(self,posx,posy):
        print "You are using wand healing ",posx,posy,"."
        if self.owner.pos.distance(posx, posy)<=self.range:
            player = self.owner.game.getPlayer(posx, posy)
            if player != 1:
                if player.getHealth()!=self.owner.getHealth():
                    print "You are not allowed to heal your opponent race."
                else:
                    player.increaseHealth(self.effect)
            else:
                print "Out of reach."
        
class Weapon(object):
    def __init__(self,ranges,damage,owner):
        self.range=ranges
        self.effect=damage
        self.owner=owner
        
    def getEffect(self):
        return self.effect
   
    def getRange(self):
        return self.range

class Axe(Weapon):
    def __init__(self,owner):
        super(Axe,self).__init__(1,40,owner)
    def enhance(self):
        self.effect=self.effect+10
    def action(self,posx,posy):
        print "You are using axe attacking ",posx,posy,"."
        if self.owner.pos.distance(posx, posy)<=self.range:
            player = self.owner.game.getPlayer(posx, posy)
            if player != 1:
                if player.getHealth()==self.owner.getHealth():
                    print "You are not allowed to attack player of your own race."
                else:
                    player.decreaseHealth(self.effect)
            else:
                print "Out of reach."
class Rifle(Weapon):
    def __init__(self,owner):
        super(Rifle,self).__init__(4,10,owner)
        self.AMMO_LIMIT=6
        self.ammo=self.AMMO_LIMIT
        self.AMMO_RECHARGE = 3
    def enhance(self):
        self.ammo = min(self.AMMO_LIMIT, self.ammo + self.AMMO_RECHARGE)
    def action(self,posx,posy):
        print "You are using rifle attacking ",posx,posy,"."
        while True:
            try:
                ammoToUse=int(raw_input("Type how many ammos you want to use."))
                break
            except:
                pass
        if ammoToUse > self.ammo:
            print "You don't have that ammos."
        elif self.owner.pos.distance(posx, posy)<=self.range:
            player = self.owner.game.getPlayer(posx, posy)
            if player != 1:
                if player.getHealth()==self.owner.getHealth():
                    print "You are not allowed to attack player of your own race."
                else:
                    player.decreaseHealth(self.effect*int(ammoToUse))
                    self.ammo=self.ammo-ammoToUse
            else:
                print "Out of reach." 
    def getAmmo(self):
        return self.ammo
               
#Main
h=SurvivalGame()
h.gameStart()