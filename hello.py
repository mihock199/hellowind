import sys
import time

def slow_print(text, speed=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# เรียกใช้งาน
slow_print(">>> Initializing System...", speed=0.05)
slow_print(text) # ใส่ตัวแปร text จากโค้ดเดิมของคุณ