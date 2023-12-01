# 라즈베리파이 -> 서버 소켓통신

import websockets
import asyncio

temp_data = ""
async def send_data(tmp_data):
    # 로컬 테스트 시 사용
    uri = "ws://#:8000/ws"
    # 배포환경으로 테스트 시 사용
    # uri = "wss://port-0-raspberry-pi-project-5mk12alpbcv53c.sel5.cloudtype.app/ws"

    async with websockets.connect(uri) as websocket:
        try:
            temp_data = tmp_data
            print(f"{temp_data} in try")

            await websocket.send(temp_data)
        except:
            print("Error")
        finally:
            print(f"{temp_data} recieved")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_data())
