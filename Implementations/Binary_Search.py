def binary_search(a_list, item):
    # First and last index values
    first = 0
    last = len(a_list) - 1

    found = False

    while first <= last and not found:

        midpoint = (first + last) // 2

        # Match found
        if a_list[midpoint] == item:
            found = True

        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if item < a_list[midpoint]:
                last = midpoint - 1

            # Set up
            else:
                first = midpoint + 1
    return found


# list must already be sorted!
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(a_list, 4))

print(binary_search(a_list, 2.2))
