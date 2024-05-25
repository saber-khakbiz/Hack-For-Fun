import  time

import rotatescreen as rs

display = rs.get_primary_display()

listOfAngels= [90, 180, 270, 0]

while True:
    for x in listOfAngels:
        display.rotate_to(x)
        time.sleep(1)