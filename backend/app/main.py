from fastapi import FastAPI
from app.routes.learning import router

app = FastAPI(title="NeuroAdapt AI")

app.include_router(router)
