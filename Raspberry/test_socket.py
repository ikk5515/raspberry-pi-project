# 라즈베리파이 -> 서버 소켓통신

import websockets
import asyncio

async def send_data(websocket):
    while True:
        # 센서 값 로직 추가
        # sleep 부분 변수로 변경(기본 30초)
        # receive_data에서 받아온 srver_value값에서 센서이름, 변경할 시간 파싱해서 사용 (ex mq5:60 형식으로 넘어옴)
        temp_data = "test:105.2"
        await websocket.send(temp_data)
        await asyncio.sleep(5)  # 5초 대기

async def receive_data(websocket):
    while True:
        # 서버로부터 메시지 수신
        server_value = await websocket.recv()
        print(f"Received data from the server: {server_value}")

async def main():
    # 로컬 테스트 시 사용
    uri = "ws://#:8000/ws"
    # 배포환경으로 테스트 시 사용
    # uri = "wss://port-0-raspberry-pi-project-5mk12alpbcv53c.sel5.cloudtype.app/ws"
    async with websockets.connect(uri) as websocket:
        # send, receive 메소드를 비동기적으로 실행
        send_task = asyncio.ensure_future(send_data(websocket))
        receive_task = asyncio.ensure_future(receive_data(websocket))

        # 두 task 동시에 실행
        await asyncio.gather(send_task, receive_task)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
