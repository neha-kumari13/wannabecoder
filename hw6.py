def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("Original list:")
print(input_list)

unique_list = remove_duplicates(input_list)
print("List without duplicates:")
print(unique_list)
