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
 
package Player;
sub new {
	my $class = shift @_;
	my $name = shift @_;
	my @cards=();
	my $self = bless {"name"=>\$name,"cards"=>\@cards}, $class;
	#print "${$self->{name}}\n";
	return $self;


}

sub getCards {
	my $self = shift;
	my $input=shift @_;
	my @new_card = @$input;
	#print(@new_card);
	my @stack=@${$self->{"cards"}};
	my $num =scalar @new_card;
	for (my $j=$num-1;$j>=0;$j--){
	push(@${$self->{"cards"}},$new_card[$j]);
	}
	#print "@stack\n";

}

sub dealCards {
	my $self = shift;
	my @stack=@${$self->{"cards"}};


	my $top= shift(@${$self->{"cards"}});
	#print "$top\n";
	#print @$${$self->{"cards"}};
	#print "putting top into deck stack\n";
	#print"@stack\n";
	return $top;
	

}

sub numCards {
	my $self = shift;

	my @card= @${$self->{"cards"}};
	my $num_card= scalar @card;
	return $num_card;
	
}

return 1;