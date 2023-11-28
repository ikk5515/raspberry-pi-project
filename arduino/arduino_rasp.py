import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time
import serial
from Raspberry import send_sensor

def main():
    port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=None)

    while True:
        line = port.readline()     # 시리얼모니터 한 줄 ( ~~ 센서 인식값 : @@@ )
        print(line.decode())
        arr = str(line).replace(" ", "").split(":")
        
        if len(arr) < 1:   # 인식값이 아니면..
            continue

        temp_data = ""

        dataType = arr[0]       # 온도 or 습도 or 가스
        data = arr[1]
        if dataType == 'mq5':
            temp_data += "mq5 : " + data + "\n"
        elif dataType == 'mq7':
            temp_data += "mq7 : " + data + "\n"   # 센서 구별 -> 보내기  더 좋은 방법 찾아보기

        print(temp_data)
        
        send_sensor.send_data(temp_data)
        
        time.sleep(0.01)

#main() 부분 코드를 라즈베리파이 > 서버 통신 코드에 합칠 수 있으면 좋을 듯
if __name__ == "__main__":
   main()
