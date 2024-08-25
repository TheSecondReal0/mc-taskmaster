from sqlalchemy import (
    Column,
    String,
    Text,
    BigInteger,
    Integer,
    Boolean,
    ForeignKey,
    CheckConstraint,
    TIMESTAMP
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as UUID_PG
from sqlalchemy.ext.declarative import declarative_base
import uuid

from flask_sqlalchemy import SQLAlchemy

from .. import db

Base = db.Model

class Player(Base):
    __tablename__ = 'players'
    id = Column(UUID_PG(as_uuid=True), primary_key=True, default=uuid.uuid4)
    discord_id = Column(BigInteger, nullable=False)
    score = Column(BigInteger, nullable=False, default=0)

    categories = relationship("Category", secondary="player_categories_xref")
    tasks = relationship("Task", secondary="player_tasks_xref", order_by="PlayerTaskXref.time_assigned")


class Category(Base):
    __tablename__ = 'categories'
    id = Column(UUID_PG(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)


class PlayerCategoryXref(Base):
    __tablename__ = 'player_categories_xref'
    player_id = Column(UUID_PG(as_uuid=True), ForeignKey('players.id'), primary_key=True)
    category_id = Column(UUID_PG(as_uuid=True), ForeignKey('categories.id'), primary_key=True)


class Season(Base):
    __tablename__ = 'season'
    id = Column(BigInteger, primary_key=True)
    session = Column(Integer, nullable=False)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(UUID_PG(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(Text, nullable=False)
    points = Column(Integer)
    min_session = Column(Integer)
    max_session = Column(Integer)
    enabled = Column(Boolean, nullable=False, default=True)

    categories = relationship("Category", secondary="task_categories_xref")

    def __init__(self, description, points, min_session=None, max_session=None, enabled=True):
        self.description = description
        self.points = points
        self.min_session = min_session
        self.max_session = max_session
        self.enabled = enabled


class TaskCategoryXref(Base):
    __tablename__ = 'task_categories_xref'
    task_id = Column(UUID_PG(as_uuid=True), ForeignKey('tasks.id'), primary_key=True)
    category_id = Column(UUID_PG(as_uuid=True), ForeignKey('categories.id'), primary_key=True)


class PlayerTaskXref(Base):
    __tablename__ = 'player_tasks_xref'
    player_id = Column(UUID_PG(as_uuid=True), ForeignKey('players.id'), primary_key=True)
    task_id = Column(UUID_PG(as_uuid=True), ForeignKey('tasks.id'), primary_key=True)
    session_assigned = Column(Integer, nullable=False, primary_key=True)
    time_assigned = Column(TIMESTAMP, nullable=False)
    session_resolved = Column(Integer)
    time_resolved = Column(TIMESTAMP)
    status = Column(String(255), CheckConstraint("status IN ('assigned', 'failed', 'completed')"), nullable=False)
