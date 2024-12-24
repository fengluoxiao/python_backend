from sqlalchemy import text
from utils.dbUtils import DatabaseConnection
from utils.validatorUtils import validate_sql_params

class NameTestQuery:
    def __init__(self):
        self.db = DatabaseConnection.get_instance()
        self.engine = self.db.get_engine()

    def execute_query(self, query, params=None):
        """通用查询执行方法"""
        try:
            if not isinstance(query, str):
                raise ValueError("Query must be a string")
            
            safe_params = validate_sql_params(params)
            
            with self.engine.connect() as conn:
                result = conn.execute(text(query), safe_params)
                if query.lower().startswith('select'):
                    return {"status": "success", "data": [dict(r) for r in result.mappings()]}
                conn.commit()
                return {"status": "success"}
        except ValueError as ve:
            return {"status": "error", "message": f"Validation error: {str(ve)}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_all_names(self):
        return self.execute_query("SELECT * FROM nameTest")

    def get_name_by_id(self, id):
        return self.execute_query("SELECT * FROM nameTest WHERE id = :id", {"id": id})

    def insert_name(self, data):
        return self.execute_query(
            "INSERT INTO nameTest (name, age, email) VALUES (:name, :age, :email)",
            data
        )

    def update_name(self, id, data):
        data['id'] = id
        return self.execute_query(
            "UPDATE nameTest SET name=:name, age=:age, email=:email WHERE id=:id",
            data
        )

    def delete_name(self, id):
        return self.execute_query("DELETE FROM nameTest WHERE id = :id", {"id": id})
