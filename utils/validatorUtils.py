from pydantic import BaseModel, validator
import re

class NameData(BaseModel):
    name: str
    age: int
    email: str

    @validator('name')
    def validate_name(cls, v):
        if not v or not re.match(r'^[a-zA-Z0-9\s]{1,50}$', v):
            raise ValueError('Name must be 1-50 characters and contain only letters, numbers and spaces')
        return v

    @validator('age')
    def validate_age(cls, v):
        if not 0 <= v <= 150:
            raise ValueError('Age must be between 0 and 150')
        return v

    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Invalid email format')
        return v

def validate_sql_params(params):
    """验证SQL参数安全性"""
    if not params:
        return {}
        
    sanitized = {}
    for key, value in params.items():
        # 验证键名是否合法
        if not re.match(r'^[a-zA-Z0-9_]+$', str(key)):
            raise ValueError(f"Invalid parameter name: {key}")
        
        # 验证和清理值
        if isinstance(value, (int, float)):
            sanitized[key] = value
        elif isinstance(value, str):
            # 移除潜在的SQL注入字符
            if re.search(r'[\'";]', value):
                raise ValueError(f"Invalid characters in value for {key}")
            sanitized[key] = value
        else:
            raise ValueError(f"Unsupported parameter type for {key}")
            
    return sanitized
