HADOOP_CMD="/usr/local/hadoop/"
STREAM_JAR_PATH="/usr/local/hadoop/share/hadoop/tools/lib/"
INPUT_FILE_PATH="/input"
OUTPUT_PATH="/output"

dumbo start e2.py \
  -hadoop $HADOOP_CMD \
  -hadooplib $STREAM_JAR_PATH \
  -input $INPUT_FILE_PATH/OlympicAthletes.txt \
  -output $OUTPUT_PATH \
  -overwrite yes \
  -file ./data/CountryMedals.txt
