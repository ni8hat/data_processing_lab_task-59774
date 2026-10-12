"""EXERCISE 5"""

"""• Student Dictionary

Create a dictionary containing a student's name, ID, department, and CGPA. Print each key and value using a for loop. Then check the CGPA and display 'Good Standing' if the CGPA is 2.50 or higher; otherwise display 'Academic Warning'."""


print()
student_info = {
                "name" : "Nishat",
                "ID": "24-59774-3",
                "department": "data science",
                "cgpa": 3.89
                }

for i in student_info:
    print(f"{i} is {student_info[i]}")

if student_info["cgpa"] >= 2.5:
    print("good standing")
else:
    print("academic warning")


    