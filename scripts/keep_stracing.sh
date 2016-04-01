# !/bin/bash

# if you want to keep straceing when SSH disconnect
# use this command:
# nohup ./keep_stracing.sh &

processname='cdr_collector'
previous_pid=0
while :
    do
    pid=$(pgrep $processname | head -1)
    if [[ -n "$pid" ]]; then # pid exists
        if [[ "$pid" -ne "$previous_pid" ]]; then
            previous_pid="$pid"
            strace -o ${processname}_${pid}.log -T -tt -v -e trace=all -fp "$pid" -s 10000 &
        fi
    fi
    sleep 1
done