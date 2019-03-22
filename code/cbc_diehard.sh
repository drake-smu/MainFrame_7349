#!/bin/bash
cbc_looper(){
    for ((i=0;i<=30000;i++)); do
         python cbc_mode.py |  sed "s/'/ /g" | sed 's/^.\{2\}//'| awk '{a=a s $0;s=""}END{print a}'

    done
}
cbc_looper | ~/MainFrame_7349/src/sts-2.1.2/assess 1000000
cbc_looper | dieharder -a

