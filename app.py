from flask import Flask, render_template, request
from utils.extractor import extract_text_from_pdf
from utils.matcher import extract_skills, final_score, extract_experience
from utils.qna_generator import generate_questions

app = Flask(__name__)

THRESHOLD = 55  # screening threshold

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # 1️⃣ Get inputs FIRST
    resume_file = request.files["resume"]
    jd_text = request.form["jd"]

    # 2️⃣ Save resume
    path = "resume.pdf"
    resume_file.save(path)

    # 3️⃣ Extract resume text
    resume_text = extract_text_from_pdf(path)

    # 4️⃣ Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    # 5️⃣ Extract experience (NOW variables exist)
    resume_exp = extract_experience(resume_text)
    jd_exp = extract_experience(jd_text)

    # 6️⃣ Calculate final score
    score = final_score(resume_text, jd_text, resume_skills, jd_skills)

    # 7️⃣ Screening decision
    status = "Shortlisted" if score >= THRESHOLD else "Not Shortlisted"

    # 8️⃣ Trigger QnA only if shortlisted
    questions = generate_questions(jd_skills) if status == "Shortlisted" else []

    # 9️⃣ Send data to UI
    return render_template(
        "result.html",
        score=score,
        status=status,
        resume_skills=resume_skills,
        jd_skills=jd_skills,
        questions=questions,
        resume_exp=resume_exp,
        jd_exp=jd_exp
    )

if __name__ == "__main__":
    app.run(debug=True)
