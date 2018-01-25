#!/bin/bash
hadoop jar $STREAM  \
-mapper ./mapper.py \
-reducer ./reducer.py \
-input /input/*.txt \
-output /output
