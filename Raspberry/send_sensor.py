# 라즈베리파이 -> 서버 소켓통신

import websockets
import asyncio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO 핀 번호 지정

async def send_data(tmp_data):
    uri = "ws://#:8000/ws"
    
    async with websockets.connect(uri) as websocket:
        while True:
            # 센서 값 로직 추가
            # setup
            MQ5_pin = 2
            GPIO.setup(MQ5_pin, GPIO.IN)
            
            # loop
            try:
                while True:
                    time.sleep(2)
                    if GPIO.input(MQ5_pin) == 1:
                        print("가스 감지")
                        print(type(GPIO.input(MQ5_pin)))
                        temp_data = tmp_data
            
                        await websocket.send(temp_data)
                    else:
                        print("가스 미감지")
            except:
                print("Error")
            finally:
                # try 구문 종료 후 GPIO핀 초기화
                GPIO.cleanup() 
            
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_data())
