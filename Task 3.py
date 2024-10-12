
def repeated_elements(numbers):
    element_count = {}
    repeated_count = 0


    for value in numbers:
        if value in element_count:
            element_count[value] += 1
        else:
            element_count[value] = 1


    for count in element_count.values():
        if count > 1:
            repeated_count += 1

    return repeated_count


numbers = [2, 3, 4, 2, 7, 8, 3, 9, 10, 4]
print(repeated_elements(numbers))
