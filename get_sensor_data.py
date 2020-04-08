""" msg2.payload = [{
    "Solar-V1": Math.random()*10,
    "Solar-V2": Math.random()*10,
    "Solar-V3": Math.random()*10,
    "Solar-V4": Math.random()*10,
    "Battery-V1": Math.random()*5,
    "Battery-V2": Math.random()*5,
    "Temp-C1": Math.random()*100,
    "Temp-C2": Math.random()*100,
    "Reset-Count":1,
    "Time":1
},
{
    Igate: "zr6aic",
    Command: "rx",
    Mode: 0

}];
pip install setuptools
sudo pip install git+https://github.com/nicmd/vcgencmd.git
"""
import vcgencmd
import random
import time

Res=2
Tim = time.time()
#CPUc=vcgencmd.measure_temp()
#print str(CPUc)
Mod1 = 0
Sol1 = random.randint(0,7)
Sol2 = random.randint(0,9)
Sol3 = random.randint(4,6)
Sol4 = random.randint(4,6)
Bat1 = random.randint(5,9)
Bat2 = random.randint(5,6)
Tem1 = vcgencmd.measure_temp()
Tem2 = random.randint(-30,60)

print(Sol1)
print(Sol2)
print(Sol3)
print(Sol3)
print(Sol4)
print(Bat1)
print(Bat2)
print(Tem1)
print(str(Tem2))
print(Res)
print(Tim)
#'FROMCALL>TOCALL::ADDRCALL :message text'
file = open("aprs_telemetry.txt","w") 
#print ("Africube Transponder:"+ Mod1 +":" + Sol1 + ":" + Sol2 + ":" + SoL3 + ":" + Sol4 + ":" + Bat1 + ":" + Bat2 + ":" + Tem1 + ":" + Tem2 + ":" + Res ) 
file.write("ZR6AIC>TOCALL::ADDRCALL :Africube,"+ str(Mod1) + "," + str(Sol1) + "," + str(Sol2) + "," + str(Sol3) + "," + str(Sol4) + "," + str(Bat1) + "," + str(Bat2) + "," + str(Tem1) + "," + str(Tem2) + "," + str(Res) ) 
 
file.close() 
