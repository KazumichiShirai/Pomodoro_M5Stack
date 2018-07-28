from m5stack import lcd
import machine

def tcb(timer):
    lcd.clear()
    lcd.text(lcd.CENTER, lcd.CENTER, "26:00")

lcd.clear()
lcd.setColor(lcd.WHITE)
lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=64, width=2)
lcd.text(lcd.CENTER, lcd.CENTER, "25:00")

t1 = machine.Timer(2)
t1.init(period=1000, mode=t1.PERIODIC, callback=tcb)