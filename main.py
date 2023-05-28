#Mengimport module machine yang akan digunaan untuk mengambil pi
#Module utime untuk waktu dalam machine
from machine import Pin, ADC

import utime
import math

#mendefine pin yang akan digunakan
PIN_27 = 27

#mendefine led yang akan digunakan
PIN_18 = 18

#mendefine buzzer
PIN_19 = 19

#define infrared
PIN_3 = 3


#fungsi utama yang akan dijalankan
def main():
    #mengambil nilai ldr sebagain inputan
    photo = ADC(PIN_27)
    
    #mengambil inputan infrared
    infrared = Pin(PIN_3, Pin.IN)
    
    #mengambil lampu RGB sebagai output
    Led = Pin(PIN_18, Pin.OUT, value=0)
    
    #Mengambil Buzzer
    buzz = Pin(PIN_19,Pin.OUT,value=0)
    
    terang = 0
    gelap = 0
    redup = 0
    
    #melakukan looping program utama
    while True:
        x = round(photo.read_u16()/65535*100,2)
        if x >= 0 and x <7 :
            gelap = 0
            redup = 0
            terang = 1
        elif x >=7 and x <10:
            gelap = 0
            redup = (x -7)/(10-7)
            terang = (10-x) /(10-7)
        elif x >= 10 and x <= 50:
            gelap = 0
            redup = (50 - x) / (50 - 10)
            terang = (x - 10) / (50 - 10) 
        elif x >= 50 and x <= 80:
             gelap = 0
             redup = (80 - x) / (80 - 50)
             terang = (x - 80) / (80 - 50)
        elif x > 80:
             gelap = 1
             redup = 0
             terang = 0
            
        if infrared.value() == 0:
            buzz.value(1)
            if gelap == 1 or redup == 1 and terang == 0 :
                Led.value(1)
            elif gelap == 0 and terang == 1:
                Led.value(0)
            utime.sleep(1)
            buzz.value(0)

        print(x)
        #melakukan sleep machine, ini berfungsi sebagai safe counter
        utime.sleep(0.5)
#menjalankan program utama
main()
#debug()
#infrared()
