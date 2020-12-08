def fastSort(numbers, sortedNumbers):
    if len(numbers) <= 0:  # if numbers is empty, return
        return
    if len(numbers) == 1:
        sortedNumbers.append(numbers[0])
        return
    pivot = numbers[0]
    l = []
    r = []
    repeat = 0  # Pivot may be repeated several times in numbers
    for num in numbers:
        if num < pivot:
            l.append(num)
        elif num > pivot:
            r.append(num)
        else:
            repeat += 1
    fastSort(l, sortedNumbers)
    for j in range(repeat):
        sortedNumbers.append(pivot)
    fastSort(r, sortedNumbers)


if __name__ == '__main__':
    numbers = list(map(int, input().split(' ')))
    sortedNumbers = []
    fastSort(numbers, sortedNumbers)
    sortedNumbersStr = ''
    for num in sortedNumbers:  # convert to string
        sortedNumbersStr += (str(num) + ' ')
    print(sortedNumbersStr)
