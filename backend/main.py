from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

from resume import FullResume
from html import resume_from_json, resume_to_html

app = FastAPI()

# Allow your frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumePayload(BaseModel):
    data: Dict[str, Any]


@app.post("/generate-resume")
def generate_resume(payload: ResumePayload):
    """Accepts JSON from the web form and produces a completed resume HTML."""
    
    json_data = payload.data
    resume = resume_from_json(json_data)      # Convert JSON → FullResume object
    html_output = resume_to_html(resume)      # Convert into full HTML resume

    return {"html": html_output}
