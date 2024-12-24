from database.dbQuery import NameTestQuery
from utils.validatorUtils import NameData

class NameController:
    def __init__(self):
        self.query = NameTestQuery()

    async def get_all_names(self):
        """获取所有名称记录"""
        return self.query.get_all_names()

    async def get_name_by_id(self, id: int):
        """根据ID获取单个名称记录"""
        return self.query.get_name_by_id(id)

    async def create_name(self, data: NameData):
        """创建新的名称记录"""
        return self.query.insert_name(data.dict())

    async def update_name(self, id: int, data: NameData):
        """更新指定ID的名称记录"""
        return self.query.update_name(id, data.dict())

    async def delete_name(self, id: int):
        """删除指定ID的名称记录"""
        return self.query.delete_name(id)
