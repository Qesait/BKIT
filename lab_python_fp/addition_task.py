if __name__ == '__main__':
    a = [1, 2, 3]
    print([(i, i*i) for i in a])
    print(list(zip(a, (i * i for i in a))))
    print(list(map(lambda i: (i, i * i), a)))
    print(list(zip(a, map(lambda i: i * i, a))))
