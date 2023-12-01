import asyncio

from fastapi import FastAPI, WebSocket, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocketDisconnect
from datetime import datetime
from database import session
from models import SensorTable, Sensor

templates = Jinja2Templates(directory="templates") # 템플릿 사용

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")  # 정적파일 경로설정

# 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    cycle: int

# 기본 메인페이지
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# DB 연동 api
# 모든 센서 정보(센서 리스트 반환)
@app.get("/sensors")
def read_sensors():
    # sensors = session.query(SensorTable).distinct(SensorTable.sensor_name).all()
    sensors = session.query(SensorTable.sensor_name).distinct().all()
    sensor_list = [sensor[0] for sensor in sensors]
    return sensor_list

# 특정 센서 정보
@app.get("/sensors/{sensor_name}")
def read_sensor(sensor_name: str):
    sensor = session.query(SensorTable).filter(SensorTable.sensor_name == sensor_name).all()
    return sensor

# 센서 측정 주기 변경

# asyncio 이벤트, WebSocket을 통해 데이터를 전송할 때 신호를 보내기 위한 것
send_data_event = asyncio.Event()

@app.post("/change")
async def change_cycle(item: Item, background_tasks: BackgroundTasks):
    # 소켓통신으로 입력받은 주기 넘기기
    # global websocket_global
    # if websocket_global:
    #     await websocket_global.send_text({item})
    global test123
    test123 = item

    send_data_event.set()

    return item

# 웹 소켓 연결
connected_clients = set()
websocket_global = None

@app.websocket("/ws")
async def websocket_sensor_data(websocket: WebSocket):
    global websocket_global
    await websocket.accept()  # client의 websocket접속 허용
    connected_clients.add(websocket)
    websocket_global = websocket

    try:
        while True:
            await asyncio.sleep(0)

            if send_data_event.is_set():
                await websocket_global.send_text({test123})

            data = await websocket.receive_text()  # client 메시지 수신대기
            print(f"message received : {data} from : {websocket.client}")

            # DB 저장 로직
            sensor_name, measure_value = data.split(":")
            print(sensor_name, '///', measure_value, '///', datetime.now())

            mea_value = SensorTable(
                sensor_name=sensor_name,
                measure_value=float(measure_value),
                measure_time=datetime.now(),
            )

            session.add(mea_value)
            session.commit()

            # global testValue # 받아온 data 전역 변수로 사용
            # testValue = data
            # server_value = "tttt"
            # await websocket.send_text({server_value}) # client에 메시지 전달
            send_data_event.clear()

    except WebSocketDisconnect:
        print(f"WebSocket connection disconnected")
    except Exception as e:
        print(f"WebSocket connection closed: {e}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
