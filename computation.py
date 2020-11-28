def findBestProgrammer():
    programId = 0
    grade = 0
    countOfProgrammer = 4
    countOfLang = 3  # count of languages
    for i in range(countOfProgrammer):
        data = input().split(" ")
        for j in range(countOfLang):
            if int(data[j]) > int(grade):
                grade = data[j]
                programId = i + 1

    print(programId)


if __name__ == '__main__':
    findBestProgrammer()
