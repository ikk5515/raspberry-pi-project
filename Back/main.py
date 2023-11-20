from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates")
app = FastAPI()

testValue = 30

class Item(BaseModel):
    name: str
    cycle: int

# 기본 메인페이지
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
