import json
import os

FILE_PATH = "data/cv.json"


def save_cv(cv_data):
    os.makedirs("data", exist_ok=True)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(cv_data, f, indent=4, ensure_ascii=False)


def load_cv():
    if not os.path.exists(FILE_PATH):
        return {"cvs": []}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read().strip()

        if not content:
            return {"cvs": []}

        return json.loads(content)