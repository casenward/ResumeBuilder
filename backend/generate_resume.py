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
