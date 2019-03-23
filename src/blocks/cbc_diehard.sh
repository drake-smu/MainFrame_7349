#!/bin/bash
cbc_looper(){
    for ((i=0;i<=100000;i++)); do
         python cbc_mode.py
     done
}
#cbc_looper | ~/MainFrame_7349/src/sts-2.1.2/assess 1000000
cbc_looper  |  sed "s/'/ /g"  | sed 's/^.\{2\}//'  | sed 's/\\//g'  | awk 1 ORS=''
#| dieharder -g 200 -a -c ' ' -D default -D histogram -D description
    #awk '{a=a s $0;s=""}END{print a}'

# | dieharder -g 200 -a -c ' ' -D default -D histogram -D description
