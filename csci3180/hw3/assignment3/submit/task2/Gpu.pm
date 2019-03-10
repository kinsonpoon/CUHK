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

package Gpu;
use Task;
sub new {
	my $class = shift @_;
	my $time=0;
	my $state=0;
	my %task=("name"=>"empty");
	my $id=shift @_;
	my $self = bless {"time"=>\$time,"state"=>\$state,"task"=>\%task,"id"=>\$id}, $class;
	return $self;

}
sub id{
	my $self = shift;
	return ${$self->{"id"}};
}
sub assign_task {
	my $self = shift;
	my $task = shift@_;
	$self->{"state"}=\1;
	$self->{"task"}=$task;
}
sub release {
	my $self = shift;
	$self->{"state"}=\0;
	my $time=0;
	$self->{"time"}=\$time;
	my %task=("name"=>"empty");
	$self->{"task"}=\%task;

}
sub execute_one_time {
	my $self = shift;
	${$self->{"time"}}++;
	##
	my $state=${$self->{"state"}};
	my $cur_time=${$self->{"time"}};
	my $tot_time="";
	if($state==1){
		$tot_time=$self->{"task"}->{"time"};
		$tot_time=$$tot_time;
		if($cur_time == $tot_time){
			print("task in gpu(id: ");
			print(${$self->{"id"}});
			print(") finished\n");
			$self->release();
		}
	}
}
sub print_status{
	my $self = shift;
	my $state=${$self->{"state"}};
	my $item="idle";
	my $user="";
	my $pid="";
	my $cur_time=${$self->{"time"}};
	my $tot_time="";
	if($state==1){
		$item="busy";
		$pid=$self->{"task"}->{"pid"};
		$user=$self->{"task"}->{"name"};
		$tot_time=$self->{"task"}->{"time"};
		$tot_time=$$tot_time;
		$pid=$$pid;
		$user=$$user;
		my $id=$self->{"id"};
		print("  $$id     $item   $user    $pid      $tot_time         $cur_time\n");
	}
	else{
		my $id=$self->{"id"};
		print("  $$id     idle\n");
	}


}

return 1;
