import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class ParallelDijkstra {

    public static class PDMapper
            extends Mapper<Object, Text, Text, PDNodeWritable>{

        public void map(Object key, Text value, Context context
                ) throws IOException, InterruptedException {
            String[] datas = value.toString().split(" ");
            String src = datas[0];
            IntWritable distance = new IntWritable(Integer.parseInt(datas[1]));

            if(datas.length == 3){
                String[] adjacencyList = datas[2].split(",");
                int lengthOfAdjacencyList = adjacencyList.length;
                PDNodeWritable toGo = new PDNodeWritable(distance, new Text(datas[2]));
                if (lengthOfAdjacencyList > 1){
                    for(int i = 0; i < lengthOfAdjacencyList; i = i + 2){
                        PDNodeWritable temp = new PDNodeWritable(distance, new Text("empty"));
                        if(distance.get() == -1){
                            temp.setdistance(new IntWritable(-1));
                            context.write(new Text(adjacencyList[i]), temp);
                        }else{
                            temp.setdistance(new IntWritable(Integer.parseInt(adjacencyList[i + 1]) + distance.get()));
                            context.write(new Text(adjacencyList[i]), temp);
                        }
                    }
                context.write(new Text(src), toGo);
                }
            }else{
                PDNodeWritable toGo = new PDNodeWritable(distance, new Text(""));
                context.write(new Text(src), toGo);
            }
        }
    }

    public static class PDReducer
        extends Reducer<Text, PDNodeWritable, Text, Text> {

        public void reduce(Text key, Iterable<PDNodeWritable> values, Context context
                ) throws IOException, InterruptedException {
            Integer distance = -1;
            String adjacencyList = "";
            for(PDNodeWritable value: values){
                Integer dist = value.getDistance().get();
                if(!value.getAdjacencyList().toString().equals("empty")){
                    adjacencyList = value.getAdjacencyList().toString();
                }
                if(dist != -1 && ((distance != -1 && dist < distance) || (distance == -1))){
                    distance = dist;
                }
            }
            String toGo = Integer.toString(distance) + " " + adjacencyList;
            context.write(key, new Text(toGo));
        }
    }

    public static class PDFinalReducer
        extends Reducer<Text, PDNodeWritable, Text, Text> {

        public void reduce(Text key, Iterable<PDNodeWritable> values, Context context
                ) throws IOException, InterruptedException {
            Integer distance = -1;
            String adjacencyList = "";
            for(PDNodeWritable value: values){
                Integer dist = value.getDistance().get();
                if(!value.getAdjacencyList().toString().equals("empty")){
                    adjacencyList = value.getAdjacencyList().toString();
                }
                if(dist != -1 && ((distance != -1 && dist < distance) || (distance == -1))){
                    distance = dist;
                }
            }
            String toGo = Integer.toString(distance);
            if(distance!= -1){
                context.write(key, new Text(toGo));
            }
        }
    }


    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();

        String infile = args[0];
        String outfile = args[1];
        String src = args[2];
        int iteration = Integer.parseInt(args[3]);
        String weighted = args[4];

        // Pre Process
        String[] arguments = new String[]{args[0], "pdLI/processOutput0", args[2], weighted};
        PDPreProcess.main(arguments);

        int countIteration = 0;
        for(int i = 0; i < iteration; i++){
            // Process
            if(i != iteration - 1){
                conf.set("mapred.textoutputformat.separator", " ");
                Job job = Job.getInstance(conf, "PD");
                job.setJarByClass(ParallelDijkstra.class);
                job.setMapperClass(PDMapper.class);
                job.setReducerClass(PDReducer.class);
                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(Text.class);
                job.setMapOutputValueClass(PDNodeWritable.class);
                FileInputFormat.addInputPath(job, new Path("/user/hadoop/pdLI/processOutput" + Integer.toString(countIteration) + "/part-r-00000"));
                FileOutputFormat.setOutputPath(job, new Path("pdLI/processOutput" + Integer.toString(countIteration + 1)));
                job.waitForCompletion(true);
            }else{
                Job job = Job.getInstance(conf, "PD");
                job.setJarByClass(ParallelDijkstra.class);
                job.setMapperClass(PDMapper.class);
                job.setReducerClass(PDFinalReducer.class);
                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(Text.class);
                job.setMapOutputValueClass(PDNodeWritable.class);
                FileInputFormat.addInputPath(job, new Path("/user/hadoop/pdLI/processOutput" + Integer.toString(countIteration) + "/part-r-00000"));
                FileOutputFormat.setOutputPath(job, new Path(outfile));
                job.waitForCompletion(true);
            }
            countIteration += 1;
        }
        if(iteration == 0){
            Boolean finished = false;
            while(!finished){
                conf.set("mapred.textoutputformat.separator", " ");
                Job job = Job.getInstance(conf, "PD");
                job.setJarByClass(ParallelDijkstra.class);
                job.setMapperClass(PDMapper.class);
                job.setReducerClass(PDReducer.class);
                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(Text.class);
                job.setMapOutputValueClass(PDNodeWritable.class);
                FileInputFormat.addInputPath(job, new Path("/user/hadoop/pdLI/processOutput" + Integer.toString(countIteration) + "/part-r-00000"));
                FileOutputFormat.setOutputPath(job, new Path("pdLI/processOutput" + Integer.toString(countIteration + 1)));
                job.waitForCompletion(true);
                // check if finished
                FileSystem fs = FileSystem.get(conf);
                Path checkOne = new Path("/user/hadoop/pdLI/processOutput" + Integer.toString(countIteration) + "/part-r-00000");
                Path checkTwo = new Path("/user/hadoop/pdLI/processOutput" + Integer.toString(countIteration + 1) + "/part-r-00000");
                FSDataInputStream dis1 = fs.open(checkOne);
                FSDataInputStream dis2 = fs.open(checkTwo);
                String s1;
                String s2;
                finished = true;
                while((s1 = dis1.readLine()) != null && (s2 = dis2.readLine()) != null){
                    if(!s1.equals(s2)){
                        finished = false;
                        break;
                    }
                }
                //
                countIteration++;
            }
            Job job = Job.getInstance(conf, "PD");
            job.setJarByClass(ParallelDijkstra.class);
            job.setMapperClass(PDMapper.class);
            job.setReducerClass(PDFinalReducer.class);
            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(Text.class);
            job.setMapOutputValueClass(PDNodeWritable.class);
            FileInputFormat.addInputPath(job, new Path("/user/hadoop/pdLI/processOutput" + Integer.toString(countIteration) + "/part-r-00000"));
            FileOutputFormat.setOutputPath(job, new Path(outfile));
            job.waitForCompletion(true);
        }
        //
    }
}
