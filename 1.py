import os
from itertools import repeat
import time
class TrafficLight:
     __color='o'


     def running(self):
        for _ in repeat(0):
            sv = TrafficLight.__color
            a=sv
            print('\033[31m\033[6m {}'.format(a))
            time.sleep(7)
            print('\033[6m\033[33m {}'.format(a))
            time.sleep(3)
            print('\033[6m\033[32m {}'.format(a))
            time.sleep(2)
            os.system('cls||clear')
            
a = TrafficLight()
a.running()




