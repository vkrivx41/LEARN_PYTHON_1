# We can also create our type and use it as an alias to type-hint other variavles or params, in case of re-using it
# again and again in code

# Note: This approach reduces code redundacy and complexity whereas we define a complex type-hint once a use it
# allover the program

tcp_dict = dict[str, list[str]]
student_list = list[dict[str, str]]


def resolve_servers(server: tcp_dict) -> None:
    for name, properties in server.items():
        print(f"NAME: {name}")
        print(f"IP: {properties[0]}")
        print(f"PORT: {properties[1]}")
        print(f"ACTIVE: {properties[2]}")


tcp_servers: tcp_dict = {
    "MainServer": ["1.1.1.1", "80", "yes"],
    "RemoteServer": ["2.2.2.2", "88", "no"]
}
resolve_servers(tcp_servers)

# This will blow errors in python bcs this dict values will flow out of range, but runs well in mypy because there is
# no code type-hinting violations

other_servers: tcp_dict = {
    "Apache": ["1.1.1.1", "80"]
}


# resolve_servers(other_servers)


#


def students_analysis(students: student_list) -> bool:
    for student in students:
        values = list(student.values())

        if len(values) != 3:
            return False
        return True

    return True


students_1: student_list = [
    {'name': "Nik", 'age': "21", 'level': "Advanced"},
    {'name': "Scorpus", 'age': "19", 'level': "Intermediate"},
]

students_2: student_list = [
    {'name': "Nik", 'maths': 89, 'english': 67},
    {'name': "Scorpus", 'maths': 90, 'english': 65},
]

students_3: student_list = [
    {'name': "Nik", 'intelligent': 'True'},
    {'name': "Scorpus", 'intelligent': 'False'},
]


analysis_one = students_analysis(students_1)
analysis_two = students_analysis(students_2)
analysis_three = students_analysis(students_3)

print(analysis_one)
print(analysis_two)
print(analysis_three)
