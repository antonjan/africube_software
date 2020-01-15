#kill all
sudo pkill -f start_rpitx_netcat_8011_80000.sh
sudo pkill rpitx
sleep 2 
sudo pkill -f 80khz_transponder_block.py
sleep 2 
sudo pkill -f rx_sdr
sudo pkill -f ./start_sdrplay_with_fifo.sh
sleep 2 

#start rpitx in 80Khz smpleing on 145
#sudo ./start_rpitx_netcat_8011_80000.sh&
#sleep 2 
#start start gnuradio with cw 80Khz Bandwith
#sudo ./80khz_transponder_block.py&
#sleep 6 
#start rsp sdr and send to fifo at 2Mhz
#sudo ./start_sdrplay_with_fifo.sh&
