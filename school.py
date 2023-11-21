class Studen:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self):
        return f'Student with name: {self.name}, Class: {self.current_class}, Id: {self.id}'


class Faculty:
    def __init__(self, name, id, course):
        self.name = name
        self.id = id
        self.course = course
    
    def __repr__(self):
        return f'Faculty Name: {self.name}, Course Name: {self.course}, Id: {self.id}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.student = []
    
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Faculty(name, id, subject)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fees'
        else:
            id = len(self.student) + 1
            student = Studen(name, 'C', id)
            self.student.append(student)
            return f'{name} is enrolled with Id: {id}, Extra Money: {fee - 6500}'
        
    def __repr__(self):
        print(f'Welcome to {self.name}')
        print('------OUR FACULTIES-------')
        for faculty in self.teachers:
            print(faculty)
        print('------OUR STUDENT-------')
        for student in self.student:
            print(student)
        return f'All Done For Now'



# alia = Studen('Alia Torkari', 9, 10)
# ranbeer = Faculty('Douranbedd', 'Algorithm', 101)
# print(alia)
# print(ranbeer)

phitron = School('Phitron')
phitron.enroll('Alia Torkari', 5200)
phitron.enroll('Rani', 8000)
phitron.enroll('Vaijan', 300000)
phitron.enroll('aishawria', 90000)

phitron.add_teacher('Tom crouse', 'DS')
phitron.add_teacher('Kazi Jasim', 'C++')
phitron.add_teacher('Taru MAdam', 'C#')

print(phitron)
