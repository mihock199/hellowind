# ✨ Stylish Python Terminal Output

โปรเจกต์ขนาดเล็กที่ช่วยอัปเกรดการแสดงผลบน Terminal ให้ดูน่าสนใจยิ่งขึ้นด้วยเทคนิคการแสดงผลแบบค่อยๆ พิมพ์ (Typewriter Effect) และการจัดการ ASCII Art

## 🌟 คุณสมบัติ (Features)

- **Slow Print Effect:** ฟังก์ชันที่ทำให้ข้อความไม่โผล่มาพร้อมกันทีเดียว แต่จะค่อยๆ ปรากฏเหมือนการพิมพ์ดีด
- **ASCII Art Support:** รองรับการแสดงผลรูปภาพที่สร้างจากตัวอักษรได้อย่างสวยงาม
- **Customizable Speed:** สามารถปรับความเร็วในการพิมพ์ข้อความได้ตามต้องการ

## 🚀 วิธีการใช้งาน (Usage)

1. คัดลอกโค้ดไปไว้ในไฟล์ `.py` ของคุณ (เช่น `main.py`)
2. กำหนดข้อความหรือ ASCII Art ที่ต้องการ
3. เรียกใช้ฟังก์ชัน `slow_print`

### ตัวอย่างโค้ด (Example)

```python
import sys
import time

def slow_print(text, speed=0.005):
    """
    ฟังก์ชันสำหรับพิมพ์ข้อความแบบหน่วงเวลา
    :param text: ข้อความที่ต้องการพิมพ์
    :param speed: ความเร็วต่อตัวอักษร (วินาที)
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ข้อความ ASCII Art
art = '''
          .-""""-.
         .'  .--.  '.
        /   /    \   \\
       |   |  .-. |   |
       |   | (   )|   |
        \   \ '-' /  /
         '._'---'_.'
'''

# เริ่มต้นการทำงาน
slow_print(">>> Initializing System...", speed=0.05)
slow_print(art, speed=0.002)