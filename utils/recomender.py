def generate_recommendations(missing_skills):
    roadmap = []

    for skill in missing_skills:
        if skill == "excel":
            roadmap.append("Learn Excel basics (2 days)")
        elif skill == "sql":
            roadmap.append("Practice SQL queries (3 days)")
        elif skill == "python":
            roadmap.append("Revise Python fundamentals (4 days)")
        elif skill == "machine learning":
            roadmap.append("Start ML basics (5 days)")
        else:
            roadmap.append(f"Learn {skill}")

    return roadmap

def job_priority(score):
    if score >= 80:
        return "🔥 High Priority – Apply Now"
    elif score >= 60:
        return "⚡ Medium Priority – Improve Skills"
    else:
        return "❌ Low Priority – Not Recommended"
    
def create_schedule(roadmap):
    schedule = []
    day = 1

    for task in roadmap:
        schedule.append(f"Day {day}: {task}")
        day += 1

    return schedule