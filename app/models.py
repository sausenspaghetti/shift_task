from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base



class UserEmployee(Base):
    __tablename__ = 'UserEmployee'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    promotion_date = Column(TIMESTAMP(timezone=True), nullable=True, default=text('now()'))
    salary = Column(Integer, nullable=False)

