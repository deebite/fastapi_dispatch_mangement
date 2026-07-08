from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.connection import engine, Base



def get_application():
    Base.metadata.create_all(bind=engine)

    _app = FastAPI(title=settings.PROJECT_NAME)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = get_application()

@app.get("/api/health-check")
async def health_check():
    return {"message": "Welcome to dispatch management Web Portal!"}