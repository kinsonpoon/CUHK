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

public class WordLengthCount {
	public static class TokenizerMapper extends 
			Mapper<LongWritable, Text,IntWritable, IntWritable> {
		private final static IntWritable one = new IntWritable(1);
		private IntWritable wordLength = new IntWritable();
		private Map<IntWritable, Integer> map;


		public void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
			String line = value.toString();
			
			
			
			Map<IntWritable, Integer> map = getMap();
			//String line = value.toString();
			StringTokenizer tokenizer = new StringTokenizer(line," ",false);
			while (tokenizer.hasMoreTokens()) {
				String token = tokenizer.nextToken();
				
				IntWritable wordLength = new IntWritable(0);
				wordLength.set(token.length());
				//System.out.println("Debug: "+token+" " + wordLength);
				//String token = tokenizer.nextToken();
				//System.out.println("Debug: " + wordLength);
				if(map.containsKey(wordLength)) {
    				int total=map.get(wordLength) + 1;
    				map.put(wordLength,total);
    				//System.out.println("Debug: " + wordLength + " " +total );
   				} else {
   				 map.put(wordLength, 1);
   				}
   			
		    	//System.out.println("Debug: " + wordLength + " " + );
				//context.write(wordLength, one);
			}
		
		
	}
			protected void cleanup(Context context)
 			 throws IOException, InterruptedException {
  				Map<IntWritable, Integer> map = getMap();
  				System.out.println(Arrays.asList(map));
  				//Iterator<Map.Entry<IntWritable, Integer>> it = map.entrySet().iterator();
  				//while(it.hasNext()) {
   					//Map.Entry<IntWritable, Integer> entry = it.next();
   					//IntWritable sKey = entry.getKey();
   					
   					// total = entry.getValue();
  				long i = 0;
				for (Map.Entry<IntWritable, Integer> pair : map.entrySet()) {
    				System.out.println("Debug: " +pair.getKey()+" "+ pair.getValue());
   					context.write(pair.getKey(), new IntWritable(pair.getValue()));
					}
   					//System.out.println("Debug: " +entry.getKey()+" "+ entry.getValue());
   					//context.write(entry.getKey(), new IntWritable(entry.getValue()));
  				//}
			 }



			//Iterator<Map.Entry<String, Integer>> it = map.entrySet().iterator();
  			//while(it.hasNext()) {
   			//	Map.Entry<String, Integer> entry = it.next();
   			//	String sKey = entry.getKey();
   			//	wordLength.set(sKey.length());
  			//	int total = entry.getValue().intValue();
   			//	context.write(wordLength, new IntWritable(total));
  			//}
			 public Map<IntWritable, Integer> getMap() {
  			if(null == map)//lazy loading
   				map = new HashMap<IntWritable, Integer>();
  				return map;
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

		Job job = Job.getInstance(conf, "WordLengthCount");

		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(IntWritable.class);

		job.setJarByClass(WordLengthCount.class);

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