# 라즈베리파이 -> 서버 소켓통신

import websockets
import asyncio


async def send_data():
    uri = "ws://#:8000/ws"

    async with websockets.connect(uri) as websocket:
        while True:
            # 센서 값 로직 추가
            temp_data = "test"

            await websocket.send(temp_data)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_data())