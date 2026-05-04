def calculate_match_score(resume_text, job_skills):
    resume_text = resume_text.lower()
    job_list = [s.strip().lower() for s in job_skills.split(",")]

    matched = []
    missing = []

    for skill in job_list:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(job_list)) * 100 if job_list else 0

    return round(score, 2), matched, missing

# def calculate_match_score(resume_skills, job_skills):
#     # convert job skills string → list
#     job_list = job_skills.lower().split(",")

#     resume_set = set(resume_skills)
#     job_set = set(job_list)

#     matched = resume_set.intersection(job_set)
#     missing = job_set - resume_set

#     score = (len(matched) / len(job_set)) * 100

#     return round(score, 2), list(matched), list(missing)