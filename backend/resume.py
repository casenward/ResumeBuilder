from dataclasses import dataclass, field
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
    experience_description: str = ""

    # Projects
    project1_name: str
    project1_description: str

    project2_name: str
    project2_description: str

    # Skills
    skills_programming_languages: List[str]


resume = FullResume(
    # Personal
    name="Casen Ward",
    phone="614-570-4208",
    email="casenward@gmail.com",
    linkedin="linkedin.com/in/casenward",
    github="github.com/casenward",

    # Education
    education_school="Ohio University, Russ College of Engineering and Technology",
    education_location="Athens, Ohio",
    education_graduation="May 2028",
    education_degree="Bachelor of Science",
    education_gpa=3.835,
    education_majors=["Computer Science"],

    # Experience
    experience_organization="Ohio University",
    experience_location="Athens, Ohio",
    experience_role="Student Systems Engineer and Architect",
    experience_start_date="September 2025",
    experience_end_date="Present",
    experience_description="Selected as 1 of 3 Ohio University Students to build a Student Systems Engineering team. Collaborated with faculty and peers to develop innovative solutions for real-world infrastructure challenges. Applied systems engineering principles to model and optimize complex academic and operational systems. Used Jira for task tracking, sprint planning, and agile collaboration.",

    # Project 1
    project1_name="Stock Consensus Calculator",
    project1_description="Developed Python-based backend aggregating analyst ratings from Yahoo Finance and Finnhub. Implemented financial metrics (P/E, P/B, book value, moving averages). Architected modular backend structure (APIs, services, models). Connected lightweight frontend for real-time consensus output. Used Git/GitHub with branch workflows and pull requests.",

    # Project 2
    project2_name="Photography and Videography Portfolio Website",
    project2_description="Designed and built a responsive website using HTML and CSS. Created interactive gallery, carousel, and branded navigation UI. Worked 1-on-1 with client to gather requirements and deliver final product.",

    # Skills
    skills_programming_languages=["C++", "Python", "HTML", "CSS"],
)
