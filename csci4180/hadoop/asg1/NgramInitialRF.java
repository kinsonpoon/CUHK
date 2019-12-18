import java.io.IOException;
import java.util.*;
import java.util.regex.Pattern;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.MapWritable;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class NgramInitialRF {

    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, MapWritable>{
        private final static IntWritable one = new IntWritable(1);
        private Queue<String> queue = new LinkedList<String>();
        private Map<String, Map> store = new HashMap();

        public void map(Object key, Text value, Context context
                ) throws IOException, InterruptedException {
            Configuration conf = context.getConfiguration();
            String[] temp = value.toString().split("[^a-zA-Z]+");
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
                        str = str.concat(" ").concat(buf);
                        queue.offer(buf);
                    }
                    if(store.containsKey(head)){
                        Map<String, Integer> map = store.get(head);
                        if(map.containsKey(str)){
                            Integer num = (Integer)map.get(str);
                            map.put(str, num + 1);
                            map.put("*", (Integer)map.get("*") + 1);
                            store.put(head, map);
                        }else{
                            map.put(str, 1);
                            map.put("*", (Integer)map.get("*") + 1);
                            store.put(head, map);
                        }
                    }else{
                        Map<String, Integer> map = new HashMap();
                        map.put(str, 1);
                        map.put("*", 1);
                        store.put(head, map);
                    }
                }
            }
        }
		protected void cleanup(Context context)
				throws IOException, InterruptedException {
            Iterator<Map.Entry<String, Map>> ite = store.entrySet().iterator();
            while(ite.hasNext()){
                Map.Entry<String, Map> entry = ite.next();
                String head = entry.getKey();
                Map map = entry.getValue();
                MapWritable toWrite = new MapWritable();
                Iterator<Map.Entry<String, Integer>> it = map.entrySet().iterator();
                while(it.hasNext()){
                    Map.Entry<String, Integer> small = it.next();
                    toWrite.put(new Text(small.getKey()), new IntWritable(small.getValue()));
                }
                context.write(new Text(head), toWrite);
            }
		}
    }

    public static class IntSumReducer
            extends Reducer<Text,MapWritable,Text,FloatWritable> {

        public void reduce(Text key, Iterable<MapWritable> values,
                Context context
                ) throws IOException, InterruptedException {
            Configuration conf = context.getConfiguration();
            Float theta = Float.parseFloat(conf.get("theta"));
            Map<String, Integer> totalMap = new HashMap();

            for(MapWritable map: values){
                Iterator<Map.Entry<Writable, Writable>> tails = map.entrySet().iterator();
                while(tails.hasNext()){
                    Map.Entry<Text, IntWritable> tail = (Map.Entry) tails.next();
                    String sKey = tail.getKey().toString();
                    IntWritable sValue = tail.getValue();
                    if(totalMap.containsKey(sKey)){
                        totalMap.put(sKey, totalMap.get(sKey) + sValue.get());
                    }else{
                        totalMap.put(sKey, sValue.get());
                    }
                }
            }

            Iterator<Map.Entry<String, Integer>> strs = totalMap.entrySet().iterator();
            float totalStar = (float) totalMap.get("*");
            while(strs.hasNext()){
                Map.Entry<String, Integer> str = (Map.Entry) strs.next();
                if(str.getKey().equals("*")) continue;
                float toValue = (float) str.getValue();
                float toGo = toValue / totalStar;
                if(toGo < theta) continue;
                context.write(new Text(key.toString().concat(str.getKey())), new FloatWritable(toGo));
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        conf.set("N", args[2]);
        conf.set("theta", args[3]);
        Job job = Job.getInstance(conf, "ngram initial rf");
        job.setJarByClass(NgramInitialRF.class);
        job.setMapperClass(TokenizerMapper.class);
        // job.setCombinerClass(TokenizerMapper.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);
        job.setMapOutputValueClass(MapWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
