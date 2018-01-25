# 最简单的mapper & reducer
    mapper1.py
    reducer1.py

# 迭代器和生成器优化Mapper 和 Reducer
    mapper.py
    reducer.py

# run.sh hadoop运行命令
	$export STREAM=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar
	$source run.sh:
    hadoop jar $STREAM  \
        -mapper ./mapper.py \
        -reducer ./reducer.py \
        -input /input/*.txt \
        -output /output
	$hadoop fs -cat /output/part-00000 | sort -nk 2 | tail

# 测试是否正确
    echo "foo foo quux labs foo bar quux" | ./mapper.py | sort -k1,1 | ./reducer.py
