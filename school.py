import math


def school():
    numberOfTeacher: int = int(input())
    lcm = 0
    for i in range(numberOfTeacher):
        data = int(input())
        if i == 0:
            lcm = data
        else:
            lcm: int = lcm * data // math.gcd(lcm, data)
    """
    gcd(a, b)   : greatest common divisor of integers a and b
    lcm(a,b)    : least common multiple of integers a and b
    
    lcm = (a*b) / gcd(a, b)
    """
    print(int((lcm + 1) % 30))


if __name__ == '__main__':
    school()
