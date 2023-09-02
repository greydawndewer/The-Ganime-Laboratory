a = True
x = 0
import time
while a ==True:
    x += 1
    with open("heart_beat.txt", 'w') as f:
        f.write(str(x))
        f.close()
        print('baka')
        time.sleep(1)
 # this is for the heart to run
