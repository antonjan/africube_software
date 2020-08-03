#espeak -v en-sc  --stdout "Africube transponder"| aplay -D hw:1,0
#sudo apt-get install libttspico-utils

while true

	echo "."
do

#espeak -a 200 -v en-sc  --stdout "Africube transponder  Zulu  Romio  Six  Alfa  India   Charlie"| aplay -D plughw:0,0
pico2wave -w lookdave.wav "Look Dave, I can see you're really upset about this." && aplay lookdave.wav  
sleep 3
done
