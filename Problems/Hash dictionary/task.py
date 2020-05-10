# create your dictionary here
from collections.abc import Hashable
objects_dict = {}
for item in objects:
    if isinstance(item, Hashable):
        objects_dict[item] = item.__hash__()
