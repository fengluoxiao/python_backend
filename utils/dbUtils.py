from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import urllib.parse

class DatabaseConnection:
    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the database connection if it hasn't been initialized yet"""
        if self._engine is None:
            load_dotenv()
            
            # Get database configuration
            self.DB_HOST = os.getenv("DB_HOST")
            self.DB_PORT = os.getenv("DB_PORT")
            self.DB_USER = os.getenv("DB_USER")
            self.DB_PASSWORD = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
            self.DB_NAME = os.getenv("DB_NAME")
            
            # Create database URL
            self.DATABASE_URL = f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            
            # Create engine
            self._engine = create_engine(
                self.DATABASE_URL,
                pool_recycle=3600,
                pool_pre_ping=True,  # 添加心跳检测
                pool_size=5,  # 连接池大小
                max_overflow=10,  # 超过连接池大小外最多创建的连接
                connect_args={"connect_timeout": 30}
            )
    
    def test_connection(self):
        try:
            with self._engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                result.fetchone()
                return {
                    "status": "success",
                    "message": "Database connected successfully",
                    "connection_string": self.DATABASE_URL.replace(self.DB_PASSWORD, "****")
                }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "details": {
                    "host": self.DB_HOST,
                    "port": self.DB_PORT,
                    "database": self.DB_NAME,
                    "user": self.DB_USER
                }
            }
    
    @classmethod
    def get_instance(cls):
        """Get singleton instance"""
        if cls._instance is None:
            cls._instance = DatabaseConnection()
        return cls._instance
    
    def get_engine(self):
        return self._engine
