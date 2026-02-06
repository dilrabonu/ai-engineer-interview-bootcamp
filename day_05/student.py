print("="*60)
print("STUDENT CLASS")
print("="*60)

class Student:
    """ Represent a student with academic bahavior"""
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        """Simulate studying -> improves grade"""
        self.grade += 1
        

    def introduce(self) -> str:
        return f"Hello! My name is {self.name} and I am {self.age} years old. My grade is {self.grade}"
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"
# multiple students
students = [
    Student("John", 20, 95),
    Student("Kevin", 24, 92),
    Student("Nice", 18, 100)
]
for s in students:
    print(s.introduce())
    s.study()
    print("After studying:", s)

print("="*60)
print("Thank you for attention!")
print("="*60)
