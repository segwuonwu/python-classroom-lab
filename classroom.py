class Assignment:
    def __init__(self, name, github_url=""):
        self.name = name
        self.github_url = github_url
        self.completed = False
        self.grade = None
    
    def mark_done(self, grade):
        self.completed = True
        self.grade = grade

class Student:
    def __init__(self, name):
        self.name = name
        self.pending_homeworks = []
        self.completed_homeworks = []

    def assign_homework(self, assignment):
        self.pending_homeworks.append(assignment)

    def complete_homework(self, name, grade):
        for i in range(len(self.pending_homeworks)):
            homework = self.pending_homeworks[i]
            if homework.name == name:
                homework.mark_done(grade)
                self.completed_homeworks.append(self.pending_homeworks.pop(i))
                break

    def print_outstanding_homeworks(self):
        missing_hw = []
        for homework in self.pending_homeworks:
            missing_hw.append(homework.name)
        if len(missing_hw) == 0:
            print(f'{self.name} has no outstanding homeworks!')
        else:
            print(f'{self.name} still needs to turn in', missing_hw)

class SeiClass:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def assign_homework(self, assignment):
        for student in self.students:
            student.assign_homework(assignment)


henry = Student('Henry')
sarah = Student('Sarah')
mike = Student('Mike')
print(f"""Student:
    Name: {henry.name}
    Pending: {henry.pending_homeworks}
    Completed: {henry.completed_homeworks}""")

sei26 = SeiClass('sei26')
sei26.add_student(henry)
sei26.add_student(sarah)
sei26.add_student(mike)


assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')
print(f"""Assignment 1: 
    Name: {assignment1.name} 
    Url: {assignment1.github_url} 
    Completed: {assignment1.completed} 
    Grade: {assignment1.grade}""")

print("Assigned a homework to the class")
sei26.assign_homework(assignment1)
print(f"""Student:
    Name: {henry.name}
    Pending: {henry.pending_homeworks}
    Completed: {henry.completed_homeworks}""")
print(f"""Student:
    Name: {sarah.name}
    Pending: {sarah.pending_homeworks}
    Completed: {sarah.completed_homeworks}""")

henry.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

henry.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
mike.print_outstanding_homeworks()