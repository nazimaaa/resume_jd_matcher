# Resume-to-JD Matcher with Automated Screening & QnA Trigger

## 📌 Problem Statement
Manual resume screening is time-consuming and subjective. Recruiters often struggle to quickly identify candidates whose skills match a given job description (JD).

This project automates resume screening by:
- Parsing resumes
- Matching them against job descriptions
- Computing a match score using NLP techniques
- Automatically shortlisting candidates based on a threshold
- Triggering tailored interview questions for shortlisted candidates

---

## 🏗️ System Architecture

1. Resume Upload (PDF)
2. Resume Text Extraction
3. Skill Extraction
4. Similarity Scoring
   - TF-IDF (keyword similarity)
   - SBERT (semantic similarity)
   - Skill overlap
5. Weighted Final Score Calculation
6. Threshold-based Screening
7. Automated Interview Question Generation

---

## ⚙️ Technologies & Libraries Used

- **Python**
- **Flask** – Web framework
- **PyPDF2** – Resume PDF parsing
- **scikit-learn** – TF-IDF & cosine similarity
- **sentence-transformers (SBERT)** – Semantic similarity
- **HTML/CSS** – Frontend UI

---

## 🧠 Scoring Logic (Core of the System)

The final match score is calculated using a weighted approach:

| Component | Weight |
|----------|--------|
| Skill Overlap | 60% |
| SBERT Semantic Similarity | 25% |
| TF-IDF Keyword Similarity | 15% |

### Final Score Formula

Final Score =
0.60 × Skill Overlap
0.25 × SBERT Similarity
0.15 × TF-IDF Similarity


This approach ensures:
- Skill relevance is prioritized
- Semantic meaning is captured
- Keyword overlap is considered

---

## 🎯 Screening Threshold Logic

- **Threshold = 55%**
- Designed specifically for **intern-level roles**
- Prevents false rejection of capable candidates
- Aligns better with human recruiter judgment

### Decision Rule
- Score ≥ 55% → Candidate is **Shortlisted**
- Score < 55% → Candidate is **Not Shortlisted**

---

## 🤖 Automated QnA Trigger

- Interview questions are generated **only if the candidate is shortlisted**
- Questions are **skill-based and non-repetitive**
- Uses predefined templates mapped to extracted JD skills
- Includes conceptual, practical, and scenario-based questions

---

## 🧪 Sample Output

**Input:**
- Resume: Python Developer Intern Resume
- Job Description: Python Developer Intern

**Output:**
- Match Score: 55.91%
- Status: Shortlisted
- Interview Questions Triggered Automatically

---

## 🧪 Testing & Validation

- Tested with multiple resumes and job descriptions
- Verified that:
  - Strong matches score higher
  - Weak matches are rejected
- Manual inspection showed strong alignment with human judgment

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/nazimaaa/resume-jd-matcher.git
   cd resume-jd-matcher
2. Install dependencies:
pip install -r requirements.txt
3. Run the application:
python app.py
4. Open a browser and visit:
http://127.0.0.1:5000
