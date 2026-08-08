#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' NE555_astable-calc.py

NE555 timer IC (8 pin DIP)
count counter clock wise from left of notch
1 -GND
2 trigger: if its input goes >1/3 Vcc then output goes high
3 output: 200mA max with a voltage of Vcc-1.5V
4 reset: resets the whole timer if input goes low, so keep it high
5 control voltage:  sets the threshold voltage of the threshold pin6
6 threshold: if its input goes >2/3 Vcc then output goes low
7 discharge: if unconnected output is high, if at GND output is low 
8 +Vcc from 5V to 9V
 
Astable circuit:
connect resistors R1, R2 and capacitor C1 in series
(if the capacitor is electrolytic, use the + side toward R2)
connect the junction of R1/R2 to the 555 pin7
connect the junction of R2/C1 to the combined 555 pins 2 and 6
connect lose end of R1 to +Vcc
combine 555 pins8 and pin4 connect to +Vcc
connect the lose end of C1 and 555 pin1 to ground
connect 555 pin3 (output) to a two 10k resistor voltage divider
(protects arduino analog input, max 5.5V limit)

Alternate Astable circuit replacing R1/R2 with one trimpot:
(allows simple frequency adjustment)
Connect one lead of C1 to GND other lead to joined pin2 and pin6
Connect 10k ohm trim pot left side to pin6, right side to +Vcc, and
the wiper to pin7
Connect pin1 to GND
Connect pin8 and pin4 to +Vcc

gives square-wave output at 555 pin3
t_low = 0.693 * (R1 + R2) * C1   sec
t_high = 0.693 * R2 * C1    sec
frequency f = 1.44/((R1 + 2*R2)*C1)   Hz
duty_cycle = 100 * (R1 + R2)/(R1 + 2*R2)   percent

eg.
R1 = 1k ohm
R2 = 7K ohm (6.8k or 4.7k+2.2k)
C1 = 100uF
gives f = 0.96Hz  t(high) = 554ms  t(low) = 486ms  dc(high) = 53%

Used an 'Arduino UNO' programmed in C++ as a frequency meter to
verify  calculations.

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

R1 = 1000  # ohm
R2 = 6800  # ohm
C1 = 1e-6  # 1 uF u--> micru
# frequency in Herz 
f = 1.44/((R1 + 2*R2)*C1)

#print("R1={} R2={} C1={} f={:0.1f}Hz".format(R1, R2, C1, f))
print(f"R1={R1}ohm  R2={R2}ohm  C1={C1}uF  f={f:3.1f}Hz")

# time square-wave pulse is low
t_low = 0.693 * (R1 + R2) * C1  # sec
# time square-wave pulse is high
t_high = 0.693 * R2 * C1   # sec
#print("t_low={}sec  t_high={}sec".format(t_low, t_high))
#print("t_low={}msec  t_high={}msec".format(t_low*1000, t_high*1000))
print(f"t_low={t_low:6.8f}sec  t_high={t_high:6.8f}sec")
print(f"(t_low={t_low*1000:6.5f}msec  t_high={t_high*1000:6.5f}msec)")

duty_cycle = 100 * (R1 + R2)/(R1 + 2*R2)  # percent
print(f"duty_cycle={duty_cycle:6.2f}%")

''' result...
R1=1000ohm  R2=6800ohm  C1=1e-06uF  f=98.6Hz
t_low=0.00540540sec  t_high=0.00471240sec
(t_low=5.40540msec  t_high=4.71240msec)
duty_cycle= 53.42%
'''

