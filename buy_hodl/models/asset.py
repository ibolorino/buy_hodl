#from typing import TYPE_CHECKING
from buy_hodl.db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship


class Asset_Type(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    assets = relationship("Asset", back_populates="type")


class Asset(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    ticker = Column(String, index=True, unique=True, nullable=False)
    current_price = Column(Numeric)
    asset_type_id = Column(Integer, ForeignKey("asset_type.id"))
    type = relationship("Asset_Type", back_populates="assets")