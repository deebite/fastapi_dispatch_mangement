from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, Enum, ForeignKey
from datetime import datetime 
from app.core.connection import Base
from sqlalchemy.orm import relationship
import enum

class BatchStatus(enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    AVAILABLE = "AVAILABLE"
    CLOSED = "CLOSED"

class Batch(Base):
    __tablename__ = "batch"

    batch_id = Column(Integer, primary_key=True, index=True)
    batch_serial_number = Column(String, unique=True, index=True)
    product_id = Column(Integer, ForeignKey("product.product_id"), nullable=False)
    max_unit = Column(Integer)
    current_unit = Column(Integer, default=0)
    product_serial_number_list = Column(JSON, default=None)
    status = Column(Enum(BatchStatus), default=BatchStatus.IN_PROGRESS.value)
    qr_code_path = Column(String)
    qr_status = Column(String, default="NOT_SCANNED")
    qr_generated_time = Column(DateTime, default=datetime.utcnow)
    close_at = Column(DateTime, default=None)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    product = relationship("Product", back_populates="batches")