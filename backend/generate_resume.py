from pathlib import Path
from backend.resume import Resume, Education, Experience, Project, Skills


def resume_to_html(resume: Resume) -> str:
    """Convert a Resume object into styled HTML."""

    # Experience section
    experience_html = ""
    for exp in resume.experience:
        bullet_list = "".join(f"<li>{b}</li>" for b in exp.bullets)

        experience_html += f"""
        <div class="item">
            <div class="item-header">
                <span class="item-role">{exp.role}</span>
                <span class="item-location">{exp.organization} – {exp.location}</span>
            </div>
            <div class="item-dates">{exp.start_date} – {exp.end_date}</div>
            <ul class="item-bullets">{bullet_list}</ul>
        </div>
        """

    # Projects section
    projects_html = ""
    for proj in resume.projects:
        bullet_list = "".join(f"<li>{b}</li>" for b in proj.bullets)

        projects_html += f"""
        <div class="item">
            <div class="item-header">
                <span class="item-role">{proj.name}</span>
            </div>
            <ul class="item-bullets">{bullet_list}</ul>
        </div>
        """

    education = resume.education
    skills = resume.skills

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
            margin: 0; padding: 0;
            background: #f7f7f7;
        }}
        .page {{
            width: 800px;
            margin: 20px auto;
            padding: 40px;
            background: white;
            box-shadow: 0 0 8px rgba(0,0,0,0.15);
        }}
        .name {{
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 8px;
        }}
        .contact span {{
            margin-right: 14px;
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
        .item {{
            margin-bottom: 12px;
        }}
        .item-header {{
            display: flex;
            justify-content: space-between;
        }}
        .item-role {{
            font-weight: bold;
        }}
        .item-dates {{
            font-size: 12px;
            color: #666;
        }}
        .item-bullets {{
            margin: 4px 0;
            padding-left: 20px;
        }}
        .item-bullets li {{
            margin: 2px 0;
        }}
    </style>
</head>
<body>
    <div class="page">
        <div class="name">{resume.name}</div>
        <div class="contact">
            <span>{resume.email}</span>
            <span>{resume.phone}</span>
        </div>

        <div class="section">
            <div class="section-title">Experience</div>
            {experience_html}
        </div>

        <div class="section">
            <div class="section-title">Projects</div>
            {projects_html}
        </div>

        <div class="section">
            <div class="section-title">Education</div>
            <div class="item">
                <div class="item-header">
                    <span class="item-role">{education.degree}</span>
                    <span class="item-location">{education.school}</span>
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Skills</div>
            <div class="item">
                {", ".join(skills.skills)}
            </div>
        </div>
    </div>
</body>
</html>
    """