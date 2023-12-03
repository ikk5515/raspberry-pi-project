import asyncio
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time
import serial
from Raspberry import test_socket


async def arduino_data(websocket, server_value):
    # port = serial.Serial("/dev/cu.usbmodem11101", baudrate=9600, timeout=None) # /dev/cu.usbmodem11101 수정 필요

    while True:
        # line = port.readline()     # 시리얼모니터 한 줄 ( ~~ 센서 인식값 : @@@ )
        # print(line.decode())      # 수신값 확인

        line = "mq5:340"
        arr = str(line).replace(" ", "").split(":")   # 원본 데이터: mq5:425.00
        if len(arr) < 1:   # 인식값이 아니면..
            continue

        temp_data = ""

        dataType = arr[0]     # mq5, mq7
        data = arr[1]       # data
        if dataType == 'mq5':
            temp_data = "mq5 : " + data
        elif dataType == 'mq7':
            temp_data += "mq7 : " + data + "\n"  # 센서 구별 -> 보내기  더 좋은 방법 찾아보기

        # print(data)

        await test_socket.send_data(websocket, temp_data)

        time.sleep(server_value)


# main() 부분 코드를 라즈베리파이 > 서버 통신 코드에 합칠 수 있으면 좋을 듯
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())
