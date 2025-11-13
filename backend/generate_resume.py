from resume import FullResume

def resume_from_json(data: dict) -> FullResume:
    return FullResume(
        name=data.get("full_name", ""),
        phone=data.get("phone", ""),
        email=data.get("email", ""),
        linkedin=data.get("linkedin", ""),
        github=data.get("github", ""),

        education_school=data.get("uni_name", ""),
        education_location=f"{data.get('edu_city', '')}, {data.get('edu_state', '')}",
        education_graduation=f"{data.get('grad_month', '')} {data.get('grad_year', '')}",
        education_degree=data.get("degree", ""),
        education_gpa=float(data.get("gpa", "0").replace("/", "").strip() or 0),
        education_majors=[m.strip() for m in data.get("majors", "").split(",") if m.strip()],

        experience_organization=data.get("exp_coordinator", ""),
        experience_location=f"{data.get('exp_city', '')}, {data.get('exp_state', '')}",
        experience_role=data.get("exp_name", ""),
        experience_start_date=f"{data.get('exp_start_month', '')} {data.get('exp_start_year', '')}",
        experience_end_date=f"{data.get('exp_end_month', '')} {data.get('exp_end_year', '')}",
        experience_bullets=[
            b.strip("- ").strip()
            for b in data.get("exp_details", "").split("\n")
            if b.strip()
        ],

        project1_name=data.get("proj_name", ""),
        project1_bullets=[
            p.strip()
            for p in data.get("proj_details", "").split("\n")
            if p.strip()
        ],

        skills_programming_languages=[
            s.strip() for s in data.get("skills", "").split(",") if s.strip()
        ],
    )


def resume_to_html(resume: FullResume) -> str:
    bullets_exp = "".join(f"<li>{b}</li>" for b in resume.experience_bullets)
    bullets_proj = "".join(f"<li>{b}</li>" for b in resume.project1_bullets)
    bullets_skills = "".join(f"<li>{s}</li>" for s in resume.skills_programming_languages)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{resume.name} - Resume</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2 {{ margin-bottom: 4px; }}
            ul {{ margin-top: 6px; }}
            .section {{ margin-bottom: 22px; }}
        </style>
    </head>
    <body>
        <h1>{resume.name}</h1>
        <p>{resume.phone} · {resume.email} · {resume.linkedin} · {resume.github}</p>

        <div class="section">
            <h2>Education</h2>
            <p><strong>{resume.education_school}</strong> — {resume.education_location}</p>
            <p>{resume.education_degree}, GPA {resume.education_gpa}</p>
            <p>Majors: {", ".join(resume.education_majors)}</p>
            <p>Graduation: {resume.education_graduation}</p>
        </div>

        <div class="section">
            <h2>Experience</h2>
            <p><strong>{resume.experience_role}</strong> — {resume.experience_organization}, {resume.experience_location}</p>
            <p>{resume.experience_start_date} → {resume.experience_end_date}</p>
            <ul>{bullets_exp}</ul>
        </div>

        <div class="section">
            <h2>Project: {resume.project1_name}</h2>
            <ul>{bullets_proj}</ul>
        </div>

        <div class="section">
            <h2>Skills</h2>
            <ul>{bullets_skills}</ul>
        </div>
    </body>
    </html>
    """
