# Resume-to-JD Matcher – Design Document

## 1. Problem Statement
Manual resume screening is slow, subjective, and prone to errors. Recruiters often rely on keyword-based filtering, which can miss suitable candidates or shortlist under-qualified ones due to variations in terminology and lack of structured evaluation.

This project aims to automate resume screening by objectively comparing resumes with job descriptions using Natural Language Processing (NLP), skill matching, and experience alignment.

---

## 2. System Architecture

1. User uploads resume in PDF format
2. Resume text is extracted
3. Skills are extracted from resume and job description
4. Similarity is calculated using:
   - Skill overlap
   - TF-IDF (keyword similarity)
   - SBERT (semantic similarity)
   - Experience matching
5. A weighted final score is computed
6. Candidate is shortlisted based on a predefined threshold
7. Interview questions are generated for shortlisted candidates

---

## 3. Core Logic

### 3.1 Skill Matching
- Uses predefined skill aliases to handle different terminologies
- Example: "ML" → "Machine Learning"
- Reduces false negatives caused by JD wording differences

### 3.2 Experience Matching
- Extracts experience in years from resume and JD using regex
- Example:
  - JD: *0–2 years experience*
  - Resume: *1 year experience* → Valid match
- Experience contributes to the final score to prevent unfair shortlisting

### 3.3 Similarity Scoring
- **TF-IDF** captures keyword-level similarity
- **SBERT** captures semantic meaning beyond keywords
- **Skill overlap** ensures required skills are prioritized

### 3.4 Final Score Formula
Final Score =
0.50 × Skill Overlap
0.25 × SBERT Similarity
0.15 × TF-IDF Similarity
0.10 × Experience Score

---

## 4. Screening Threshold Logic
- Threshold is set to **55%**
- Optimized for intern and entry-level roles
- Prevents false rejection of capable candidates
- Avoids shortlisting candidates with major skill or experience gaps

---

## 5. User Interface Flow
- Upload resume and paste job description
- View match score and shortlisting status
- Compare resume skills with JD skills
- View experience comparison
- Option to scan another resume

---

## 6. Testing & Validation

- Tested with multiple resumes and job descriptions
- Verified rejection when:
  - Key skills are missing
  - Experience requirements are not met
- Manual inspection shows strong alignment with human recruiter judgment

---

## 7. Limitations & Future Enhancements
- Current experience extraction is rule-based
- Future improvements:
  - Use NLP models for better experience parsing
  - Support multiple resume formats (DOCX)
  - Add email/ATS integration


### 3.4 Final Score Formula

