class Student:
    def __init__(self, name, contact, id) -> None:
        self.name = name
        self.contact = contact
        self.id = id
    def __repr__(self) -> str:
        return f'Student Name: {self.name}, Contact: {self.contact}, ID: {self.id}'
    
class Faculty:
    def __init__(self, name, sub, id) -> None:
        self.name = name
        self.sub = sub
        self.id = id
    def __repr__(self) -> str:
        return f'Faculty Name: {self.name}, Course Name: {self.sub}, Id: {self.id}'
    
class Activities:
    def __init__(self, activity_name, winner) -> None:
        self.activity_name = activity_name
        self.winner = winner
    def __repr__(self) -> str:
        return f'Activity Name: {self.activity_name} and our winner is: {self.winner}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.faculties = []
        self.activities = []
    
    def add_faculties(self, name, sub):
        id = len(self.faculties) + 1010
        faculty = Faculty(name, sub, id)
        self.faculties.append(faculty)

    def add_students(self, name, contact):
        id = len(self.students) + 3
        student = Student(name, contact, id)
        self.students.append(student)
    
    def activities_m(self, activity_name, winner):
        activity = Activities(activity_name, winner)
        self.activities.append(activity)
    
    def __repr__(self) -> str:
        print('------Welcome to The Rom-Roma Coaching-------')
        print('-----Our Faculties Name------')
        for faculti in self.faculties:
            print(faculti)
        print('--------our Students-------')
        for st in self.students:
            print(st)
        print('----------our activity----------')
        for ac in self.activities:
            print(ac)

        return f'This is Our Prthom School'
    
gi_thub = School('Github School Girls')

gi_thub.add_faculties('Jahirul Bhuiyan', 'Rom Roma Bebsha')
gi_thub.add_faculties('Ashraf Ali', 'Balir Gonon')
gi_thub.add_faculties('Bebshatul Kali', 'Kacha Jahl')

gi_thub.add_students('Shahin', 'Noakhali')
gi_thub.add_students('rasel', 'dhaka')
gi_thub.add_students('farhan', 'boroguna')

gi_thub.activities_methods('Runnig - 100m', 'Jabbar Kaka')
gi_thub.activities_methods('Gobor dour', 'kala Nazmul')
gi_thub.activities_methods('khonon bij bopon', 'Baper chele')

print(gi_thub)