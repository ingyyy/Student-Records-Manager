# 🎓 Student Records Manager (CLI Tool)

A lightweight, terminal-based Python application designed to manage student records, track course enrollments, calculate GPA/averages, and filter top-performing students.

---

## 🌟 Key Features

- **Student Management:** Add new student profiles with age and courses.
- **Grade Tracking:** Append grades dynamically to existing student records.
- **Course Enrollment Check:** Verify if a student is enrolled in a specific course using set operations for O(1) lookup.
- **Performance Analytics:** Calculate average grades safely without zero-division issues.
- **Top Student Filter:** Filter students achieving above a specified target percentage.
- **Robust Input Handling:** Comprehensive try-except validation loops for numerical inputs.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Data Structures:** Hash Maps (Dictionaries), Sets, Lists

---

## 🚀 Quick Start

### Prerequisites
Make sure you have Python installed:
`python --version`

### Running the Application
1. **Clone the repository:**
   `git clone [https://github.com/YOUR_USERNAME/student-records-manager.git](https://github.com/YOUR_USERNAME/student-records-manager.git)`
   `cd student-records-manager`

2. **Run the script:**
   `python main.py`

---

## 📋 Usage Overview

***********************************
Student Records Manager
***********************************
Choose your input:
1. Add a new student
2. Add grade to a student
3. Check course enrollment
4. Calculate student average grade
5. List students by course
6. Filter top-performing students
7. Exit
===================================

---

## 💡 Future Enhancements
- [ ] Add JSON data persistence (Save/Load records).
- [ ] Implement multi-course addition during student setup.
- [ ] Support case-insensitive name/course inputs.
