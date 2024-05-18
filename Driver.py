from machine import Pin, ADC

import utime
import math

#mendefine pin yang akan digunakan
PIN_2 = 2

#mendefine led yang akan digunakan
PIN_20 = 20

#mendefine buzzer
PIN_11 = 11

#define infrared
PIN_10 = 10

class App:
    photo = ''
    infrared = ''
    led = ''
    buzz = ''
    
    gelap = 0
    redup = 0
    terang = 0
    
    def __init__(self):
        self.photo = ADC(PIN_2)
        self.infrared = Pin(PIN_3, Pin.IN)
        self.led = Pin(PIN_20, Pin.OUT)
        self.buzz = Pin(PIN_11,Pin.OUT)
        
        self.gelap = 0
        self.redup = 0
        self.terang = 0
    
    def mapping(self,rad):
        x = math.sin(rad / 4)
        x = x**2
        return x
    
    def infrared(self):
        x = self.mapping(self.photo.read_u16())
        y = 1024 * math.sin(x / 4)**2
        
        if y < 15:
            self.gelap = 1
            self.redup = 0
            self.terang = 0
        elif y >= 15 and y <= 20:
            self.gelap = (20 - y) / (20 - 15)
            self.redup = (y - 15) / (20 - 15)
            self.terang = 0
        elif y >= 20 and y <= 25:
            self.gelap = 0
            self.redup = (25 - y) / (25 - 20)
            self.terang = (y - 25) / (25 - 20)
        elif y >= 25:
            self.gelap = 0
            self.redup = 0
            self.terang = 1
            
        print(self.gelap,self.redup,self.terang, sept=" ")
        print("AA")

    def app_behaviour(self):
        if self.infrared.value() == 1:
            print("HELLO")
        else:
            if self.gelap < 1 and self.terang == 1:
                self.led.value(0)
            elif self.gelap == 1 and self.terang < 1:
                self.led.value(1)

    def start(self):
        while True:
            print("EE")
            self.infrared()
            
            utime.sleep(0.5)

