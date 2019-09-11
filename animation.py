# Judd Brau
# Period 7
# animation.py
import os, art, time, platform

start = time.time()

for i, el in enumerate(art.animation):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print(el['text'])
    time.sleep(el['speed']*.8),

print(len(art.animation))
print(time.time()-start)
