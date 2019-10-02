aprs --callsign ZR6AIC --output - "AFRICube transponder" | csdr convert_i16_f |csdr dcblock_ff |csdr gain_ff 7000 | csdr convert_f_samplerf 20833 |sudo rpitx -m RF -i - -f 145950
