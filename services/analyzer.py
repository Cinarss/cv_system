def analyze_cv(cv):

    score = 0
    missing = []

    if cv.name:
        score += 10
    else:
        missing.append("Name")

    if cv.email:
        score += 10
    else:
        missing.append("Email")

    if len(cv.education) > 0:
        score += 20
    else:
        missing.append("Education")

    if len(cv.experience) > 0:
        score += 25
    else:
        missing.append("Experience")

    if len(cv.skills) >= 3:
        score += 20
    else:
        missing.append("Skills (min 3 recommended)")

    return {
        "score": score,
        "missing": missing
    }

def sort_skills(skills):
    return sorted(skills, key=lambda x: len(x))


def experience_generator(experiences):
    for exp in experiences:
        yield exp