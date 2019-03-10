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
             self.teleportObjects[i]=Human(0,0,i,self)
             self.teleportObjects[i+len(self.teleportObjects)/2]=Chark(0,0,i,self)
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
        self.health=healthCap
        self.mob=mob
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
            self.equipment.enhance()
            self.pos.setPos(randx,randy)
    def getName(self):
        return self.myString
    def askForMove(self):
        print"Your health is ",self.health,".Your position is (",self.pos.posx,",",self.pos.posy,").Your mobility is",self.mob
        print "You now have following options: "
        print "1. Move"
        print"2. Attack"
        print"3. End tne turn"
        a=int(raw_input())
        if a == 1:
            position=raw_input("Specify your target position (Input 'x y').")
            try:
                posx=int(position[0])
                posy=int(position[2])
                if self.pos.distance(posx, posy) > self.mob:
                    print "Beyond your reach. Staying still."
                elif self.game.positionOccupied(posx, posy)==True:
                    print "Position occupied. Cannot move there."
                else:
                    self.pos.setPos(posx, posy)
                    self.game.printBoard()
                    b=int(raw_input("You can now \n1.attack\n2.End the turn"))
                    if b==1:
                        attackpos=raw_input("Input position to attack. (Input 'x y')")
                        attx=int(attackpos[0])
                        atty=int(attackpos[2])
                        #weapon shit
                        self.equipment.action(attx, atty)
            except:
                print "Beyond your reach. Staying still."
        if a==2:
            attackpos=raw_input("Input position to attack. (Input 'x y')")
            try:
                attx=int(attackpos[0])
                atty=int(attackpos[2])
                self.equipment.action(attx, atty)
            except:
                print "Beyond your reach. Staying still."
            #weapon shit
    def increaseHealth(self,h):
        self.health=self.health+h
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
    def __init__(self,posx,posy,index,game):
        super(Human,self).__init__(80, 2, posx, posy, index, game)
        self.myString = 'H' + str(index)
        self.equipment = Rifle(self)
    def askForMove(self):
        print "You are a human", self.myString, "using Rifle. (Range:",self.equipment.getRange(),", Ammo #:",self.equipment.getAmmo(),", Damage per shot:",self.equipment.getEffect(),")"
        super(Human,self).askForMove()
class Chark(Player):
    def __init__(self,posx,posy,index,game):
        super(Chark,self).__init__(100, 4, posx, posy, index, game)
        self.myString = 'C' + str(index)
        self.equipment = Axe(self)
    def askForMove(self):
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
        ammoToUse=int(raw_input("Type how many ammos you want to use."))
        if ammoToUse > self.ammo:
            print "You don't have that ammos."
        elif self.owner.pos.distance(posx, posy)<=self.range:
            player = self.owner.game.getPlayer(posx, posy)
            if player != 1:
                player.decreaseHealth(self.effect*int(ammoToUse))
                self.ammo=self.ammo-ammoToUse
            else:
                print "Out of reach." 
    def getAmmo(self):
        return self.ammo
               
"""

public class SurvivalGame {
	private int n; // Number of player
	public final int D = 10; // dimension of board
	private final int O = 2; // Number of obstacles

	
	private Object[] teleportObjects;

	public static Scanner reader = new Scanner(System.in);

	public void printBoard() {
		String printObject[][] = new String[D][D];

		// init printObject
		for (int i = 0; i < D; i++)
			for (int j = 0; j < D; j++)
				printObject[i][j] = "  ";

		for (int i = 0; i < n; i++) {
			Pos pos = ((Player)teleportObjects[i]).getPos();
			printObject[pos.getX()][pos.getY()] = ((Player) teleportObjects[i]).getName();
		}

		for (int i = n; i < n+O; i++) {
			Pos pos = ((Obstacle)teleportObjects[i]).getPos();
			printObject[pos.getX()][pos.getY()] = "O" + Integer.toString(i-n);
		}

		// printing
		System.out.print(" ");
		for (int i = 0; i < D; i++)
			System.out.print(String.format("| %d  ", i));

		System.out.println("|");

		for (int i = 0; i < D * 5.5; i++)
			System.out.print("-");
		System.out.println("");

		for (int row = 0; row < D; row++) {
			System.out.print(row);
			for (int col = 0; col < D; col++)
				System.out.print(String.format("| %s ",
				printObject[row][col]));
			System.out.println("|");
			for (int i = 0; i < D * 5.5; i++)
				System.out.print("-");
			System.out.println("");
		}

	}

	public boolean positionOccupied(int randx, int randy) {

		for (Object o : teleportObjects) {
			if (o instanceof Player) {
				Pos pos = ((Player) o).getPos();
				if (pos.getX() == randx && pos.getY() == randy)
					return true;
			} else {
				Pos pos = ((Obstacle) o).getPos();
				if (pos.getX() == randx && pos.getY() == randy)
					return true;
			}

		}

		return false;
	}

	public Player getPlayer(int randx, int randy) {
		// TODO Auto-generated method stub
		for (Object o : teleportObjects) {
			if (o instanceof Player) {
				Pos pos = ((Player) o).getPos();
				if (pos.getX() == randx && pos.getY() == randy)
					return (Player) o;
			}
		}

		return null;
	}

	private  void init() {

		System.out.println("Welcome to Kafustrok. Light blesses you. \nInput number of players: (a even number)");
		n = reader.nextInt();

		teleportObjects = new Object[n + O];

		// create N/2 Humans

		for (int i = 0; i < n / 2; i++) {
			teleportObjects[i] = new Human(0, 0, i, this);
			teleportObjects[i + n / 2] = new Chark(0, 0, i, this);
		}

		// create O obstacles. You cannot stand there
		for (int i = 0; i < O; i++) {

			teleportObjects[i + n] = new Obstacle(0, 0, i, this);
		}

		// positions would be reinitialized later. 0,0 is dummy

	}

	private  void gameStart() {
		int turn = 0;
		int numOfAlivePlayers = n;
		while (numOfAlivePlayers > 1) {
			// teleport after every N turns
			if (turn == 0) {
				for (Object obj : teleportObjects) {
					if (obj instanceof Human)
						((Human) obj).teleport();
					else if (obj instanceof Chark)
						((Chark) obj).teleport();
					else if (obj instanceof Obstacle)
						((Obstacle) obj).teleport();
				}
				System.out.println("Everything gets teleported..");
			}
			printBoard();
			Player t = (Player) teleportObjects[turn];
			// t can move only if he is alive!
			if (t.health > 0) {
				// dynamic binding helps
				t.askForMove();
				System.out.println("\n");
				
			}
			turn = (turn + 1) % n;
			// count number of alive players
			numOfAlivePlayers = 0;

			for (int i = 0; i < n; i++) {
				if (((Player) teleportObjects[i]).health > 0)
					numOfAlivePlayers += 1;
			}
	
		}

		System.out.println("Game over.");
		printBoard();

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// System.out.println(String.format("(%d,%d)", 3,4));
		SurvivalGame game = new SurvivalGame();
		game.init();
		game.gameStart();
	}
}

"""
h=SurvivalGame()
h.gameStart()
