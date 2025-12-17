# Resume-to-JD Matcher – Design Document

## 1. Problem Statement
Manual resume screening is slow, subjective, and prone to errors. Recruiters often rely on keyword-based filtering, which can miss suitable candidates or incorrectly shortlist candidates due to variations in terminology and lack of structured evaluation.

This project aims to automate resume screening by objectively comparing resumes with job descriptions using Natural Language Processing (NLP), skill matching, and experience alignment.

---

## 2. System Architecture

1. User uploads a resume in PDF format
2. Resume text is extracted from the PDF
3. Skills are extracted from both resume and job description
4. Similarity is calculated using:
   - Skill overlap
   - TF-IDF (keyword similarity)
   - SBERT (semantic similarity)
   - Experience matching
5. A weighted final score is computed
6. Candidate is shortlisted based on a predefined threshold
7. Interview questions are generated automatically for shortlisted candidates

---

## 3. Core Logic

### 3.1 Skill Matching
- Uses predefined skill aliases to handle variations in terminology across resumes and job descriptions
- Example: “ML” → “Machine Learning”, “Cloud” → “AWS”
- Reduces false negatives caused by different wording in job descriptions

### 3.2 Experience Matching
- Experience is extracted from resume and job description using regex-based pattern matching
- Example:
  - JD: *0–2 years experience*
  - Resume: *1 year experience* → Valid match
- Experience contributes to the final score to prevent unfair shortlisting of under-qualified candidates

### 3.3 Similarity Scoring
- **TF-IDF** captures keyword-level similarity between resume and JD
- **SBERT** captures semantic similarity by understanding contextual meaning
- **Skill overlap** ensures required skills are given higher importance

### 3.4 Final Score Formula
The final score is calculated using a weighted approach:

Final Score =
- 0.50 × Skill Overlap  
- 0.25 × SBERT Similarity  
- 0.15 × TF-IDF Similarity  
- 0.10 × Experience Score  

This weighting prioritizes core skills while still considering meaning, keywords, and experience.

---

## 4. Screening Threshold Logic
- Threshold is set to **55%**
- Designed specifically for intern and entry-level roles
- Prevents false rejection of capable candidates
- Avoids shortlisting candidates with major skill or experience gaps

---

## 5. User Interface Flow
- User uploads resume and pastes job description
- System displays:
  - Match score
  - Shortlisting status
  - Extracted resume skills
  - Extracted JD skills
  - Experience comparison
- A “Scan Another Resume” option allows repeated evaluations

---

## 6. Unit Tests / Basic Test Harness
- Core functions were tested using multiple resume and job description samples
- Test scenarios included:
  - Matching technical roles (Python/Java Developer)
  - Mismatched roles (IT Support vs Software Developer)
  - Experience mismatch cases
- Results were manually verified to ensure consistency and correctness

---

## 7. Testing & Validation
- Tested with multiple resumes and job descriptions
- Verified rejection when:
  - Required skills are missing
  - Experience requirements are not met
- Manual inspection shows strong alignment with human recruiter judgment

---

## 8. Limitations & Future Enhancements
- Current experience extraction is rule-based and limited to simple patterns
- Future enhancements include:
  - Advanced NLP models for experience parsing
  - Support for DOCX resumes
  - Email or ATS system integration
  - Learning-based skill weighting
