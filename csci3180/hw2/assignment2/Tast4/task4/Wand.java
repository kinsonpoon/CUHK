public class Wand {
	protected final int range;
	protected int effect;
	protected Player owner;
	
	public Wand(Player owner) {
		this.range = 5;
		this.effect = 5;
		this.owner = owner;
	}
	
	public void action(int posx, int posy){
		System.out.println("You are using wand healing " + posx + " " + posy +".");

		if (this.owner.pos.distance(posx, posy)  <= this.range) {
			// search for all targets with target coordinates.
			Player player = owner.game.getPlayer(posx, posy);

			if(player != null ) 
			{	if(this.owner.getmaxhp() != player.getmaxhp())
					System.out.println("You are not allowed to heal your opponent race.");
				else
					player.increaseHealth(this.effect);
			}
		} else {
			System.out.println("Out of reach.");
		}



}
	public void enhance(){
		this.effect +=5;
}

	public int getEffect() {
		return this.effect;
	}

	public int getRange() {
		return this.range;
	}
}