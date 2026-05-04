import re

SKILLS_DB = [
    "python", "sql", "excel", "java", "html", "css",
    "javascript", "machine learning", "deep learning",
    "data analyst", "ai"
]

def extract_skills(resume_text):
    # clean text
    clean_text = re.sub(r'[^a-zA-Z\s]', ' ', resume_text)
    clean_text = clean_text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        # split multi-word skill
        words = skill.split()

        if all(word in clean_text for word in words):
            found_skills.append(skill)

    return list(set(found_skills))