import csv

    # Dictionary 
grade_map = {

        "A": 4.0, "A-": 3.67,
        "B+": 3.33, "B": 3.0, "B-": 2.67,
        "C+": 2.33, "C": 2.0, "C-": 1.67,
        "D+": 1.33, "D": 1.0,
        "F": 0.0
}

def calculate_weighted_gpa(filename):
    total_points = 0
    total_credits =  0 

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            subject  = row["Subject"]
            grade = row["Grade"].upper()
            credit = float(row["Credit"])

            if grade not in grade_map:
                print(f"Invalid grade for {subject}, skipped.")
                continue

            gpa = grade_map[grade]

            total_points += gpa * credit
            total_credits += credit

            print (f"{subject}: Grade = {grade}, GPA = {gpa}, Credit = {credit}")
    
    if total_credits == 0:
        return 0
    
    return round(total_points / total_credits, 4)

def classify_gpa(gpa):
    if gpa >= 3.75:
        return "FIRST CLASS" 
    elif gpa >= 3.50:
        return "DEAN'S LIST"
    elif gpa >= 3.0:
        return "Second Upper"
    elif gpa >= 2.0:
        return "Second Lower"
    else:
        return "FAIL"
        
filename = r"C:\Users\User\Downloads\Python_Notes\Python_Project\grades.csv"

gpa = calculate_weighted_gpa(filename)
classification = classify_gpa(gpa)

print("\n===== FINAL RESULT =====")
print("GPA:", gpa)
print("Classification:", classification)