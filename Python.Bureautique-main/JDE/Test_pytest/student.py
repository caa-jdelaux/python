class Student: #creation of a student class
    def __init__(self, grades = []):
        self.grades = grades
        self.count_grades = len(grades)

    def add_grade(self, grade) :
        if  (grade < 0) | (grade > 20) :
            raise InvalidGrade("Grade should be between 0 and 20")
        else :
            self.grades.append(grade)

    def academic_average(self):
        if len(self.grades) == 0 :
            return 0
        else :
            return sum(self.grades) / len(self.grades)
  
class InvalidGrade(Exception):
    pass

# student = Student()
# student.add_grade(12)
# print(student.academic_average())