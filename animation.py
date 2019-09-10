# Judd Brau
# Period 7
# animation.py

import os, art, time

start = time.time()
for i, el in enumerate(art.animation):
    os.system('clear')
    print(el['text'])
    time.sleep(el['speed']*.8),

print(time.time()-start)
