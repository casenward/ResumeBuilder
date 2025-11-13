from resume import FullResume
from generate_resume import save_resume_html


def build_resume() -> FullResume:
    return FullResume(
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
        education_majors=["Computer Science", "Artificial Intelligence"],

        # Experience
        experience_organization="Ohio University",
        experience_location="Athens, Ohio",
        experience_role="Student Systems Engineer and Architect",
        experience_start_date="September 2025",
        experience_end_date="Present",
        experience_bullets=[
            "Selected as 1 of 3 students to build a Student Systems Engineering team.",
            "Collaborated with faculty and peers to develop real-world infrastructure solutions.",
            "Applied systems engineering to optimize academic and operational systems.",
            "Used Jira for task tracking, sprint planning, and cross-team collaboration."
        ],

        # Project 1
        project1_name="Stock Consensus Calculator",
        project1_bullets=[
            "Python backend aggregating analyst ratings (Yahoo Finance, Finnhub).",
            "Implemented P/E, P/B, book value, and momentum calculations.",
            "Built modular backend architecture (APIs, services, models).",
            "Integrated frontend for real-time consensus scoring.",
            "Used Git/GitHub with branch workflows and PR reviews."
        ],

        # Project 2
        project2_name="Photography & Videography Portfolio Website",
        project2_bullets=[
            "Developed responsive site using HTML/CSS.",
            "Implemented custom carousel and gallery UI.",
            "Worked directly with client to gather requirements.",
            "Delivered a professional portfolio platform."
        ],

        # Skills
        skills_programming_languages=["C++", "Python", "HTML", "CSS"],
        skills_version_control=["Git"]
    )


if __name__ == "__main__":
    resume = build_resume()
    save_resume_html(resume, "resume.html")
