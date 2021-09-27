import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
led = [17, 27, 22]
switch = [23, 24]
for i in range(len(led)):
  gpio.setup(led[i], gpio.OUT)

for i in range(len(switch)):
  gpio.setup(switch[i], gpio.IN, pull_up_down=gpio.PUD_DOWN)

def switch_fun(pin):
  pwm = gpio.PWM(pin, 1)
  pwm.start(0)
  for dc in range(101):
    pwm.ChangeDutyCycle(dc)
  for dc in range(101):
    pwm.ChangeDuty(100-dc)

for i in range(len(switch)):
  gpio.add_event_detect(switch[i], gpio.RISING, callback=switch_fun, bouncetime=100)

try:
  while True:
    gpio.output(led[2], 1)
    sleep(1)
    gpio.output(led[2], 0)
    sleep(1)
except KeyboardInterrupt:
  print('\nExiting')
finally:
  gpio.cleanup()  
