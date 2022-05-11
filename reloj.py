from datetime import datetime
import os
from time import sleep

while True:
    print("La hora es: {}:{}:{}".format(datetime.now().hour, datetime.now().minute, datetime.now().second))
    sleep(1)
    os.system('clear')
