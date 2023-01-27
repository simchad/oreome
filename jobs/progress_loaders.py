"""
general.progress_loaders
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains several progress loaders and bars.

Orignial codes from:
<https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running>.
"""

import sys
import time
from itertools import cycle
from threading import Thread


done = False
#here is the animation
def animate():
    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True

if __name__ == "__main__":
    pass