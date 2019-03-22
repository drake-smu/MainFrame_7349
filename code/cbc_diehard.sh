#!/bin/bash
#python cbc_mode.py > ~/tmp/tmp.txt
#sed "s/'/ /g" ~/tmp/tmp.txt
rm ~/tmp/cbc.input
for ((i=0;i<=30000;i++)); do
    python cbc_mode.py  >> ~/tmp/cbc.input
done
cat ~/tmp/cbc.input |  sed "s/'/ /g" | sed 's/^.\{2\}//'| awk '{a=a s $0;s=""}END{print a}' | dieharder -a
