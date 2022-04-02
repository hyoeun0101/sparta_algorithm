# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때,
#  출석하지 않은 학생의 이름을 반환하시오.
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나"]

# O(N)
def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:
        student_dict[key] = True
    for key in present_array:
        del student_dict[key]
    return list(student_dict.keys())


print(get_absent_student(all_students, present_students))