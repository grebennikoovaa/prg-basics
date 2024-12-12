def f(subjects):
    highest_avg = -1  
    best_subject = ""
    for subject, grade in subjects.items():
        average_grade = sum(grade)/len(grade)
        if average_grade > highest_avg:
            highest_avg = average_grade
            best_subject = subject
    return best_subject

subjects = {"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}
result = f(subjects)
print(result)
