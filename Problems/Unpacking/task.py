def unpack(input_tuple):
    unpacked = []
    for hobby in input_tuple:
        if isinstance(hobby, tuple):
            unpacked.extend(list(hobby))
        else:
            unpacked.append(hobby)
    return tuple(unpacked)
