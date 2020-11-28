def game():
    count = int(input())
    data = map(int, input().split(" "))  # convert to int array
    sortedNumbers = sorted(data)
    newArray = ''
    chain: int = int(count / 2)
    for i in range(chain):
        newArray += (str(sortedNumbers.pop()) + ' ')  # pop biggest of number
        newArray += (str(sortedNumbers[i]) + ' ')  # add smallest of number
    if count % 2 != 0:  # if the size of data input is odd, The last index left is placed at the end of the array.
        newArray += (str(sortedNumbers.pop()) + ' ')

    print(newArray)


if __name__ == '__main__':
    game()
