from fastapi import APIRouter, HTTPException, Depends
from app.models.job_post_model import JobPost
from app.services.job_post_service import JobPostService
from app.repositories.job_post_repository import JobPostRepository
from elasticsearch import Elasticsearch

router = APIRouter()

def get_job_post_service():
    es_client = Elasticsearch("http://localhost:9200")  # Adjust the URL to your Elasticsearch instance
    repository = JobPostRepository(es_client)
    return JobPostService(repository)

@router.post("/job_posts/", response_model=dict)
async def create_job_post(job_post: JobPost, service: JobPostService = Depends(get_job_post_service)):
    return service.create_job_post(job_post)
