# 1. Create a list named 'students' with at least 4 student names.
students = ['Alice', 'Bob', 'Charlie', 'Diana']

# 2. Print the first and last student's name using indexing.
# Remember that the first item has an index of 0.
print(students[0])
print(students[3])

# 3. Add a new student to the end of the list.
# Use append() to add a new name to the list.
students = ['Alice', 'Bob', 'Charlie', 'Diana']
students.append('John')
print(students)

# 4. Remove the second student from the list.
students = ['Alice', 'Bob', 'Charlie', 'Diana']
students.remove('Bob')
print(students)

# Use pop()to delete an element by index.
students = ['Alice', 'Bob', 'Charlie', 'Diana']
popped_item = students.pop()
print(popped_item)
print(students)

# 5. Print the updated list.

