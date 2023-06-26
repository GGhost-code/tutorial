def recursive_len(some_list):
    return 1 + recursive_len(some_list[:-1]) if some_list else 0
print(recursive_len([1, 2, 3]))