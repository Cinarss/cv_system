from models.cv import CV
from services.file_handler import save_cv, load_cv
from utils.validators import validate_email
from utils.exceptions import InvalidEmailError
from utils.decorators import log_action
from services.analyzer import analyze_cv, sort_skills, experience_generator

current_cv = None


@log_action
def create_cv():
    global current_cv

    name = input("Name: ")

    while True:
        email = input("Email (or type 'exit' to cancel): ")

        if email.lower() == "exit":
            print("CV creation cancelled.")
            return

        if validate_email(email):
            break

        print("Invalid email format! please try again or type 'exit'.")

    current_cv = CV(name, email)
    current_cv.id = None
    print("CV created!")


@log_action
def add_education():
    if current_cv is None:
        print("Please create CV first!")
        return
    school = input("School: ")
    degree = input("Degree: ")

    current_cv.add_education({"school": school, "degree": degree})


@log_action
def add_experience():
    if current_cv is None:
        print("Please create CV first!")
        return
    company = input("Company: ")
    position = input("Position: ")

    current_cv.add_experience({"company": company, "position": position})


@log_action
def add_skill():
    if current_cv is None:
        print("Please create CV first!")
        return
    skill = input("Skill: ")
    current_cv.add_skill(skill)


def analyze():
    if current_cv is None:
        print("No CV found. Create or load one first.")
        return
    result = analyze_cv(current_cv)
    sorted_skills = sort_skills(current_cv.skills)
    skills_list = [skill for skill in current_cv.skills]

    print("\n===== CV ANALYSIS =====")
    print("Score:", result["score"])
    print("Missing:", result["missing"])
    if result["suggestions"]:
        print("Suggestions:")
        for suggestion in result["suggestions"]:
            print("-", suggestion)
    print("Skills sorted:", sorted_skills)
    print("Skills list (comprehension):", skills_list)
    print("\nExperiences (generator):")
    for exp in experience_generator(current_cv.experience):
        print(exp)


def save():
    global current_cv

    if current_cv is None:
        print("No CV found.")
        return

    data = load_cv()
    cvs = data.get("cvs", [])

    cv_data = current_cv.to_dict()

    if current_cv.id is None:
        existing_ids = [cv["id"] for cv in cvs] if cvs else []
        new_id = max(existing_ids, default=0) + 1

        current_cv.id = new_id
        cv_data["id"] = new_id
        cvs.append(cv_data)

    else:
        cv_data["id"] = current_cv.id

        updated = False
        for i, cv in enumerate(cvs):
            if cv["id"] == current_cv.id:
                cvs[i] = cv_data
                updated = True
                break

        if not updated:
            cvs.append(cv_data)

    data["cvs"] = cvs
    save_cv(data)

    print("Saved (create/update mode)!")


def load():
    global current_cv

    data = load_cv()

    cvs = data.get("cvs", [])

    if not cvs:
        print("No CV found!")
        return

    print("\nAvailable CVs:\n")

    for cv in cvs:
        print(f"{cv['id']}. {cv['name']}")

    choice = int(input("\nSelect CV ID: "))

    selected = next((c for c in cvs if c["id"] == choice), None)

    if not selected:
        print("Invalid selection")
        return

    current_cv = CV(selected["name"], selected["email"])
    current_cv.id = selected.get("id")
    current_cv.education = selected.get("education", [])
    current_cv.experience = selected.get("experience", [])
    current_cv.skills = selected.get("skills", [])

    print("CV loaded!")

def menu():
    while True:
        if current_cv is None:
            current_name = "No CV Loaded"
        else:
            current_name = current_cv.name
        print(f"""
====================
CV SYSTEM
Current CV: {current_name}
====================
1. Create CV
2. Add Education
3. Add Experience
4. Add Skill
5. Analyze CV
6. Save CV
7. Load CV
0. Exit
""")

        choice = input("Choose: ")

        try:
            if choice == "1":
                create_cv()
            elif choice == "2":
                add_education()
            elif choice == "3":
                add_experience()
            elif choice == "4":
                add_skill()
            elif choice == "5":
                analyze()
            elif choice == "6":
                save()
            elif choice == "7":
                load()
            elif choice == "0":
                print("Do not forget to save your CV before exiting!")
                confirm = input("Are you sure you want to exit? (y/n): ")
                if confirm.lower() == "y":
                    break
                else:
                    print("Returning to menu...")
            else:
                print("Invalid option!")
        except Exception as e:
            print("Error:", e)


menu()