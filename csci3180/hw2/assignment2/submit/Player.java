import java.util.Random;

public abstract class Player {
	private int MOBILITY;
	protected Pos pos;
	protected int health;
	protected int maxhealth;
	protected Weapon equipment;
	protected Wand object;
	protected int index;
	protected String myString;
	protected SurvivalGame game;
	
	public Player(int healthCap, int mob, int posx, int posy, int index, SurvivalGame game) {

		this.MOBILITY = mob;
		this.health = healthCap;
		this.maxhealth = healthCap;
		this.pos = new Pos(posx, posy);
		this.index = index;
		this.game = game;
	}

	public Pos getPos() {
		return pos;
	}
	public int getmaxhp(){
		return this.maxhealth;
	}
	public void teleport() {

		Random rand;
		rand = new Random();
		int randx = rand.nextInt(game.D);
		int randy = rand.nextInt(game.D);
		while (game.positionOccupied(randx, randy)) {
			randx = rand.nextInt(game.D);
			randy = rand.nextInt(game.D);
		}
		pos.setPos(randx, randy);
	}

	public void increaseHealth(int h) {
		if (this.health<=0){
			this.health += h;
			if(this.health>0)
				this.myString =this.myString.charAt(1)+Integer.toString(index);
			
		}
		else{	
		this.health += h;
		if (this.health>= this.maxhealth)
			this.health=this.maxhealth;
		}
	}

	public void decreaseHealth(int h) {
		this.health -= h;
		if (this.health <= 0)
			this.myString = "C" + this.myString.charAt(0);
	}

	public String getName() {
		return myString;
	}

	public void askForMove() {
		// Print general information
		System.out.println("Your health is " + health
				+ String.format(". Your position is (%d,%d). Your mobility is %d.", pos.getX(), pos.getY(), this.MOBILITY));

		System.out.println("You now have following options: ");
		System.out.println("1. Move");
		if(index == game.getN()/2 - 1 || index==game.getN()-1)
			System.out.println("2. Heal");
		else
			System.out.println("2. Attack");
		System.out.println("3. End tne turn");

		int a = SurvivalGame.reader.nextInt();
		
		if (a == 1) {
			System.out.println("Specify your target position (Input 'x y').");
			int posx = SurvivalGame.reader.nextInt(), posy = SurvivalGame.reader.nextInt();
			if (pos.distance(posx, posy) > this.MOBILITY) {
				System.out.println("Beyond your reach. Staying still.");
			} else if (game.positionOccupied(posx, posy)) {
				System.out.println("Position occupied. Cannot move there.");
			} else {
				this.pos.setPos(posx, posy);
				game.printBoard();
				if(index == game.getN()/2 - 1 || index==game.getN()-1)
					System.out.println("You can now \n1.heal\n2.End the turn");
				else
					System.out.println("You can now \n1.attack\n2.End the turn");
				if (SurvivalGame.reader.nextInt() == 1) {
					if(index == game.getN()/2 - 1 || index==game.getN()-1)
						System.out.println("Input position to heal. (Input 'x y')");
					else
						System.out.println("Input position to attack. (Input 'x y')");
					int attx = SurvivalGame.reader.nextInt(), atty = SurvivalGame.reader.nextInt();
					if(index == game.getN()/2 - 1 || index==game.getN()-1)
						this.object.action(attx,atty);
					else
						this.equipment.action(attx, atty);
				}
			}
		} else if (a == 2) {
			if(index == game.getN()/2 - 1 || index==game.getN()-1){
				System.out.println("Input position to heal.");
				int attx = SurvivalGame.reader.nextInt(), atty = SurvivalGame.reader.nextInt();
				this.object.action(attx, atty);
			}
			else{
				System.out.println("Input position to attack.");
				int attx = SurvivalGame.reader.nextInt(), atty = SurvivalGame.reader.nextInt();
				this.equipment.action(attx, atty);
			}
		} else if (a == 3) {
			return;
		}
	}

}
