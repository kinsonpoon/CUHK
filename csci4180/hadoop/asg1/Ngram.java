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

public class Ngram {
	public static class TokenizerMapper extends 
			Mapper<LongWritable, Text,Text, IntWritable> {
		private final static IntWritable one = new IntWritable(1);

		
		
        //private StringBuilder gramBuilder = new StringBuilder();

		public void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
				Configuration mapconf = context.getConfiguration();
				Integer gram_length = Integer.parseInt(mapconf.get("N"));
			

			  
			String[] tok = value.toString().split("[^a-zA-Z]+");
			List<String> token=new ArrayList<String>();  
			//remove null
			for(String data:tok){
				if(!data.equals("")){
					token.add(data);
				}

			}
			String[] tokens = new String[token.size()]; 
			tokens=token.toArray(tokens);
			System.out.println(Arrays.toString(tokens));
			//StringTokenizer tokenizer = new StringTokenizer(line);
			String last=mapconf.get("last");
			if(!last.equals("123")){
				for(int x =0;x<gram_length-1;x++){
					last=mapconf.get("last");
					String s= "";
					s+=last;
					for(int y=0;y+last.length()/2<gram_length;y++){
						
						s+=tokens[y].charAt(0);
						s+=" ";

					}
					System.out.println("Debug: " +s);
            		if(last.length()!=2){
            			mapconf.set("last",last.substring(2,last.length()));

            		}
            		else{
            		mapconf.set("last","123");
            	}
            		context.write(new Text(s.substring(0, s.length() - 1)), one);
				}

            }



			//after 1
			 for (int i = 0; i < tokens.length; i++){

                //gramBuilder.setLength(0);
                String s= "";
                if(i + gram_length <= tokens.length) {
                   for(int j = i; j < i + gram_length; j++) {
                       //gramBuilder.append(tokens[j].charAt(0));
                       //gramBuilder.append(" ");
                   	s+=tokens[j].charAt(0);
                   	s+=" ";
                   }

                   //System.out.println("Debug: " + new Text(gramBuilder.tostring()));
                   //context.write(new Text(gramBuilder.tostring()), one);
                   System.out.println("Debug: " +s.substring(0, s.length() - 1));
                   context.write(new Text(s.substring(0, s.length() - 1)), one);
                }

            }
            //last word of line
            last=mapconf.get("last");
            String s= "";
            if(last.equals("123")){
            	for(int k=tokens.length-gram_length+1;k<tokens.length;k++){
            		
            		s+=tokens[k].charAt(0);
                   	s+=" ";
                   
            	}
            	mapconf.set("last",s);
            	System.out.println("last: " +s);
            }
}


		



			//Iterator<Map.Entry<String, Integer>> it = map.entrySet().iterator();
  			//while(it.hasNext()) {
   			//	Map.Entry<String, Integer> entry = it.next();
   			//	String sKey = entry.getKey();
   			//	wordLength.set(sKey.length());
  			//	int total = entry.getValue().intValue();
   			//	context.write(wordLength, new IntWritable(total));
  			//}
		




		
	}

	public static class Reduce extends 
			Reducer<Text , IntWritable,Text, IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values,
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
		conf.set("last","123");
		conf.set("N",args[2]);

		Job job = Job.getInstance(conf, "wordcount");

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		job.setJarByClass(Ngram.class);

		job.setMapperClass(TokenizerMapper.class);
		job.setCombinerClass(Reduce.class);
		job.setReducerClass(Reduce.class);

		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		job.waitForCompletion(true);
	}
}