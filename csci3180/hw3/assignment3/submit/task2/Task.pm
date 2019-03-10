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

package Task;
sub new {
	my $class = shift @_;
	my $pid = shift @_;
	my $name = shift @_;
	my $time= shift @_;
	my $self = bless {"pid"=>\$pid,"name"=>\$name,,"time"=>\$time}, $class;
	return $self;
}
sub name{
	my $self = shift;
	return ${$self->{"name"}};
}
sub pid{
	my $self = shift;
	return ${$self->{"pid"}};
	
}
sub time{
	my $self = shift;
	return ${$self->{"time"}};
}

return 1;