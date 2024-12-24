from fastapi import FastAPI, HTTPException
from database.dbQuery import NameTestQuery
from utils.validatorUtils import NameData

app = FastAPI()
query = NameTestQuery()

def handle_response(result):
    """统一处理响应"""
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result

@app.get("/names")
async def get_all_names():
    return handle_response(query.get_all_names())

@app.get("/names/{id}")
async def get_name(id: int):
    return handle_response(query.get_name_by_id(id))

@app.post("/names")
async def create_name(data: NameData):
    return handle_response(query.insert_name(data.dict()))

@app.put("/names/{id}")
async def update_name(id: int, data: NameData):
    return handle_response(query.update_name(id, data.dict()))

@app.delete("/names/{id}")
async def delete_name(id: int):
    return handle_response(query.delete_name(id))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
