from fastapi import FastAPI

from app.api.health import router as health_router


app = FastAPI(
    title="TechieHorizon Job Automation",
    description="Job application management platform for DevOps candidates",
    version="0.1.0",
)


app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "TechieHorizon Job Automation API",
        "version": "0.1.0",
    }