import sys
import time

def ani(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

ani("Hello, this is a typewriter animation!", delay=0.1)