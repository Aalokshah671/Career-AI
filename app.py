from flask import Flask, render_template, request
import pickle

# correct imports
# from utils.parser import extract_skills
from utils.matcher import calculate_match_score
from utils.recomender import generate_recommendations, job_priority, create_schedule
from utils.pdf_parser import extract_text_from_pdf
from utils.resume_generator import create_resume
from flask import send_file
from flask import request, render_template, send_file
from utils.resume_generator import create_resume

app = Flask(__name__)

# load model once
model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # get inputs
        file = request.files["resume"]
        job_role = request.form["role"]
        job_skills = request.form["job"]

        # extract text from PDF
        resume_text = extract_text_from_pdf(file)

        # extract skills
        # skills = extract_skills(resume_text)

        # calculate score
        score, matched, missing = calculate_match_score(resume_text, job_skills)

        # prediction
        prediction = model.predict([[score]])[0]

        # recommendations
        roadmap = generate_recommendations(missing)
        priority = job_priority(score)
        schedule = create_schedule(roadmap)

        # final result
        result = {
            "score": score,
            "matched": matched,
            "missing": missing,
            "prediction": "Selected" if prediction == 1 else "Not Selected",
            "roadmap": roadmap,
            "priority": priority,
            "schedule": schedule,
            "role": job_role
            
            
        }

    return render_template("index.html", result=result)

# print("CLEAN TEXT:", resume_text)
# print("SKILLS FOUND:", skills)
@app.route("/create_resume", methods=["POST"])
def create_resume_route():

    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "linkedin": request.form["linkedin"],
        "summary": request.form["summary"],
        "skills": request.form["skills"],
        "education": request.form["education"],
        "experience": request.form["experience"],
        "projects": request.form["projects"],
        "certifications": request.form["certifications"],
        "achievements": request.form["achievements"],
        "languages": request.form["languages"],
        "hobbies": request.form["hobbies"]
    }

    # ✅ Create PDF
    file_path = create_resume(data)

    # ✅ Return file
    return send_file(file_path, as_attachment=True)


# ✅ Second page route (correct)
@app.route("/resume_builder")
def resume_builder():
    return render_template("resume_builder.html")

if __name__ == "__main__":
    app.run(debug=True)
