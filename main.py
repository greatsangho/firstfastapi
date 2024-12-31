from containers import Container
import uvicorn
from fastapi import FastAPI
from user.interface.controllers.user_controller import router as user_routers
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()


# app.container = Container()
# Dependency Injector 컨테이너 생성 및 FastAPI와 연결
container = Container()
container.wire(modules=["user.interface.controllers.user_controller"])  # 주입할 모듈 지정
app.container = container
# app.container = Container()
app.include_router(user_routers)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8000)