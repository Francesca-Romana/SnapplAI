from pydantic import BaseModel

class JobSummary(BaseModel):
    title: str
    seniority: str
    modality: str
    experience_years_min: int
    required_skills: str
    nice_to_have_skills: str
    required_education: str
    languages: str



class JobScore(BaseModel):
    analysis: str
    score: int
    a_summirize: str
    company: str
    role: str
    work_mode: str
    apply_link: str
    
    
