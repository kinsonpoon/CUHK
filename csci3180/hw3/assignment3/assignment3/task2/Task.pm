use strict;
use warnings;

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