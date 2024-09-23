register_number = input()
year = int(register_number[4:6])
year = 2000 + year if year < 50 else 1900 + year 


department_code = register_number[6:9]


department_course_map = {
    "104": ("CSE", "BE"),
    "244": ("CSBS", "BT"),
    "205": ("IT", "BT"),
    "243": ("AIDS", "BT"),
    "105": ("EEE", "BE"),
    "106": ("ECE", "BE")
}

department, course = department_course_map.get(department_code)

print(course, department, year) 
