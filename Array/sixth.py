def reverse_array(L):
    first = 0
    end = len(L) - 1

    while first < end:
        L[first], L[end] = L[end], L[first]
        first += 1
        end -= 1

    return L

numbers = [2, 3, 4, 9, 8]
reversed_numbers = reverse_array(numbers)

for num in reversed_numbers:
    print(num)




