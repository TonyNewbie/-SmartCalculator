from collections.abc import Hashable
object_dict = {}
for object_ in object_list:
    if isinstance(object_, Hashable):
        if object_ in object_dict:
            object_dict[object_] += 1
        else:
            object_dict[object_] = 1
count = 0
for value in object_dict.values():
    if value > 1:
        count += value
print(count)
