def test1():
    dict = {}
    a = 2
    def test2():
        nonlocal dict
        dict[1]  = "a"
        a = 3
        print("Inside Inner " , dict)
        print("Inside Inner " , a)
    test2()
    dict[1] = "b"
    print(dict)
    print(a)

test1()