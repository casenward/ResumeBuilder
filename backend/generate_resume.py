from pathlib import Path
from resume import FullResume


def resume_to_html(resume: FullResume) -> str:
    """Convert a FullResume object into a clean HTML resume."""

    # Experience bullets
    exp_bullets_html = "".join(f"<li>{b}</li>" for b in resume.experience_bullets)

    # Project 1 bullets
    project1_html = "".join(f"<li>{b}</li>" for b in resume.project1_bullets)

    # Project 2 bullets
    project2_html = "".join(f"<li>{b}</li>" for b in resume.project2_bullets)

    # Final HTML template
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{resume.name} – Resume</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f7f7f7;
        }}
        .page {{
            width: 800px;
            margin: 30px auto;
            padding: 40px;
            background: white;
            box-shadow: 0 0 8px rgba(0,0,0,0.15);
        }}
        .name {{
            font-size: 32px;
            font-weight: bold;
        }}
        .contact span {{
            margin-right: 12px;
        }}
        .section {{
            margin-top: 30px;
        }}
        .section-title {{
            font-size: 16px;
            font-weight: bold;
            text-transform: uppercase;
            border-bottom: 1px solid #ccc;
            margin-bottom: 8px;
        }}
        ul {{
            padding-left: 20px;
        }}
    </style>

</head>
<body>

<div class="page">

    <div class="name">{resume.name}</div>
    <div class="contact">
        <span>{resume.phone}</span>
        <span>{resume.email}</span>
        <span>{resume.linkedin}</span>
        <span>{resume.github}</span>
    </div>

    <div class="section">
        <div class="section-title">Education</div>
        <p><b>{resume.education_school}</b>, {resume.education_location}</p>
        <p>{resume.education_degree} — GPA: {resume.education_gpa}</p>
        <p>Expected Graduation: {resume.education_graduation}</p>
        <p>Majors: {", ".join(resume.education_majors)}</p>
    </div>

    <div class="section">
        <div class="section-title">Experience</div>
        <p><b>{resume.experience_role}</b> — {resume.experience_organization}, {resume.experience_location}</p>
        <p>{resume.experience_start_date} – {resume.experience_end_date}</p>
        <ul>{exp_bullets_html}</ul>
    </div>

    <div class="section">
        <div class="section-title">Projects</div>

        <p><b>{resume.project1_name}</b></p>
        <ul>{project1_html}</ul>

        <p><b>{resume.project2_name}</b></p>
        <ul>{project2_html}</ul>
    </div>

    <div class="section">
        <div class="section-title">Skills</div>
        <p><b>Programming Languages:</b> {", ".join(resume.skills_programming_languages)}</p>
        <p><b>Version Control:</b> {", ".join(resume.skills_version_control)}</p>
    </div>

</div>

</body>
</html>
"""


def save_resume_html(resume: FullResume, filename: str = "resume.html"):
    html = resume_to_html(resume)
    Path(filename).write_text(html, encoding="utf-8")
    print(f"✔ Resume generated: {filename}")



def resume_from_json(data: dict) -> FullResume:
    return FullResume(
        name=data.get("full_name"),
        phone=data.get("phone"),
        email=data.get("email"),
        linkedin=data.get("linkedin"),
        github=data.get("github"),

        education_school=data.get("uni_name"),
        education_location=f"{data.get('edu_city')}, {data.get('edu_state')}",
        education_graduation=f"{data.get('grad_month')} {data.get('grad_year')}",
        education_degree=data.get("degree"),
        education_gpa=float(data.get("gpa")),
        education_majors=[m.strip() for m in data.get("majors", "").split(",")],

        experience_organization=data.get("exp_coordinator"),
        experience_location=f"{data.get('exp_city')}, {data.get('exp_state')}",
        experience_role=data.get("exp_name"),
        experience_start_date=f"{data.get('exp_start_month')} {data.get('exp_start_year')}",
        experience_end_date=f"{data.get('exp_end_month')} {data.get('exp_end_year')}",
        experience_bullets=[
            b.strip("- ").strip()
            for b in data.get("exp_details", "").split("\n")
            if b.strip()
        ],

        project1_name=data.get("proj_name"),
        project1_bullets=[
            p.strip()
            for p in data.get("proj_details", "").split("\n")
            if p.strip()
        ],

        project2_name="Additional Project Placeholder",
        project2_bullets=["Add more projects using UI later"],

        skills_programming_languages=[
            s.strip()
            for s in data.get("skills", "").split(",")
            if s.strip()
        ],
        skills_version_control=["Git"]
    )
