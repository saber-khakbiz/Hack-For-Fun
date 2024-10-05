import time
import platform

try:
    import rotatescreen as rs
except ImportError:
    rs = None

# شناسایی سیستم‌عامل
os_name = platform.system()

if os_name == 'Windows' and rs:
    display = rs.get_primary_display()
    listOfAngles = [90, 180, 270, 0]

    while True:
        for angle in listOfAngles:
            display.rotate_to(angle)
            time.sleep(3)
else:
    print(f"Screen rotation is not supported on {os_name}.")
