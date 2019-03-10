public class Human extends Player {
	
	public Human(int posx, int posy, int index, SurvivalGame game) {
		super(80, 2, posx, posy, index, game);
		
		this.myString = 'H' + Integer.toString(index);
		System.out.println(String.format("index %d, game %d",index,game.getN()));
		if(index == game.getN()/2 - 1)
			this.object = new Wand(this);
		else
			this.equipment = new Rifle(this);
		
	}

	public void teleport() {
		super.teleport();
		if(index == game.getN()/2 - 1)
			((Wand)this.object).enhance();
		else
			((Rifle)this.equipment).enhance();
		
	}
	
	public void distance(int posx, int posy)
	{
		
	}
	
	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		if(index == game.getN()/2 - 1){
			System.out.println(String.format("You are a human (H%d) using Wand. (Range %d, Healing effect: %d)", this.index, 
				this.object.getRange(),
				this.object.getEffect() ));

		super.askForMove();


}
		else{
		System.out.println(String.format("You are a human (H%d) using Rifle. (Range %d, Ammo #: %d, Damage per shot: %d)", this.index, 
				this.equipment.getRange(),((Rifle)this.equipment).getAmmo(),
				this.equipment.getEffect() ));

		super.askForMove();
		}
	}

}
