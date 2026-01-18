import time
import sys

stops = [".", "!", "?"]

def narrate(text: str, WPM: float = 250):
    # Source - https://stackoverflow.com/a/15238748
    # Posted by Bill Gross
    # Retrieved 2026-01-18, License - CC BY-SA 3.0
    LPS = (WPM * 5) / 60
    SPL = 1 / LPS
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        if stops.count(i) > 0:
            time.sleep(SPL * 10)
        elif i == ",":
            time.sleep(SPL * 5)
        else:
            time.sleep(SPL)
    print("")
