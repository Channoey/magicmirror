import RPi.GPIO as GPIO

LED_R = 22
LED_G = 27
LED_B = 24
GPIO.setmode(GPIO.BCM)  # BCM编码
GPIO.setwarnings(False)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

GPIO.cleanup()

