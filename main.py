from fastapi import FastAPI
from routes import api_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 注册API路由
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
