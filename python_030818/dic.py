students = {
  'best': 'Mittens',
  'worst': 'Jason'
}
# or
#students = dict(best='Mittens', worst='Jason')

students['worst'] = 'Paul'
print(students)
print(students['best'])
students['food'] = 'pizza'
print(students)

del students['best']
print(students)
students['favorite_foods'] = ['pizza', 'chicken']
print(students['favorite_foods'][1])

contact = {
  'name': 'Paul',
  'favorite_foods': {
    'fast': 'burgers',
    'italian': 'pizza'
  }
}
print(contact['favorite_foods']['italian'])
print(contact.get('lst_name'))

# look through the dic. look at the key and value.
for key, value in students.items():
    print('{}:{}'.format(key, students[key]))
    
rgb = [255,255,255]
rgb = {'r': 255, 'g': 255,'b': 255}
print(rgb['r'])