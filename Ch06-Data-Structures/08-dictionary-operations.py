student_scores = {}
student_scores['Foo'] = 85
student_scores['Bar'] = 70
student_scores['Baz'] = 90
print(f'Dictionary: {student_scores}, Type: {type(student_scores)}')

student_scores = dict()
student_scores.update({'Foo': 85, 'Bar': 70, 'Baz': 90})
print(f'Dictionary: {student_scores}, Type: {type(student_scores)}')

# Retrieve
student_scores = {'Foo': 85, 'Bar': 70}
#print(f'Baz score = {student_scores["Baz"]}') # KeyError: 'Baz'
print(f'Baz score = {student_scores.get('Baz')}') # None

# updating value for a key
student_scores['Baz'] = 80
print(f'student scores after update: {student_scores}')

# Add elements
student_scores.update({'John': 65, 'Doe': 95})
print(f'student scores after update: {student_scores}')

# Remove element
removed_element = student_scores.pop('Doe')
print(f'Removed element: {removed_element}, updated score: {student_scores}')

removed_element = student_scores.popitem()
print(f'Removed element: {removed_element}, updated score: {student_scores}')

# Zipping two arrays to a dictionary
students = ['Foo', 'Bar', 'Baz']
scores = [85, 70, 90]
student_scores = dict(zip(students, scores))
print(f'Dictionary: {student_scores}, Type: {type(student_scores)}')

# Clear content of a dictionary
student_scores.clear()
print(f'Dictionary after clear: {student_scores}')