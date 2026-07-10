from sqlalchemy import Column, Integer, String
from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    credits = Column(Integer)
    department_id = Column(Integer)