import json

student_data = {
    "name": "John",
    "age": 20,
    "grade": "A",
}
with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)
    print(data["name"])
    print(data["age"])
    print(data["grade"])
    
json_string = json.dumps(student_data)
back_to_dict = json.loads(json_string)
print(back_to_dict)
