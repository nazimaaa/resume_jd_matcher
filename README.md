# Resume-to-JD Matcher with Automated Screening & QnA Trigger

## 📌 Problem Statement
Manual resume screening is time-consuming, subjective, and error-prone. Recruiters often struggle to accurately identify candidates whose skills and experience align with a given job description (JD), especially when different terminologies are used.

This project automates resume screening by:
- Parsing resumes
- Matching them against job descriptions
- Computing a match score using NLP techniques
- Considering skills, semantic similarity, and experience
- Automatically shortlisting candidates based on a threshold
- Triggering tailored interview questions for shortlisted candidates

---

## 🏗️ System Architecture

1. Resume Upload (PDF)
2. Resume Text Extraction
3. Skill Extraction (with alias handling)
4. Similarity Scoring
   - TF-IDF (keyword similarity)
   - SBERT (semantic similarity)
   - Skill overlap
   - Experience matching
5. Weighted Final Score Calculation
6. Threshold-based Screening
7. Automated Interview Question Generation
8. Option to scan another resume in the same session

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

The final match score is calculated using a weighted, human-like approach:

| Component | Weight |
|----------|--------|
| Skill Overlap | 50% |
| SBERT Semantic Similarity | 25% |
| TF-IDF Keyword Similarity | 15% |
| Experience Matching | 10% |

### Final Score Formula

Final Score =  
0.50 × Skill Overlap  
0.25 × SBERT Similarity  
0.15 × TF-IDF Similarity  
0.10 × Experience Score  

This approach ensures:
- Skill relevance is prioritized
- Semantic meaning is captured
- Keyword overlap is considered
- Experience mismatch is penalized

---

## 🎯 Screening Threshold Logic

- **Threshold = 55%**
- Designed specifically for **intern / entry-level roles**
- Prevents false rejection of capable candidates
- Avoids shortlisting under-qualified candidates for higher requirements

### Decision Rule
- Score ≥ 55% → Candidate is **Shortlisted**
- Score < 55% → Candidate is **Not Shortlisted**

---

## 🧠 Experience Matching Logic

- Experience is extracted from resume and JD using regex
- Example:
  - JD: *0–2 years experience*
  - Resume: *1 year experience* → Valid match
- If JD requires experience and resume does not meet it, the final score is reduced
- Experience contributes **10%** to the overall score

---

## 🤖 Automated QnA Trigger

- Interview questions are generated **only if the candidate is shortlisted**
- Questions are dynamically generated based on extracted JD skills
- Includes:
  - Conceptual questions
  - Practical questions
  - Scenario-based questions
- Prevents unnecessary interview questions for rejected candidates

---

## 🎨 User Interface Features

- Clean and simple upload interface
- Displays:
  - Match score
  - Shortlisting status
  - Resume skills vs JD skills
  - Experience comparison
- Includes **“Scan Another Resume”** button for better usability

---

## 🧪 Sample Output

**Input:**
- Resume: Python / AI-ML Intern Resume
- Job Description: AI/ML Intern

**Output:**
- Match Score: 52.84%
- Status: Not Shortlisted
- Experience Mismatch Highlighted
- Interview Questions Not Triggered

---

## 🧪 Testing & Validation

- Tested with multiple resumes and job descriptions
- Verified that:
  - Strong matches score higher
  - Missing skills reduce score
  - Experience mismatch prevents shortlisting
- Results align closely with human recruiter judgment

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/nazimaaa/resume_jd_matcher.git
   cd resume-jd-matcher
2. Install dependencies:
pip install -r requirements.txt
3. Run the application:
python app.py
4. Open a browser and visit:
http://127.0.0.1:5000

