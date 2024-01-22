import org.apache.flink.streaming.api.CheckpointingMode;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class Main {

    static final String TOPIC = "people";
    static final String TOPIC_ERR = "topic-errr";
    static final String BROKERS = "redpanda:29092";

    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.enableCheckpointing(150000);
        env.getCheckpointConfig().setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE);
        env.getCheckpointConfig().setCheckpointStorage("file:///tmp");
        // Define Source
        // Add Sink
        DataStreamSource<String> source1 = env.fromElements("abc");
        DataStreamSource<String> source2 = env.fromElements("123");
        source1.union(source2).print();
        env.execute("Kafka2postgres");
    }
}
