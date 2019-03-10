use strict;
use warnings;
#/*
# * CSCI3180 Principles of Programming Languages
# *
# * --- Declaration ---
# *
# * I declare that the assignment here submitted is original except for source
# * material explicitly acknowledged. I also acknowledge that I am aware of
# * University policy and regulations on honesty in academic work, and of the
# * disciplinary guidelines and procedures applicable to breaches of such policy
# * and regulations, as contained in the website
# * http://www.cuhk.edu.hk/policy/academichonesty/
# *
# * Assignment 3
# * Name : Poon King Hin
# * Student ID : 1155077526
# * Email Addr : khpoon6@cse.cuhk.edu.hk
# */

package Game;
use MannerDeckStudent; 
use Player;

sub new {
	my $class = shift @_;
	my $deck = MannerDeckStudent->new();
	my @players=();
	my $cards;
	my $self = bless {"deck"=>\$deck,"players"=>\@players,"cards"=>\$cards}, $class;
	return $self;
	
}

sub set_players {
	 my $self = shift;
	 my $players_name=  shift @_;

	 my @playernum=@$players_name;
     my @myArray =();
	#my $class = shift @_;
  	#my @array = @{$_[0]};
  	for my $i(@$players_name){
  	 push(@myArray, Player->new($i));
  	}
  	my $lol=\@myArray;
  	$self->{"players"}=\$lol;
 #
 	return 1;

}

sub getReturn {

}

sub numCards {

}

sub showCards {
	my $self = shift;
	my @printline=();
	@printline=@${$self->{"cards"}};
	print join " ",@${$self->{"cards"}};
	print("\n");

}

sub start_game {
	my $self = shift;
	our @stack=();
	our $turn=0;
	${$self->{"cards"}}=\@stack;
	#print("player1:");
	#print("player1:"); 
	#print("player2:");
	#${$self->{player}}[1]->numCards();
	my @cards= @{${$self->{"deck"}}->{"cards"}};

	our $num_player =scalar @${$self->{"players"}};
	my $counter=$num_player;

	if(52 % $num_player !=0){
		print("Error: cards' number 52 can not be divided by players number $num_player!");
		exit;
	}
	print("There ",$num_player," players in the game:\n");
	
	for (my $i=0; $i < $num_player; $i++){
	my $name=${$${$self->{"players"}}[$i]->{"name"}};
	print($name);
	print" ";
	}
	print"\n\n";
	print"Game begin!!!\n\n";
	#printing name
	${$self->{"deck"}}->shuffle();

	my @deal=${$self->{"deck"}}->AveDealCards($num_player);
	my $xdd;
	my $count=0;
	my $numdeal= scalar @deal;
	for (my $j=0;$j<$numdeal;$j++){
		$${$self->{"players"}}[$j]->{"cards"}=\$deal[$j];
		$count=$count+1;
	}
	#@${$self->{"players"}}[0]->numCards();
	our @dead=();
	while($num_player > 1){
		$turn=$turn+1;
		for (my $i=0; $i < $count; $i++){
			our $flag=0;
			for my $k (@dead){
				if($k ==$i){
					$flag=1;
				}
			}
				if($flag==0){
					
		my $name2=$${$self->{"players"}}[$i]->{"name"};
		my $num_card=$${$self->{"players"}}[$i]->numCards();
		print("Player $$name2 has $num_card cards before deal.\n");
		print("=====Before player's deal=======\n");
		
		$self->showCards();
		print("================================\n");

		our $top=$${$self->{"players"}}[$i]->dealCards();
		print("$$name2 ==> card ");
		print("$top\n");
		push (@stack,$top);
		my $stacknum=@stack;

			
		for (my $j=0;$j<$stacknum-1;$j++){
					if('J' eq  $top){
				$${$self->{"players"}}[$i]->getCards(\@stack);
				@stack=();
				last;
			}
			elsif ($stack[$j] eq $top){
				my @get=@stack[$j..$stacknum-1];
				$${$self->{"players"}}[$i]->getCards(\@get);
				my $pos=$j-1;
				@stack=@stack[0..$pos];
				last;
			}

		}
	
		print("=====After player's deal=======\n");
		$self->showCards();
		print("================================\n");
		$num_card=$${$self->{"players"}}[$i]->numCards();
		print("Player $$name2 has $num_card cards after deal.\n");
			if($num_card==0){
				$num_player=$num_player-1;
				print("Player $$name2 has no cards, out!\n");
				push (@dead,$i);
				
			}
			else{
				print"\n";
			}
			
		}

	}
}
	for(my $x=0;$x<$counter;$x++){
		my $winner=0;
		for my $k (@dead){
				if($k ==$x){
					$winner=1;
				}
			}
			if($winner!=1){
				my $name3=$${$self->{"players"}}[$x]->{"name"};;
				print("Winner is $$name3 in game $turn\n");
				last;
		}
	
	
		}

	}
return 1;