odd_numbers = {1, 3, 5, 7, 9}
even_numbers = {0, 2, 4, 6, 8}

# Union - creates a new set
all_numbers = odd_numbers | even_numbers
print(f'All numbers (union): {all_numbers}')

cities1 = {'Delhi', 'Madrid', 'New York', 'Tokyo'}
cities2 = {'New York', 'London', 'Paris', 'Delhi'}
all_cities = cities1.union(cities2)
print(f'All cities (union): {all_cities}')

# Intersection - common elements between two sets
common_cities = cities1.intersection(cities2)
print(f'Common cities: {common_cities}')

# Intersection_Update - puts only common cities on first set
cities1.intersection_update(cities2)
print(f'Common cities: {cities1}')

# Update - updates on the first set
num_set_1 = {1, 2, 5, 6}
num_set_2 = {2, 4, 6, 8}
num_set_1.update(num_set_2)
print(f'After update: {num_set_1}')

# Symmetric difference
cities1 = {'Delhi', 'Madrid', 'New York', 'Tokyo'}
cities2 = {'New York', 'London', 'Paris', 'Delhi'}
non_common_cities = cities1.symmetric_difference(cities2)
print(f'Symmetric difference: {non_common_cities}') # 'London', 'Madrid', 'Tokyo', 'Paris'

# Symmetric difference update - updates first city with non-common values
cities1.symmetric_difference_update(cities2)
print(f'Symmetric difference: {cities1}') # 'London', 'Madrid', 'Tokyo', 'Paris'

# Difference - Present in first but not present in second
difference = cities1.difference(cities2)
print(f'Difference: {difference}')

# Is subset/superset/disjoint
all_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
odd_nums = {1, 3, 5, 7, 9}
even_nums = {0, 2, 4, 6, 8}
is_all_nums_superset = all_nums.issuperset(odd_nums)
is_odd_nums_subset = odd_nums.issubset(all_nums)
print(f'Is all numbers superset: {is_all_nums_superset}')
print(f'Is odd numbers subset: {is_odd_nums_subset}')
is_odd_even_disjoint = odd_nums.isdisjoint(even_nums)
print(f'Are all numbers different: {is_odd_even_disjoint}')

# Remove element
even_nums.discard(0)
even_nums.discard(8)
print(f'Even numbers after discarding 0 and 8: {even_nums}')

removed_el = even_nums.pop()
print(f'Removed element: {removed_el}, updated set: {even_nums}')

odd_nums.clear()
print(f'Set after clear: {odd_nums}')