from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

DB_URI = URL.create(
    port=settings.DB_PORT,
    drivername= settings.DRIVER_NAME,
    username= settings.DB_USERNAME,
    host= settings.DB_HOST,
    database= settings.DB_NAME,
    password= settings.DB_PASSWORD,
)

engine = create_engine(DB_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
