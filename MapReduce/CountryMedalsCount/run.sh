#!/bin/bash
HADOOP_CMD="/usr/local/hadoop/bin/hadoop"
STREAM_JAR_PATH="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar"
INPUT_FILE_PATH="/input"
OUTPUT_PATH="/output"

$HADOOP_CMD fs -rm -r $OUTPUT_PATH
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH \
    -output $OUTPUT_PATH \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -file ./mapper.py \
    -file ./reducer.py
