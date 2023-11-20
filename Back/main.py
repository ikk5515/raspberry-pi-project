from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.websockets import WebSocketDisconnect

templates = Jinja2Templates(directory="templates")
app = FastAPI()

class Item(BaseModel):
    name: str
    cycle: int

# 기본 메인페이지
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 웹 소켓 연결
@app.websocket("/ws")
async def websocket_sensor_data(websocket: WebSocket):
    await websocket.accept() # client의 websocket접속 허용
    try:
        while True:
            data = await websocket.receive_text()  # client 메시지 수신대기
            print(f"message received : {data} from : {websocket.client}")

            global testValue # 받아온 data 전역 변수로 사용
            testValue = data

            await websocket.send_text(f"Message text was: {data}") # client에 메시지 전달

    except WebSocketDisconnect:
        print(f"WebSocket connection disconnected")
    except Exception as e:
        print(f"WebSocket connection closed: {e}")


# 센서 값 확인
@app.get("/view/{sensor}")
async def view_value(sensor: str):
    return {"message": f"{sensor}의 측정 값 : {testValue}"}

# 센서 측정 주기 변경
@app.post("/change/")
async def change_cycle(item: Item):
    return item

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
