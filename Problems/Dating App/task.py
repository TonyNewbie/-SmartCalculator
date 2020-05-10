# the list "girls" is already defined
suitable_girls = []
for girl in girls:
    if girl['education'] == 'MIT' and girl['about']:
        suitable_girls.append(girl['name'])
print(', '.join(suitable_girls))
