#from typing import TYPE_CHECKING
from buy_hodl.db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship


class Wallet(Base):
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=True, default=0)
    quarantine = Column(Boolean, nullable=True, default=False)
    asset_id = Column(Integer, ForeignKey("asset.id"), index=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)
    asset = relationship("Asset")
    user = relationship("User", back_populates="wallet")