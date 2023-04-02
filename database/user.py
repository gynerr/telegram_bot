from sqlalchemy import Column, Integer, VARCHAR, DATE

from .postgre import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, nullable=False)
    username = Column(VARCHAR(32), nullable=True, unique=False)
    req_date = Column()
    upd_date = Column()

    def __str__(self) -> str:
        return f'User:({self.user_id})'
