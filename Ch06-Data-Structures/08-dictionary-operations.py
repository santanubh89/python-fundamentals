student_scores = {}
student_scores['Foo'] = 85
student_scores['Bar'] = 70
student_scores['Baz'] = 90
print(f'Dictionary: {student_scores}, Type: {type(student_scores)}')

student_scores = dict()
student_scores.update({'Foo': 85, 'Bar': 70, 'Baz': 90})
print(f'Dictionary: {student_scores}, Type: {type(student_scores)}')

student_scores = {'Foo': 85, 'Bar': 70}
#print(f'Baz score = {student_scores["Baz"]}') # KeyError: 'Baz'
print(f'Baz score = {student_scores.get('Baz')}') # None