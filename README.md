# CV Management and Analysis System (Python CLI Project)

## 📌 Project Description
This is a Python-based command-line application that allows users to create, manage, analyze, and store multiple CVs.

The system supports adding education, work experience, and skills, and provides an automatic CV scoring and analysis feature.

Data is stored locally using JSON files, and the system supports multiple CV management with update and selection functionality.

---

## ⚙️ Features

- Create multiple CVs
- Add education, experience, and skills
- CV scoring and analysis system
- Skill sorting using lambda function
- Experience display using generator
- Save and load CVs using JSON file
- Update existing CV instead of duplicating
- Logging system using decorator

---

## 🧠 Technologies & Python Concepts Used

- Object-Oriented Programming (OOP)
- Functions and lambda expressions
- Custom decorators (logging system)
- Generators (experience iterator)
- List comprehensions
- File handling (with open)
- JSON serialization
- Exception handling (custom exceptions)
- Control structures (if, for, while)
- CLI menu system


---

## 🚀 How to Run

### 1. Install Python (3.8+ recommended)

### 2. Run the project

```bash
python main.py
💾 Data Storage
All CV data is stored in cv.json
Logs are stored in log.txt
JSON structure supports multiple CVs with unique IDs
🧪 Example Usage
1. Create CV
2. Add Education
3. Add Experience
4. Add Skill
5. Analyze CV
6. Save CV
7. Load CV
📊 CV Analysis System

The system calculates a CV score based on:

Name existence
Email validation
Education entries
Work experience
Number of skills

It also lists missing sections to improve CV quality.

📝 Notes
This project is designed for educational purposes.
JSON is used instead of a database for simplicity.
Logging is implemented using a Python decorator.
The system supports multiple CV management with update functionality.
👨‍💻 Author

Created as a Python final project demonstrating OOP, file handling, and core language features.

📌 Future Improvements
Add database support (SQLite/PostgreSQL)
Add GUI (Tkinter or web interface)
Add CV export to PDF
Add search/filter system for CVs