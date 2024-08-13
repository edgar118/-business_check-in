from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from backend.core.config import Base, PersonType

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)
    document_id = Column(Integer, index=True, unique=True)

    user_type_id = Column(
        Integer, ForeignKey('user_type.id'), index=True
    )
    user_type = relationship(
        'UserType', foreign_keys=[user_type_id]
    )

    department_id = Column(
        Integer, ForeignKey('department.id'), index=True
    )
    department = relationship(
        'Department', back_populates='user'
    )

    entry_exit_register = relationship("EntryExitRegister", back_populates="user")