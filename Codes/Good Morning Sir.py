import time
import os
t = time.strftime('%H:%M')
h = int(time.strftime('%H'))


if h>=0 and h<12:
    command = f"say 'Good Morning Sir!'"
    os.system(command)
if h>=12 and h<16:
    com = f"say 'Good Afternoon Sir!'"
    os.system(com)
if h>=16 and h<20:
    come = f"say 'Good Evening Sir!'"
    os.system(come)

if h>=20 and h<24:
    came = f"say 'Good Night Sir!'"
    os.system(came)