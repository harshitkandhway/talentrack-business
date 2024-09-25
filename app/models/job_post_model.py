from pydantic import BaseModel, Field
from datetime import date

class JobPost(BaseModel):
    title: str
    company_name: str
    years_of_experience: int
    description: str
    requirements: str
    joining_date: date
    salary: float
    location: str
