import random

QUESTION_TEMPLATES = {
    "python": [
        "Explain how Python handles memory management.",
        "What are Python decorators and where would you use them?",
        "Explain the difference between list and tuple in Python.",
        "How do you handle exceptions in Python?"
    ],
    "flask": [
        "Explain the request–response lifecycle in Flask.",
        "How do you structure a Flask application?",
        "What is the difference between Flask and Django?",
        "How do you handle errors in Flask?"
    ],
    "django": [
        "Explain Django’s MVT architecture.",
        "What are Django ORM and migrations?",
        "How does Django handle authentication?",
        "Difference between Django and Flask."
    ],
    "sql": [
        "What is normalization and why is it important?",
        "Explain the difference between INNER JOIN and LEFT JOIN.",
        "How do you optimize SQL queries?",
        "What are indexes in databases?"
    ],
    "mongodb": [
        "What is the difference between SQL and MongoDB?",
        "Explain documents and collections in MongoDB.",
        "How does indexing work in MongoDB?",
        "When would you prefer MongoDB over relational databases?"
    ],
    "rest api": [
        "What are REST principles?",
        "Difference between GET and POST methods.",
        "What is HTTP status code 401 vs 403?",
        "How do you secure REST APIs?"
    ],
    "git": [
        "Explain the Git workflow you follow in projects.",
        "Difference between git merge and git rebase.",
        "How do you resolve merge conflicts?",
        "What is the use of .gitignore?"
    ],
    "docker": [
        "What is Docker and why is it used?",
        "Explain Docker image vs container.",
        "How does Docker help in deployment?",
        "What is Docker Compose?"
    ],
    "aws": [
        "What services of AWS are you familiar with?",
        "Explain EC2 and S3.",
        "What is the difference between EC2 and Lambda?",
        "How does AWS help in scalability?"
    ],
    "machine learning": [
        "What is overfitting and how do you prevent it?",
        "Explain bias–variance tradeoff.",
        "Difference between supervised and unsupervised learning.",
        "How do you evaluate a machine learning model?"
    ]
}

GENERAL_QUESTIONS = [
    "Explain a challenging technical problem you solved.",
    "How do you debug a Python application?",
    "How do you approach learning a new technology?",
    "Explain a project you are most proud of."
]

def generate_questions(jd_skills, max_questions=10):
    questions = []

    for skill in jd_skills:
        if skill in QUESTION_TEMPLATES:
            questions.append(random.choice(QUESTION_TEMPLATES[skill]))

    questions.extend(random.sample(GENERAL_QUESTIONS, 2))

    return questions[:max_questions]
