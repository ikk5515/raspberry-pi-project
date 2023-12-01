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

# 기본 메인페이지(프론트 연결 시 삭제 예정)
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# DB 연동 api
# 모든 센서 정보(센서 리스트 반환)
@app.get("/sensors")
def read_sensors():
    # sensors = session.query(SensorTable).distinct(SensorTable.sensor_name).all()
    sensors = session.query(SensorTable.sensor_name).distinct().order_by(SensorTable.sensor_name).all()
    sensor_list = [sensor[0] for sensor in sensors]
    return sensor_list

# 특정 센서 정보
@app.get("/sensors/{sensor_name}")
def read_sensor(sensor_name: str):
    sensor = session.query(SensorTable).filter(SensorTable.sensor_name == sensor_name)\
        .order_by(SensorTable.measure_time.desc()).first()
    sensor_value = [{"sensor_name":sensor.sensor_name, "measure_value":sensor.measure_value}]
    return sensor_value

# 그래프 용 센서값 리스트
@app.get("/sensors/graph/{sensor_name}")
def read_graph(sensor_name: str):
    sensor = session.query(SensorTable).filter(SensorTable.sensor_name == sensor_name)\
        .order_by(SensorTable.measure_time.desc()).limit(25).all()
    return sensor

# 센서 측정 주기 변경
@app.post("/change")
async def change_cycle(item: Item):
    change_value = item.name + ":" + str(item.cycle)
    for client in connected_clients:
        try:
            await client.send_text(change_value)
        except WebSocketDisconnect:
            connected_clients.remove(client)
    return change_value

# 웹 소켓 연결
connected_clients = set()

@app.websocket("/ws")
async def websocket_sensor_data(websocket: WebSocket):
    # client의 websocket접속 허용
    await websocket.accept()
    connected_clients.add(websocket)

    try:
        while True:
            # 메시지를 수신받기 위해 이벤트 루프(소켓)에 cpu양보
            await asyncio.sleep(0)

            # client 메시지 수신대기
            data = await websocket.receive_text()
            print(f"message received : {data} from : {websocket.client}")

            # DB 저장 로직
            sensor_name, measure_value = data.split(":")
            print(sensor_name, '///', measure_value, '///', datetime.now())

            insert_value = SensorTable(
                sensor_name=sensor_name,
                measure_value=float(measure_value),
                measure_time=datetime.now(),
            )

            session.add(insert_value)
            session.commit()

    except WebSocketDisconnect:
        print(f"WebSocket connection disconnected")
    except Exception as e:
        print(f"WebSocket connection closed: {e}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
