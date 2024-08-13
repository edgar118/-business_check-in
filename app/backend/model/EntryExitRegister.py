
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from backend.core.config import PersonType

from backend.core.config import Base


class EntryExitRegister(Base):
    __tablename__ = "entry_exit_register"

    id = Column(Integer, primary_key=True, index=True)
    person_type = Column(String, index=True)
    entry_time = Column(DateTime, index=True)
    exit_time = Column(DateTime, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="entry_exit_register")