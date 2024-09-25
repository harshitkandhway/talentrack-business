from app.models.job_post_model import JobPost
from app.repositories.job_post_repository import JobPostRepository

class JobPostService:
    def __init__(self, repository: JobPostRepository):
        self.repository = repository

    def create_job_post(self, job_post: JobPost):
        result = self.repository.save_job_post(job_post)
        return {"id": result['_id'], "result": result['result']}
