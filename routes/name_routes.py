from fastapi import APIRouter, HTTPException
from utils.validatorUtils import NameData
from controller.nameController import NameController

router = APIRouter(prefix="/api/names")
controller = NameController()

def handle_response(result):
    """统一处理响应"""
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result

@router.get("")
async def get_all_names():
    result = await controller.get_all_names()
    return handle_response(result)

@router.get("/{id}")
async def get_name(id: int):
    result = await controller.get_name_by_id(id)
    return handle_response(result)

@router.post("")
async def create_name(data: NameData):
    result = await controller.create_name(data)
    return handle_response(result)

@router.put("/{id}")
async def update_name(id: int, data: NameData):
    result = await controller.update_name(id, data)
    return handle_response(result)

@router.delete("/{id}")
async def delete_name(id: int):
    result = await controller.delete_name(id)
    return handle_response(result)
