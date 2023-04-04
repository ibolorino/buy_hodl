from buy_hodl.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class TokenBlacklist(Base):
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)