from fastapi import FastAPI

app = FastAPI()


@app.middleware("http")
async def my_middleware(request, call_next):
    print('ミドルウェアの実行')
    response = await call_next(request)
    return response


@app.get('/')
async def root():
    return {"message": "Hello, World!"}
