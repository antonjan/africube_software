python ./switch_beacon_on.py
python -m pysstv --mode Robot36 --vox --fskid ZR6AIC AfriCube.png sstv.wav
aplay -D plughw:1,0 sstv.wav
python ./switch_beacon_off.py
