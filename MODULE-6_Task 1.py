students = {
    "Tarini": 99,
    "Rama": 90,
    "Samriddhi": 78,
    "Nikhil": 92,
    "Daksh": 98
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Student '{name}' not found in the records.")
  
