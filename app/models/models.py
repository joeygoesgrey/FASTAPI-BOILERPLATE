from sqlalchemy import (
    Column,
    String, 
)
from sqlalchemy.dialects.postgresql import UUID
from app.core.db import Base
import uuid
from app.core.db.mixins import TimestampMixin

 
def generate_uuid():
    return str(uuid.uuid4())


class User(Base, TimestampMixin):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True)
    sub = Column(String)
    name = Column(String)
    picture = Column(String)
    password = Column(String)