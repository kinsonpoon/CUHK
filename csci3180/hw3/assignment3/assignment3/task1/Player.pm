#use strict;
#use warnings;
 
package Player;
sub new {
	my $class = shift @_;
	my $name = shift @_;
	my @cards=();
	my $dead=0;
	my $self = bless {"name"=>\$name,"cards"=>\@cards,"dead"=>\$dead}, $class;
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