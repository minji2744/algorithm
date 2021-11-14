x = int(input())
count = 0

def a(x):
    if x % 5 == 0:
        return x / 5
    else:
        return None

def b(x):
    if x % 3 == 0:
        return x / 3
    else:
        return None

def c(x):
    if x % 2 == 0:
        return x / 2
    else:
        return None

def d(x):
    return x - 1


def make_1(x):
    if x == 1:
        return 0
    results = [[x]]
    count = 0

    while True:
        rs = results.pop()
        count += 1
        result = []
        for i in rs:
            for func in [a(i), b(i), c(i), d(i)]:
                if func != None:
                    result.append(func)
        if 1 in set(result):
            return count
        else:
            results.append(result)


print(make_1(x))