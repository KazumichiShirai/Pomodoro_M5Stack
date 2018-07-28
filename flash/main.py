from m5stack import lcd

lcd.clear()
lcd.setColor(lcd.WHITE)
lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=64, width=2)
lcd.text(lcd.CENTER, lcd.CENTER, "25:00")