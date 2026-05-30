# CV Management & Analysis System (Python CLI)

This is a Python-based command-line CV management system that allows users to create, update, analyze, and store multiple CVs using JSON storage.

The system is designed for learning purposes and demonstrates core Python concepts such as OOP, file handling, decorators, and generators.

---

## Features

- Create multiple CVs
- Load and update existing CVs (no duplication)
- Add education, experience, and skills
- Automatic CV scoring and analysis system
- Skill sorting using lambda functions
- Experience iteration using generators
- JSON-based persistent storage
- Logging system using decorators
- Input validation and custom exceptions

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON file handling
- Lambda functions
- Generators
- Decorators
- Exception handling
- CLI (Command Line Interface)

---

## Project Structure

```
project/
│
├── main.py
│
├── models/
│   └── cv.py
│
├── services/
│   ├── analyzer.py
│   └── file_handler.py
│
├── utils/
│   ├── decorators.py
│   ├── exceptions.py
│   └── validators.py
│
├── data/
│   └── cv.json
│
└── log.txt
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Cinarss/cv_system.git
```

### 2. Go to project directory
```bash
cd cv-management-system
```

### 3. Run the application
```bash
python main.py
```

---

## Usage

Run the program and use the menu:

```
====================
CV SYSTEM
====================

1. Create CV
2. Add Education
3. Add Experience
4. Add Skill
5. Analyze CV
6. Save CV
7. Load CV
0. Exit
```

---

## CV Analysis

The system automatically evaluates CVs based on:

- Name completeness
- Email validation
- Education entries
- Work experience
- Skills count

It also provides:
- CV score
- Missing sections
- Sorted skill list

---

## Data Storage

- CV data is stored in `data/cv.json`
- Logs are stored in `log.txt`
- Supports multiple CVs using unique IDs

---

## Notes

- This project is for educational purposes
- No database is used (JSON instead)
- Focus is on Python fundamentals and clean structure

---

## Future Improvements

- Add database support (SQLite / PostgreSQL)
- Add web interface (Flask / Django)
- Export CV as PDF
- Add search and filtering system
- Add authentication system

---