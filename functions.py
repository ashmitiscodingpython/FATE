import time
import sys

def narrate(text: str, WPM: float):
    # Source - https://stackoverflow.com/a/15238748
    # Posted by Bill Gross
    # Retrieved 2026-01-18, License - CC BY-SA 3.0
    LPS = (WPM * 5) / 60
    SPL = 1 / LPS
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(SPL)
