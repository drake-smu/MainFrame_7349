#!/bin/bash
cbc_looper(){
    for ((i=0;i<=300;i++)); do
         python /home/david/MainFrame_7349/src/blocks/cbc_mode.py
     done
}
#cbc_looper | ~/MainFrame_7349/src/sts-2.1.2/assess 1000000
cbc_looper
#| dieharder -g 200 -a -c ' ' -D default -D histogram -D description
    #awk '{a=a s $0;s=""}END{print a}'

# | dieharder -g 200 -a -c ' ' -D default -D histogram -D description
