#!/bin/bash
#python cbc_mode.py > ~/tmp/tmp.txt
#sed "s/'/ /g" ~/tmp/tmp.txt
python cbc_mode.py | sed "s/'/ /g" | sed 's/^.\{2\}//'| awk '{a=a s $0;s=""}END{print a}'
