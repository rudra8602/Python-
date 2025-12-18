#This program uses Exception Handling to exit a infinite loop.
#This program prints '-' in the formation of spikes.
import time,sys
try:
    while True:
        for i in range(1,9):
            print('-' * (i*i))
            time.sleep(0.1)
            
           
        for i in range(7,1,-1):
            print('-' * (i*i))
            time.sleep(0.1)
            

except KeyboardInterrupt:
    sys.exit()
