import traceback
import websockets
import asyncio
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from arduino import arduino_rasp

uri = "wss://port-0-raspberry-pi-project-5mk12alpbcv53c.sel5.cloudtype.app/ws"

global server_value
server_value = 5


async def send_data(websocket, tmp_data):
    global server_value, temp_data
    try:
        temp_data = tmp_data
        print(f"{temp_data} in try")
        print(f"server_value는 이거 입니다~ {server_value}")
        await websocket.send(temp_data)
    except:
        print("Send Data Error")
    finally:
        print(f"{temp_data} recieved")


async def receive_data(websocket):
    global server_value  # 전역 변수 server_value를 사용합니다.
    while True:
        try:
            # 서버로부터 메시지 수신
            print(1)
            received_value = await websocket.recv()  # 임시 변수를 사용합니다.
            print(2)
            arr = str(received_value).replace(" ", "").split(":")  # 원본 데이터: mq5:425.00
            server_value = int(arr[1])  # 전역 변수 server_value를 업데이트합니다.
            print(f"Received data from the server: {server_value}")
            send_task.cancel()  # 기존의 send_task를 취소합니다.
            send_task = asyncio.ensure_future(
                arduino_rasp.arduino_data(websocket))  # 새로운 send_task를 생성합니다.
        except websockets.ConnectionClosed:
            traceback.print_exc()
            print("Connection closed by the server.")


async def main():
    try:
        async with websockets.connect(uri) as websocket:
            # send, receive 메소드를 비동기적으로 실행
            # send_task = asyncio.ensure_future(send_data(websocket))
            send_task = asyncio.ensure_future(
                arduino_rasp.arduino_data(websocket))  # server_value 인자를 제거합니다.
            receive_task = asyncio.ensure_future(receive_data(websocket))

            # 두 task 동시에 실행
            await asyncio.gather(send_task, receive_task)
    except:
        traceback.print_exc()
    finally:
        print("finally finish")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
