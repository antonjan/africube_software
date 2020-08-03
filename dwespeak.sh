#!/bin/bash
if [ $# -eq 0 ]
  then
#    echo "No arguments supplied"
    exit 1
fi
if [ $# -eq 1 ]
  then
#    echo "No arguments supplied"
    espeak -v en-sc "$1"
fi

chan=$1
msg=$2
sleep 1
espeak -v en-sc -a 200  "$msg"
# espeak -v en-sc  --stdout "$msg" | aplay -D plughw:0,0
#echo " chan" $chan
#echo " msg" $msg
