public class Axe extends Weapon {
	private static final int AXE_RANGE = 1;
	private static final int AXE_INIT_DAMAGE = 40;

	public Axe(Player owner) {
		super(AXE_RANGE, AXE_INIT_DAMAGE, owner);

	}

	public void enhance() {
		this.effect += 10;
	}

	@Override
	public void action(int posx, int posy) {
		// TODO Auto-generated method stub
		System.out.println("You are using axe attacking " + posx + " " + posy + ".");

		if (this.owner.pos.distance(posx, posy)  <= this.range) {
			// search for all targets with target coordinates.
			Player player = owner.game.getPlayer(posx, posy);

			if(player != null ) 
			{	if(this.owner.getmaxhp() == player.getmaxhp())
					System.out.println("You are not allowed to attack player of your own race.");
				else
				player.decreaseHealth(this.effect);
			}
		} else {
			System.out.println("Out of reach.");
		}

	}

}
