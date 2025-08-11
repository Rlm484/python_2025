import sys
import time

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

typewriter_effect("Hello, this is a typewriter animation!", delay=0.1)