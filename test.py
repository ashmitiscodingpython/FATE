import random
import sys
import time

typing_speed = 50
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(5/50)
    print('')

slow_type("hello how are you im fine what about you im curious to know how you are please tell me right now")
