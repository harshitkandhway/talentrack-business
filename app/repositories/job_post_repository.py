from elasticsearch import Elasticsearch
from app.models.job_post_model import JobPost

class JobPostRepository:
    def __init__(self, es_client: Elasticsearch, index_name: str = "job_posts"):
        self.es_client = es_client
        self.index_name = index_name

    def save_job_post(self, job_post: JobPost):
        if not self.es_client.indices.exists(index=self.index_name):
            self.es_client.indices.create(index=self.index_name)
        doc = job_post.model_dump()
        return self.es_client.index(index=self.index_name, document=doc)
