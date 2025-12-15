import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# -------------------------------------------------
# Load SBERT model once
# -------------------------------------------------
sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------------------------
# Skill aliases to handle JD variations
# -------------------------------------------------
SKILL_ALIASES = {
    "python": ["python"],
    "flask": ["flask"],
    "django": ["django"],
    "sql": ["sql", "mysql", "postgresql"],
    "mongodb": ["mongodb", "mongo"],
    "git": ["git", "github"],
    "rest api": ["rest api", "restful api", "api"],
    "docker": ["docker", "containers"],
    "aws": ["aws", "amazon web services", "cloud"],
    "machine learning": ["machine learning", "ml"],
    "nlp": ["nlp", "natural language processing"]
}

# -------------------------------------------------
# Skill Extraction (Resume + JD)
# -------------------------------------------------
def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias in text:
                found_skills.add(skill)

    return list(found_skills)

# -------------------------------------------------
# TF-IDF Similarity (Keyword matching)
# -------------------------------------------------
def tfidf_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

# -------------------------------------------------
# SBERT Similarity (Semantic meaning)
# -------------------------------------------------
def sbert_score(resume_text, jd_text):
    r_emb = sbert_model.encode(resume_text)
    j_emb = sbert_model.encode(jd_text)
    return cosine_similarity([r_emb], [j_emb])[0][0]

# -------------------------------------------------
# Skill Overlap Score
# -------------------------------------------------
def skill_overlap_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0.0
    return len(set(resume_skills) & set(jd_skills)) / len(set(jd_skills))

# -------------------------------------------------
# Experience Extraction (IMPORTANT)
# Example: "1 year", "2+ years"
# -------------------------------------------------
def extract_experience(text):
    text = text.lower()
    match = re.search(r'(\d+)\s*\+?\s*year', text)
    return int(match.group(1)) if match else 0

# -------------------------------------------------
# Experience Match Score
# -------------------------------------------------
def experience_score(resume_exp, jd_exp):
    if jd_exp == 0:
        return 1.0  # No experience required → full score
    return min(resume_exp / jd_exp, 1.0)

# -------------------------------------------------
# FINAL WEIGHTED SCORE (Industry-style)
# -------------------------------------------------
def final_score(resume_text, jd_text, resume_skills, jd_skills):
    tfidf = tfidf_score(resume_text, jd_text)
    sbert = sbert_score(resume_text, jd_text)
    skill_overlap = skill_overlap_score(resume_skills, jd_skills)

    resume_exp = extract_experience(resume_text)
    jd_exp = extract_experience(jd_text)
    exp_score = experience_score(resume_exp, jd_exp)

    score = (
        0.50 * skill_overlap +   # Skills matter most
        0.25 * sbert +           # Semantic meaning
        0.15 * tfidf +           # Keywords
        0.10 * exp_score         # Experience
    )

    return round(score * 100, 2)
