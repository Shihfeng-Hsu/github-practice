def Calculator(a,b,method):
    if method == 'add':
        result = a + b
        print(result)
        return result
    if method == 'minus':
        result = a - b
        print(result)
        return result
    if method == 'plus':
        result = a * b
        print(result)
        return result 
    print("Check the diff")
    print("This is a Calculator(Fake)")