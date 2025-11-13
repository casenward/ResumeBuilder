from dataclasses import dataclass
from typing import List


@dataclass
class FullResume:
    # Personal Info
    name: str
    phone: str
    email: str
    linkedin: str
    github: str

    # Education
    education_school: str
    education_location: str
    education_graduation: str
    education_degree: str
    education_gpa: float
    education_majors: List[str]

    # Experience
    experience_organization: str
    experience_location: str
    experience_role: str
    experience_start_date: str
    experience_end_date: str
    experience_bullets: List[str]

    # Projects
    project1_name: str
    project1_bullets: List[str]

    project2_name: str
    project2_bullets: List[str]

    # Skills
    skills_programming_languages: List[str]
    skills_version_control: List[str]
