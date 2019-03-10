public class Chark extends Player {

	public Chark(int posx, int posy, int index, SurvivalGame game) {
		super(100, 4, posx, posy, index, game);

		this.myString = "C" + Integer.toString(index);
		if(index == game.getN()/2 - 1)
			this.object = new Wand(this);
		else
			this.equipment = new Axe(this);

	}

	public void teleport() {
		
		super.teleport();
		if(index == game.getN()/2- 1)
			this.object = new Wand(this);
		else
			((Axe) this.equipment).enhance();
	}

	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		if(index == game.getN()/2 - 1){
			System.out.println(String.format("You are a Chark (C%d) using Wand. (Range: %d, Healing Effect: %d)",this.index,
			this.object.getRange(), this.object.getEffect()));
			super.askForMove();
		}
		else{
			System.out.println(String.format("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)",this.index,
			this.equipment.getRange(), this.equipment.getEffect()));
			super.askForMove();
			
			
		}
		
	}
}
