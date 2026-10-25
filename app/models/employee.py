from sqlalchemy import Column, Float, Integer, String

from app.db.session import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
