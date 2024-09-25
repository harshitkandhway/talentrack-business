from fastapi import FastAPI
from app.api.job_post_routes import router as job_post_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specifies the origins that are allowed (you can use ["*"] for all origins)
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS"],  # Specifies the methods that are allowed
    allow_headers=["Content-Type"],  # Specifies the headers that are allowed
)

app.include_router(job_post_router)
