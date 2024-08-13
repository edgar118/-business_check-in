from sqlalchemy import Column, String, Integer
from backend.core.config import Base

class UserType(Base):
    __tablename__ = "user_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)