import java.io.IOException;
import java.util.*;
import java.util.regex.Pattern;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class NgramInitialRF {

    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, IntWritable>{
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();
        private Queue<String> queue = new LinkedList<String>();

        public void map(Object key, Text value, Context context
                ) throws IOException, InterruptedException {
            Configuration conf = context.getConfiguration();
            String[] temp = value.toString().split("\\W");
            for(int i = 0; i < temp.length; i++){
                if(temp[i].length() > 0) temp[i] = Character.toString(temp[i].charAt(0));
            }
            String togo = String.join(" ", temp);
            StringTokenizer itr = new StringTokenizer(togo);

            Integer n = Integer.parseInt(conf.get("N"));
            String first = new String();

            while (itr.hasMoreTokens()) {
                String str = new String();
                queue.offer(itr.nextToken());
                if(queue.size() == n){
                    String head = new String(queue.poll());
                    String buf = new String("");
                    for(int i = 0; i < n - 1; i++){
                        buf = queue.poll();
                        str = str.concat(buf);
                        queue.offer(buf);
                    }
                    str = head.concat(", ").concat(str);
                    context.write(new Text(str), one);
                    str = head.concat(", *");
                    context.write(new Text(str), one);
                }
                // word.set(queue.poll().concat("00"));
                // context.write(word, one);
            }
        }
    }

    public static class IntSumReducer
            extends Reducer<Text,IntWritable,Text,IntWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values,
                Context context
                ) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        conf.set("N", args[2]);
        conf.set("theta", args[3]);
        Job job = Job.getInstance(conf, "ngram initial rf");
        job.setJarByClass(NgramInitialRF.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
