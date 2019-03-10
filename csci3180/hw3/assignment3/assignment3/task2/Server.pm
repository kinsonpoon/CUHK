use strict;
use warnings;
 
package Server;
use Gpu;
use Task;
our $pid=-1;
sub new {
	my $class = shift @_;
	my $gpus;
	my @waitq=();
	my $num_gpu=shift @_;
	my @array=();
	for (my $i=0;$i<$num_gpu;$i++){
		my $gpu = Gpu->new($i);
		push @array,$gpu;
	}
	$gpus=\@array;
	my $self = bless {"gpus"=>\$gpus,"waitq"=>\@waitq}, $class;
	return $self;
}
sub task_info {
	my $self = shift;
	my $task = shift @_;
	return "task(user: ".$task->name().", pid: ".$task->pid().", time: ".$task->time().")";
}
sub task_attr {
	my $self = shift;
	my $task = shift @_;
	return $task->name(), $task->pid(), $task->time();
}
sub gpu_info {
	my $self = shift;
	my $gpu = shift @_;
	return "gpu(id: ".$gpu->id().")";
}
sub submit_task {
	my $self = shift;
	my $task_name=shift @_;
	my $task_time=shift @_;
	my $print;
	my $pidxdd=$pid;
	$pid=$pid+1;
	my $task=Task->new($pid,$task_name,$task_time);
	my $num_gpu=@${$self->{"gpus"}};
	my $count=0;
	for (my $i=0;$i<$num_gpu;$i++){
		my $gpu2=$self->{"gpus"};
		my @gpu=$$gpu2;
		my $idle= $gpu[0][$i]->{"state"};
		my $state=0;
		if($$idle == 0){
			$gpu[0][$i]->assign_task($task);
			my $funny=$self->gpu_info($gpu[0][$i]);
			print($self->task_info($task));
			$print=" => $funny";
			last;
		}
			else{
				$count++;
			}
	
		}
		if($count==$num_gpu){
			push @{$self->{"waitq"}},$task;
			print($self->task_info($task));
			$print=" => waiting queue";
			}
		print("$print\n");

	}


sub deal_waitq {
	my $self = shift;
	our $idle=0;
	my $num_gpu=@${$self->{"gpus"}};
	for (my $i=0;$i<$num_gpu;$i++){
		my $gpu2=$self->{"gpus"};
		my @gpu=$$gpu2;
		my $state=$gpu[0][$i]->{"state"};
		if($$state==0){
			$idle=\$gpu[0][$i];
			my $num_waitq=@{$self->{"waitq"}};
			if($num_waitq !=0){
			my $task= shift @{$self->{"waitq"}};
			$$idle->assign_task($task);
			my $funny=$self->gpu_info($gpu[0][$i]);
			print($self->task_info($task));
			print(" => $funny\n");
				}


			}
		}

}
sub kill_task {
	my $self = shift;
	my $task_name=shift @_;
	my $task_pid=shift @_;
	my $kill=0;
	#
	my $num_gpu=@${$self->{"gpus"}};
	for (my $i=0;$i<$num_gpu;$i++){
		my $gpu2=$self->{"gpus"};
		my @gpu=$$gpu2;
		my $state=$gpu[0][$i]->{"state"};
		if($$state==1){
			my $pid=$gpu[0][$i]->{"task"}->{"pid"};
			my $name=$gpu[0][$i]->{"task"}->{"name"};
			if($$pid eq $task_pid and $$name eq $task_name){
				print("user $task_name kill ");
				print($self->task_info($gpu[0][$i]->{"task"}));
				print("\n");
				$gpu[0][$i]->release();
				$kill=1;
				}
			}
		}
	my $num_waitq=@{$self->{"waitq"}};
	for (my $i=0;$i<$num_waitq;$i++){
		my @wait2=@{$self->{"waitq"}};
			my($name,$id,$time)=$self->task_attr($wait2[$i]);
				if($id eq $task_pid and $name eq $task_name){
				print("user $task_name kill ");
				print($self->task_info($wait2[$i]));
				print("\n");
				if($i==0){
					shift @{$self->{"waitq"}};
					
				}
				elsif($i==$num_waitq-1){
					pop @{$self->{"waitq"}};
					
				}
				else{
					for(my $k=$i;$k<$num_waitq-2;$k++){
						$@{$self->{"waitq"}}[$k]=$@{$self->{"waitq"}}[$k+1];
					}
					@{$self->{"waitq"}}[$num_waitq-2]=@{$self->{"waitq"}}[$num_waitq-1];
					pop @{$self->{"waitq"}};
				}
				$kill=1;
				last;
				}
			}
		if($kill==0){
			print("user $task_name kill task(pid: $task_pid) fail\n");
			}
	$self->deal_waitq();
}
sub execute_one_time {
	my $self = shift;
	print("execute_one_time..\n");
	my $num_gpu=@${$self->{"gpus"}};
	my $count=0;
	for (my $i=0;$i<$num_gpu;$i++){
		my $gpu2=$self->{"gpus"};
		my @gpu=$$gpu2;
		my $idle= $gpu[0][$i]->{"state"};
		if($$idle==1){
		$gpu[0][$i]->execute_one_time;
		}
	}
	$self->deal_waitq();
}
sub show {
	my $self = shift;
	print("==============Server Message================\n");
	print("gpu-id  state  user  pid  tot_time  cur_time\n");
	my $num_gpu=@${$self->{"gpus"}};
	for (my $i=0;$i<$num_gpu;$i++){
		my $gpu2=$self->{"gpus"};
		my @gpu=$$gpu2;
		$gpu[0][$i]->print_status;
	}
	my $num_waitq=@{$self->{"waitq"}};
	for (my $i=0;$i<$num_waitq;$i++){
		my @wait2=@{$self->{"waitq"}};
			my($name,$id,$time)=$self->task_attr($wait2[$i]);
			print("        wait   $name    $id      $time\n");
	}
	print("============================================\n\n");
}


return 1;