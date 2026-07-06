from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, Enum, ForeignKey
from datetime import datetime 
from app.core.connection import Base
from sqlalchemy.orm import relationship
import enum

class PalletStatus(enum.Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"

class Pallet(Base):
    __tablename__ = "pallet"

    pallet_id = Column(Integer, primary_key=True, index=True)
    pallet_serial_number = Column(String, unique=True, index=True)
    product_id = Column(Integer, ForeignKey("product.product_id"), nullable=False)
    max_unit = Column(Integer)
    current_unit = Column(Integer, default=0)
    batch_serial_number_list = Column(JSON, default=None)
    status = Column(String, default="IN_PROGRESS")
    qr_code_path = Column(String)
    qr_status = Column(String, default="NOT_SCANNED")
    qr_generated_time = Column(DateTime, default=datetime.utcnow)
    close_at = Column(DateTime, default=None)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    product = relationship("Product", back_populates="pallets")