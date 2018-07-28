from m5stack import lcd
import machine

sec = 0
min = 0

def tcb(timer):
    global sec
    global min
    global t1
    sec += 1
    lcd.clear()
    text = '{0:02d}'.format(min)+":"+'{0:02d}'.format(sec)
    lcd.text(lcd.CENTER, lcd.CENTER, text)
    if sec >= 59:
        sec = 0
        min += 1
    if min >= 2:
        sec = 0
        min = 0
        t1.deinit()

lcd.clear()
lcd.setColor(lcd.WHITE)
lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=64, width=2)
lcd.text(lcd.CENTER, lcd.CENTER, "START")

t1 = machine.Timer(2)
t1.init(period=1000, mode=t1.PERIODIC, callback=tcb)