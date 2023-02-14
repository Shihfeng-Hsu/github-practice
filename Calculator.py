def Calculator(a,b,method):
    if method == 'add':
        result = a + b
        print(result)
        return result
    if method == 'minus':
        result = a - b
        print(result)
        return result
    print("This is a Calculator(Fake)")