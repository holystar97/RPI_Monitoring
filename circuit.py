import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D
import busio


# 전역 변수 선언 및 초기화
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)


sda = 2 # GPIO 핀 번호, sda라고 이름이 보이는 핀
scl = 3 # GPIO 핀 번호, scl이라고 이름이 보이는 핀
i2c = busio.I2C(scl, sda)

sensor = HTU21D(i2c) # HTU21D 장치를 제어하는 객체 리턴

def getTemperature() :
        return float(sensor.temperature) # HTU21D 장치로부터 온도 값 읽기
def getHumidity() :
        return float(sensor.relative_humidity) # HTU21D 장치로부터 습도 값 읽기



def measureDistance():
global trig, echo
        GPIO.output(trig, True) # 신호 1 발생
        time.sleep(0.00001) # 짧은시간후 0으로 떨어뜨려 falling edge를 만들기 >$
        GPIO.output(trig, False) # 신호 0 발생(falling 에지)

        while(GPIO.input(echo) == 0):
                pass
        pulse_start = time.time() # 신호 1. 초음파 발생이 시작되었음을 알림
        while(GPIO.input(echo) == 1):
                pass
        pulse_end = time.time() # 신호 0. 초음파 수신 완료를 알림

        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration