class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'teacher: {self.name}, subject: {self.subject}, id: {self.id}'
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students)  + 1
            student = Student(name, 'C', id)
            self.students.append(student) 
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}' 
                  
    def __repr__(self):
        print('Wellcome to', self.name)
        print('...........OUR Teacher..............')
        for teacher in self.teachers:            
            print(teacher)

        print('............our students.............')
        for student in self.students:
            print(student)
        return f'All done for now'



# arif = Studen('ariful islam', '10th', 12345)
# print(arif)
# arif = Teacher('Abdur Rashid', 'Endlish', 101)
# print(arif)
        

Phitron = School('Phitron')
Phitron.enroll('Md ariful islam', 7000)
Phitron.enroll('tamim', 9000)
Phitron.enroll('rasel', 70000)
Phitron.enroll('rakib', 5000)
Phitron.enroll('jakir', 80000)

Phitron.add_teacher('Shahriar kabir', 'c')
Phitron.add_teacher('shahjahan', 'c++')
Phitron.add_teacher('kamrul', 'DS')
Phitron.add_teacher('Jhankar mahmud', 'PY')

print(Phitron)