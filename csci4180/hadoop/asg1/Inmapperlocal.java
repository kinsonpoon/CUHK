import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class Inmapperlocal {
	public static class TokenizerMapper extends 
			Mapper<LongWritable, Text,IntWritable, IntWritable> {
		private final static IntWritable one = new IntWritable(1);
		private IntWritable wordLength = new IntWritable();

		public void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
			Map<String, Integer> map = new HashMap<String, Integer>();
			String line = value.toString();
			StringTokenizer tokenizer = new StringTokenizer(line);
			while (tokenizer.hasMoreTokens()) {
				//wordLength.set(tokenizer.nextToken().length());
				String token = tokenizer.nextToken();
				if(!map.containsKey(token)) {
    				map.put(token, 1);
   				} //else {
   				// map.put(token, 1);
   				//}
		    	//System.out.println("Debug: " + key + " " + wordLength);
				//context.write(wordLength, one);
			}

			Iterator<Map.Entry<String, Integer>> it = map.entrySet().iterator();
  			while(it.hasNext()) {
   				Map.Entry<String, Integer> entry = it.next();
   				String sKey = entry.getKey();
   				wordLength.set(sKey.length());
  				int total = entry.getValue().intValue();
   				context.write(wordLength, new IntWritable(total));
  			}

		}
	}

	public static class Reduce extends 
			Reducer<IntWritable, IntWritable,IntWritable, IntWritable> {
		public void reduce(IntWritable key, Iterable<IntWritable> values,
				Context context) throws IOException, InterruptedException {
			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

	public static void main(String[] args) throws Exception {
	
		// Run on a local node
		Configuration conf = new Configuration();
		conf.set("fs.defaultFS", "file:///");
		conf.set("mapreduce.framework.name", "local");

		Job job = Job.getInstance(conf, "wordcount");

		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(IntWritable.class);

		job.setJarByClass(Inmapperlocal.class);

		job.setMapperClass(TokenizerMapper.class);
		//job.setCombinerClass(Reduce.class);
		job.setReducerClass(Reduce.class);

		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		job.waitForCompletion(true);
	}
}