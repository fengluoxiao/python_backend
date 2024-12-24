from fastapi import APIRouter, HTTPException
from database.dbQuery import NameTestQuery
from utils.validatorUtils import NameData

router = APIRouter(prefix="/api/names")
query = NameTestQuery()

def handle_response(result):
    """统一处理响应"""
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result

@router.get("")
async def get_all_names():
    return handle_response(query.get_all_names())

@router.get("/{id}")
async def get_name(id: int):
    return handle_response(query.get_name_by_id(id))

@router.post("")
async def create_name(data: NameData):
    return handle_response(query.insert_name(data.dict()))

@router.put("/{id}")
async def update_name(id: int, data: NameData):
    return handle_response(query.update_name(id, data.dict()))

@router.delete("/{id}")
async def delete_name(id: int):
    return handle_response(query.delete_name(id))
