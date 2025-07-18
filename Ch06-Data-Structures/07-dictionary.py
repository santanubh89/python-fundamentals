student_scores = {'Foo' : 85, 'Bar': 70, 'Baz': 90}
print(f'Dictionary: {student_scores}, Type: {type(student_scores)}')
print(f'Student map size: {len(student_scores)}')

print(f'Foo score: {student_scores["Foo"]}')

all_students = student_scores.keys()
print(f'All students: {list(all_students)}, Type {type(all_students)}')

all_scores = student_scores.values()
print(f'All scores: {list(all_scores)}, Type {type(all_scores)}')

for name in student_scores:
    print(f'{name} : {student_scores[name]}')

for name, score in student_scores.items():
    print(f'Student {name} score: {score}')

