
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from backend.core.config import Base

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    user = relationship("User", back_populates="department")