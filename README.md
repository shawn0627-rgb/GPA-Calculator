## 📚 Self-Learning Journey

This project was developed through self-learning as part of my effort to build practical Python automation skills alongside my Electrical Engineering studies.

Key areas I explored independently:
- Python file handling and CSV processing
- Data parsing using `csv.DictReader`
- Implementing weighted GPA calculations
- Debugging real-world issues such as file paths and data formatting
- Designing a simple data processing pipeline

# GPA-Calculator
Python Based GPA Calculator using CSV Automation

This project reflects my initiative to apply programming skills to solve real-world problems.

🧠 Overview

This project is a Python-based GPA Calculator that automates the process of computing a student's weighted GPA using data from a CSV file in which exported from Excel or Google Sheets.

This shows fundamental concepts of:
Data processing
File handling
Automation pipelines
Structured programming

⚙️ Workflow
Excel / Google Sheets → CSV File → Python Script → GPA Calculation → Output

🚀 Features
📂 Reads academic data from CSV file
🔄 Converts letter grades into GPA values
⚖️ Calculates weighted GPA using credit hours
🏆 Classifies academic performance:
FIRST CLASS
DEAN'S LIST
SECOND UPPER
SECOND LOWER
FAIL
🛡️ Handles invalid data safely
🧩 Modular function-based design

🛠️ Tech Stack
Language: Python 3
Libraries: csv
Concepts: File I/O, dictionaries, loops, functions

📂 Project Structure
GPA-Calculator
GPA Calculator 4.py
grades.csv
README.md

📥 Example Input (grades.csv)
Subject,Grade,Credit
Signal & System,A,3
Analog Electronics,A-,3
Engineering Maths 2,A,3
Electrical Engineering Lab,A,1
Electrical Circuit 2,A,3
Ethics,A,2
Academic Writing,A,2

📤 Example Output
Signal & System: Grade=A, GPA=4.0, Credit=3
...

===== FINAL RESULT =====
GPA: 3.94
Classification: FIRST CLASS

▶️ How to Run
Clone this repository:
git clone https://github.com/your-username/GPA-Calculator.git
Navigate into the folder:
cd GPA-Calculator
Make sure your CSV file exists:
grades.csv
Run the script:
python "GPA Calculator 4.py"

🧠 What I Learned
Reading and processing structured data (CSV)
Building reusable functions
Implementing weighted calculations
Debugging file path and data format issues
Designing a simple automation pipeline

🔥 Future Improvements
📊 Add Excel (.xlsx) support using pandas
🖥️ Build GUI interface (Tkinter)
📈 Visualize GPA trends (matplotlib)
☁️ Integrate with Google Sheets API
📄 Export automated reports

📌 About This Project

This project is part of my journey as an Electrical Engineering student to develop Python scripting and automation skills, which are applicable in real-world engineering systems and data processing tasks.
