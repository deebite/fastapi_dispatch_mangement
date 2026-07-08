from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, Enum, ForeignKey
from datetime import datetime 
from app.core.connection import Base
from sqlalchemy.orm import relationship
import enum

class ProductStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, unique=True, index=True)
    product_name = Column(String, index=True)
    description = Column(String)
    model = Column(String)
    variant = Column(String)
    manufacturer_code = Column(String)
    part_no = Column(String)
    sap_code = Column(String)
    status = Column(Enum(ProductStatus), default=ProductStatus.ACTIVE.value)
    image_url = Column(String)
    box_capacity = Column(Integer)
    pallet_capacity = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    batch = relationship("Batch", back_populates="product")
    pallet = relationship("Pallet", back_populates="product")
