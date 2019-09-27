soapy=0,driver=sdrplay

sudo nano /etc/modprobe.d/blacklist.conf


Now add the following by cut and paste:


#sdrplay

blacklist sdr_msi3101

blacklist msi001

blacklist msi2500 
#################################
cd ~/wrkgit clone https://github.com/sdrplay/gr-osmosdrcd gr-osmosdr && git checkout sdrplay2 && mkdir build && cd buildmkdir -p ~/wrk/libs/gr-osmosdr-sdrplaycmake -DCMAKE_INSTALL_PREFIX=~/wrk/libs/gr-osmosdr-sdrplay -DENABLE_NONFREE=yes -˓→DENABLE_BLADERF=OFF ..make && make install


Full-duplex: YES
  Supports AGC: YES
  Stream formats: CS16, CF32
  Native format: CS16 [full-scale=32767]
  Antennas: RX
  Corrections: DC removal
  Full gain range: [0, 42] dB
    IFGR gain range: [20, 59] dB
    RFGR gain range: [0, 3] dB
  Full freq range: [0.01, 2000] MHz
    RF freq range: [0.01, 2000] MHz
    CORR freq range:  MHz
  Sample rates: 0.25, 0.5, 1, 2, 2.048, 6, 7, 8, 9, 10 MSps
  Filter bandwidths: 0.2, 0.3, 0.6, 1.536, 5, 6, 7, 8 MHz

