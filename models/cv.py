class CV:
    def __init__(self, name, email):
        self.id = None  
        self.name = name
        self.email = email
        self.education = []
        self.experience = []
        self.skills = []

    def add_education(self, edu):
        self.education.append(edu)

    def add_experience(self, exp):
        self.experience.append(exp)

    def add_skill(self, skill):
        self.skills.append(skill)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "education": self.education,
            "experience": self.experience,
            "skills": self.skills
        }