#Mengimport module machine yang akan digunaan untuk mengambil pin dan
#Module utime untuk waktu dalam machine
from machine import Pin, ADC

import utime
import math

#mendefine pin yang akan digunakan
PIN_27 = 27
#mendefine led yang akan digunakan
PIN_20 = 20 # kuning
PIN_19 = 19 # merah
PIN_18 = 18 # hijau

def mapping(rad):
        x = math.sin(rad / 4)
        x = x**2
        return x
    

#fungsi utama yang akan dijalankan
def main():
    #mengambil nilai ldr sebagain inputan
    photo = ADC(PIN_27)
    
    #mengambil lampu RGB sebagai output
    kuning = Pin(PIN_20, Pin.OUT)
    merah = Pin(PIN_19, Pin.OUT)
    hijau = Pin(PIN_18, Pin.OUT)
    
    terang = 0
    gelap = 0
    redup = 0
    
    #melakukan looping program utama
    while True:
        x = mapping(photo.read_u16())
        y = 1024 * math.sin(x / 4)**2
        
        if y < 15:
            gelap = 1
            redup = 0
            terang = 0
        elif y >= 15 and y <= 20:
            gelap = (20 - y) / (20 - 15)
            redup = (y - 15) / (20 - 15)
            terang = 0
        elif y >= 20 and y <= 25:
            gelap = 0
            redup = (25 - y) / (25 - 20)
            terang = (y - 25) / (25 - 20)
        elif y >= 25:
            gelap = 0
            redup = 0
            terang = 1
    
        print(gelap, redup, terang, y, sep=' ')
        
        #melakukan sleep machine, ini berfungsi sebagai safe counter
        utime.sleep(0.5)

#menjalankan program utama
main()
