#!/usr/bin/python

from m5stack import lcd
import time
import machine
import network

MY_SSID = "your ssid"
MY_SSID_PASSWORD = "your password"

def wifi_connect():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  while not wlan.isconnected():
    for net in wlan.scan():
      ssid = net[0].decode('utf-8')
      if ssid == MY_SSID:
        wlan.connect(MY_SSID, MY_SSID_PASSWORD)
        while not wlan.isconnected():
          time.sleep_ms(100)

def rtc_setup():
  rtc = machine.RTC()
  rtc.ntp_sync(server="ntp.jst.mfeed.ad.jp", tz="JST-9")
  while not rtc.synced():
    time.sleep_ms(100)


lcd.println("WiFi connecting...")
wifi_connect()
lcd.println("RTC setup...")
rtc_setup()

lcd.clear()

lcd.setTextColor(lcd.ORANGE, lcd.BLACK)
lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=16, width=2)
while True:
  d = time.strftime("%Y-%m-%d", time.localtime())
  t = time.strftime("%H:%M:%S", time.localtime())
  lcd.print(d, lcd.CENTER, 50)
  lcd.print(t, lcd.CENTER, 130)
  time.sleep_ms(1000)
