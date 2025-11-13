from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

from generate_resume import resume_from_json, resume_to_html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ResumePayload(BaseModel):
    data: Dict[str, Any]


@app.post("/generate-resume")
def generate_resume(payload: ResumePayload):
    resume = resume_from_json(payload.data)
    html = resume_to_html(resume)
    return {"html": html}
