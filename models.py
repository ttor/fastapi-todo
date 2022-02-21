from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy.orm import Session

from database import Base


class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    session_key = Column(String)


def create_todo(db: Session, content: str, session_key: str):
    todo = ToDo(content=content, session_key=session_key)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo(db: Session, item_id: int):
    return db.query(ToDo).filter(ToDo.id == item_id).first()


def update_todo(db: Session, item_id: int, content: str):
    todo = get_todo(db, item_id)
    todo.content = content
    db.commit()
    db.refresh(todo)
    return todo


def get_todos(db: Session, session_key: str, skip: int = 0, limit: int = 100):
    return db.query(ToDo).filter(ToDo.session_key == session_key).offset(skip).limit(limit).all()


def delete_todo(db: Session, item_id: int):
    todo = get_todo(db, item_id)
    db.delete(todo)
    db.commit()


class Contest(Base):
    __tablename__ = "contests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    is_active = Column(Boolean)
    #end_datetime = Column(DateTime)


def create_contest(db: Session, name: str, description: str, image_url: str, is_active: bool):
    contest = Contest(name=content, description=session_key, image_url=image_url, is_active=is_active)
    db.add(contest)
    db.commit()
    db.refresh(contest)
    return contest

def get_contest(db: Session, contest_id: int):
    return db.query(Contest).filter(Contest.id == contest_id).first()

def get_todos(db: Session, session_key: str, skip: int = 0, limit: int = 100):
    return db.query(ToDo).filter(ToDo.session_key == session_key).offset(skip).limit(limit).all()