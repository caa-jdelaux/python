from student import Student
import pytest # importing our library of test


# Paramétrage de notre test
@pytest.mark.parametrize("grades, expected_average", [
    ([], 0),
    ([12], 12),
    ([12, 8], 10),
    ([12, 8, 16], 12),
    ([12, 8, 16, 4], 10)
])

# Itération sur les paramètres
def test_academic_average(grades, expected_average):
    student = Student(grades)
    assert student.academic_average() == expected_average
 
# fixture : permet de définir une fonction qui s'exécute avant chaque test
@pytest.fixture
def student():
    return Student()

# 3 test cases are defined in this test suite
def test_create_student_grades(student):
    assert(student.grades) == []
 
def test_create_student_average(student):
    assert student.academic_average() == 0 
 
def test_add_grades(student):
    student.add_grade(12)
    assert student.academic_average() == 12